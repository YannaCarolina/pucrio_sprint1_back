from flask import Flask, jsonify, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    frequency = db.Column(db.String, nullable=False)
    health_info = db.Column(db.String, nullable=False)
    obs = db.Column(db.String, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'owner': self.owner,
            'breed': self.breed,
            'frequency': self.frequency,
            'health_info': self.health_info,
            'obs': self.obs,
        }

api = Api(app, version='1.0', title='Pet API', description='A simple CRUD API for pets', prefix='/api')
ns = api.namespace('pets', description='Pets operations')

pet_model = api.model('Pet', {
    'id': fields.Integer(readonly=True, description='The pet unique identifier'),
    'name': fields.String(required=True, description='The pet name'),
    'age': fields.Integer(required=True, description='The pet age'),
    'owner': fields.String(required=True, description="The owner's name"),
    'breed': fields.String(required=True, description='The pet breed'),
    'frequency': fields.String(required=True, description='The frequency of pet boarding'),
    'health_info': fields.String(required=True, description='The pet health information'),
    'obs': fields.String(required=True, description='Other important details about the pet'),
})

@ns.route('/')
class PetList(Resource):
    @ns.doc('list_pets')
    @ns.marshal_list_with(pet_model)
    def get(self):
        pets = Pet.query.all()
        return [pet.serialize for pet in pets]

    @ns.doc('create_pet')
    @ns.expect(pet_model)
    @ns.marshal_with(pet_model, code=201)
    def post(self):
        new_pet_data = request.json
        new_pet = Pet(
            name=new_pet_data['name'],
            age=new_pet_data['age'],
            owner=new_pet_data['owner'],
            breed=new_pet_data['breed'],
            frequency=new_pet_data['frequency'],
            health_info=new_pet_data['health_info'],
            obs=new_pet_data['obs']
        )
        db.session.add(new_pet)
        db.session.commit()
        return new_pet.serialize, 201

@ns.route('/<int:id>')
@ns.response(404, 'Pet not found')
@ns.param('id', 'The pet identifier')
class PetResource(Resource):
    @ns.doc('get_pet')
    @ns.marshal_with(pet_model)
    def get(self, id):
        pet = Pet.query.get_or_404(id)
        return pet.serialize

    @ns.doc('delete_pet')
    @ns.response(204, 'Pet deleted')
    def delete(self, id):
        pet = Pet.query.get_or_404(id)
        db.session.delete(pet)
        db.session.commit()
        return '', 204

    @ns.doc('update_pet')
    @ns.expect(pet_model)
    @ns.marshal_with(pet_model)
    def put(self, id):
        pet = Pet.query.get_or_404(id)
        updated_data = request.json
        pet.name = updated_data['name']
        pet.age = updated_data['age']
        pet.owner = updated_data['owner']
        pet.breed = updated_data['breed']
        pet.frequency = updated_data['frequency']
        pet.health_info = updated_data['health_info']
        pet.obs = updated_data['obs']
        db.session.commit()
        return pet.serialize

if __name__ == '__main__':
    app.run(debug=True)

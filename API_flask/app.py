from flask import Flask, jsonify, request # type: ignore
import os
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS 



app = Flask(__name__)

api = Api(app)

ns = api.namespace('pets', description='Pets operations')

pet = api.model('Pet', {
    'id': fields.Integer(readonly=True, description='The pet unique identifier'),
    'name': fields.String(required=True, description='The pet name'),
    'age': fields.String(required=True, description='The pet age'),
    'owner': fields.String(required=True, description="The owner's name"),
    'breed': fields.String(required=True, description='The pet breed'),
    'frequency': fields.String(required=True, description='The frequency of pet boarding'),
    'health_info': fields.String(required=True, description='The pet health informations'),
    'obs': fields.String(required=True, description='Other important details about the pet'),
})
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    age = db.Column(db.Integer) #birth_date
    owner = db.Column(db.String)
    breed = db.Column(db.String)
    frequency = db.Column(db.String)
    health_info = db.Column(db.String)
    obs = db.Column(db.String)
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

@ns.route('/api/pets') #tenho uma rota que busco informações sobre os pets
class Petlist(Resource):
    '''Shows a list of all pets'''
    @ns.doc('list_pets')
    @ns.marshal_list_with(pet)
    def get(self):
        pets = Pet.query.all() #traz todos os pets que tem no banco
        #print(dir(pets[0]))
        #print(pets[0].age)
       # return jsonify({'pets':[{'id': pet.id, 'name': pet.name, 'age': pet.age, 'owner': pet.owner, 'breed':pet.breed, 
       #              'frequency': pet.frequency, 'health_info': pet.health_info, 'obs': pet.obs} for pet in pets]}) #transforma a queryset em um json para rota, que nao reconhece pets. 
        return [pet.serialize for pet in Pet.query.all()]

@ns.route('/api/add/<int:id>', methods = ["POST","PUT"])
class PetResource(Resource):
    '''Add a pet'''
    def post(id):
        new_pet_data = request.get_json()
        if id:
            pet = Pet.query.get(id)
            if not pet:
                return jsonify({'message': 'Pet not found'}), 404
            pet.name = new_pet_data['name']
            pet.age = new_pet_data['age']
            pet.owner = new_pet_data['owner']
            pet.breed = new_pet_data['breed']
            pet.frequency = new_pet_data['frequency']
            pet.health_info = new_pet_data['health_info']
            pet.obs = new_pet_data['obs']
            db.session.commit()
            return jsonify({'message': f'Pet {pet.name} updated successfully'})
        #print(new_pet_data)
        new_pet = Pet(name = new_pet_data['name'], age = new_pet_data['age'], owner = new_pet_data['owner'], breed = new_pet_data['breed'],
                    frequency = new_pet_data['frequency'], health_info = new_pet_data['health_info'], obs = new_pet_data['obs'])
        db.session.add(new_pet)
        db.session.commit()
        return {'id': new_pet.id, 'name': new_pet.name, 'age': new_pet.age, 'owner': new_pet.owner, 'breed':new_pet.breed, 
                        'frequency': new_pet.frequency, 'health_info': new_pet.health_info, 'obs': new_pet.obs}

@app.route('/api/delete/<int:id>', methods = ["DELETE"])
def delete_pet(id):
    pet = Pet.query.get(id)
    if not pet:
        return jsonify({'message': 'Pet not found'}), 404
    db.session.delete(pet)
    db.session.commit()
    return jsonify({'message': f'Pet {pet.name} deleted successfully'})



#ns.add_resource(Petlist, '/api/pets')

if __name__ == '__main__':
    app.run(debug=True)
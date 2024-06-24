from flask import Flask, jsonify # type: ignore
import os
from flask_sqlalchemy import SQLAlchemy # type: ignore


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    owner = db.Column(db.String)
    breed = db.Column(db.String)

@app.route('/')
def index():
    return "Hello Yan"

@app.route('/api/pets', methods = ["GET"]) #tenho uma rota que busco informações sobre os pets
def get_pets():
    pets = Pet.query.all() #traz todos os pets que tem no banco
    return jsonify(pets) #transforma a queryset em um json para rota, que nao reconhece pets. 







if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# sqlalchemy db uri
basedir = os.path.abspath(os.path.dirname(__name__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

# class/model
class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category  = db.Column(db.String(100), unique=True)
    hobbies = db.Column(db.String(100))
    environment = db.Column(db.String(200))

    # init
    def __init__(self, category, hobbies, environment):
        self.category = category
        self.hobbies = hobbies
        self.environment = environment

# hobby schema, fields allow to show
class HobbySchema(ma.Schema):
    class Meta:
        fields = ('id', 'category', 'hobbies', 'environment')

# Init schema
hobby_schema = HobbySchema()
hobbies_schema = HobbySchema(many=True)

# add hobby to db
@app.route('/hobby', methods=['POST'])
def add_hobby():
    category = request.json['category']
    hobbies = request.json['hobbies']
    environment = request.json['environment']

    new_hobby = Hobby(category, hobbies, environment)

    db.session.add(new_hobby)
    db.session.commit()

    return hobby_schema.jsonify(new_hobby)


# Get all hobbies
@app.route('/hobby', methods=['GET'])
def get_hobbies():
    all_hobbies = Hobby.query.all()
    result = hobbies_schema.dump(all_hobbies)
    return jsonify(result)


# Get one hobby
@app.route('/hobby/<id>', methods=['GET'])
def get_hobby(id):
    hobby = Hobby.query.get(id)
    return hobby_schema.jsonify(hobby)

# delete hobby
@app.route('/hobby/<id>', methods=['DELETE'])
def delete_hobby(id):
    hobby = Hobby.query.get(id)
    db.session.delete(hobby)
    db.session.commit()

    return hobby_schema.jsonify(hobby)

# update hobby
@app.route('/hobby/<id>', methods=['PUT'])
def update_hobby(id):
    hobby = Hobby.query.get(id)

    category = request.json['category']
    hobbies = request.json['hobbies']
    environment = request.json['environment']

    hobby.category = category
    hobby.hobbies = hobbies
    hobby.environment = environment

    db.session.commit()

    return hobby_schema.jsonify(hobby)



if __name__ == '__main__':
    app.run(debug=True)
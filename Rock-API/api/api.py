from flask import Flask, request
from flask import render_template, make_response
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class RockMod(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

class RockRate(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

db.create_all()


def generate_id():
    while True:
        ids = random.randint(100, 10000)
        result = RockMod.query.filter_by(id=ids).first()
        if result is None:
            return ids


rock_put_args = reqparse.RequestParser()
rock_put_args.add_argument(
    "name", type=str, help="Name of the rock is required. Please put rock name lmao", required=True)
rock_put_args.add_argument(
    "desc", type=str, help="You need a rock description.", required=True)
rock_put_args.add_argument(
    "image", type=str, help="Add an image url for the rock lol", required=True)
rock_put_args.add_argument(
    "rating", type=str, help="You gotta give a rating lmao", required=True)

rock_update_args = reqparse.RequestParser()
rock_update_args.add_argument(
    "name", type=str, help="Name of the rock is required. Please put rock name lmao")
rock_update_args.add_argument(
    "desc", type=str, help="You need a rock description.")
rock_update_args.add_argument("image", type=str, help="Yes, image url...")
rock_update_args.add_argument(
    "rating", type=str, help="The whole point is to give a rating")


resource_fields = {
    'name': fields.String,
    'desc': fields.String,
    'image': fields.String,
    'rating': fields.Integer
}


trusted_ips = ['144.172.83.214']


class Rockss(Resource):
    @marshal_with(resource_fields)
    def get(self, name):
        #Best rock - finds the rock with 5 stars and picks random
        if name == "random":
            randomresult = RockMod.query.all()
            thing = random.choice(randomresult)
            return thing
        if name == "top":
            randomresult4 = RockMod.query.filter_by(rating=4).all()
            randomresult5 = RockMod.query.filter_by(rating=5).all()
            result = random.choice([randomresult4,randomresult5])
            rock = random.choice(result)
            return rock
        
        result = RockMod.query.filter_by(name=name).first()
        if not result:
            name = name.lower() + " rock"
            result = RockMod.query.filter_by(name=name).first()
            if not result:
                abort(404, message="Could not find rock with that name... :(")
        return result, 200

    @marshal_with(resource_fields)
    def put(self, name):
        idss = generate_id()
        args = rock_put_args.parse_args()
        result = RockMod.query.filter_by(name=name).first()
        if result:
            abort(409, message=f"Rock name taken...")
        rockk = RockMod(id=idss, name=args['name'], desc=args['desc'],
                        image=args['image'], rating=args['rating'])
        db.session.add(rockk)
        db.session.commit()
        return rockk, 201

    @marshal_with(resource_fields)
    def patch(self, name):
        args = rock_update_args.parse_args()
        result = RockMod.query.filter_by(name=name).first()
        if not result:
            abort(404, message="Rock doesn't exist, cannot update :(((")

        if args['name']:
            result.name = args['name']
        if args['desc']:
            result.desc = args['desc']
        if args['image']:
            result.image = args['image']
        if args['rating']:
            result.rating = args['rating']

        db.session.commit()

        return result


class RateRock(Resource):
    def patch(self, name):
        args = rock_update_args.parse_args()
        result = RockMod.query.filter_by(name=name).first()
        if not result:
            abort(404, message="Rock doesn't exist, cannot rate.")
        if args['rating']:
            if int(args['rating']) < 1:
                abort(406, message="Must be above 0.")
            if int(args['rating']) > 5:
                abort(406, message="Must be below 6.")
        result.rating = args['rating']

        db.session.commit()

        abort(201, message="Rated rock!")

class NoRock(Resource):
    def get(self):
        abort(200, message="View the github at https://github.com/mr-conos/rock-api")

api.add_resource(Rockss, "/rock/<string:name>")
api.add_resource(RateRock, "/rate/<string:name>")
api.add_resource(NoRock, "/")

if __name__ == "__main__":
    app.run(debug=False)
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class RockMod(db.Model):
	name = db.Column(db.String(50), nullable=False, primary_key=True)
	desc = db.Column(db.String, nullable=False)
	image = db.Column(db.String, nullable=False)
	rating = db.Column(db.Integer, nullable=False)



rock_put_args = reqparse.RequestParser()
rock_put_args.add_argument("name", type=str, help="Name of the rock is required. Please put rock name lmao", required=True)
rock_put_args.add_argument("desc", type=str, help="You need a rock description.", required=True)
rock_put_args.add_argument("image", type=str, help="Add an image url for the rock lol", required=True)
rock_put_args.add_argument("rating", type=str, help="You gotta give a rating lmao", required=True)

rock_update_args = reqparse.RequestParser()
rock_update_args.add_argument("name", type=str, help="Name of the rock is required. Please put rock name lmao")
rock_update_args.add_argument("desc", type=str, help="You need a rock description.")
rock_update_args.add_argument("image", type=str, help="Yes, image url...")
rock_update_args.add_argument("rating", type=str, help="The whole point is to give a rating")


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
		result = RockMod.query.filter_by(name=name).first()
		if not result:
			abort(404, message="Could not find rock with that name... :(")
		return result

	@marshal_with(resource_fields)
	def put(self, name):
		if request.remote_addr not in trusted_ips:
		    abort(403)

		args = rock_put_args.parse_args()
		result = RockMod.query.filter_by(name=name).first()
		if result:
			abort(409, message="Rock name taken...")

		rockk = RockMod(name=args['name'], desc=args['desc'],image=args['image'],rating=args['rating'])
		db.session.add(rockk)
		db.session.commit()
		return rockk, 201

	@marshal_with(resource_fields)
	def patch(self, name):
	    if request.remote_addr not in trusted_ips:
		    abort(403)
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


api.add_resource(Rockss, "/rock/<string:name>")

if __name__ == "__main__":
	app.run(debug=False)

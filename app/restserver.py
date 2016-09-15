from flask import jsonify, abort, make_response
from flask_restful import Resource, reqparse, fields, marshal
from app import app, db, api
from models import User, Interests

user_fields     = { 'id':fields.Integer, 'username':fields.String, 'email':fields.String }  
interest_fields = { 'user_id':fields.Integer, 
					'books':fields.String,
					'movies':fields.String,
					'tvshows':fields.String,
					'food':fields.String,
					'hobbies':fields.String,
					'hate':fields.String,
					'dreams':fields.String,
					'dreamcity':fields.String }

class UserAPI(Resource):
#	decorators = [auth.login_required]
	
	def __init__(self):
	
		self.reqparse = reqparse.RequestParser()
		
		self.reqparse.add_argument('username', type=str, required=True,
									help='No Username provided',
									location='json')

		self.reqparse.add_argument('password', type=str, required=True,
									help='No Password provided',
									location='json')

		self.reqparse.add_argument('email', type=str, required=True,
									help='No EMail provided',
									location='json')
		super(UserAPI, self).__init__()


	def get(self, id):
		user = User.query.get(id)
		if user is None:
			abort(404)
		return {'user': marshal(user, user_fields)}

	def post(self):
		args = self.reqparse.parse_args()
		new_user = User(username=args['username'], password=args['password'], email=args['email'])
		
		user1 = User.query.filter_by(email=new_user.email).first()
		user2 = User.query.filter_by(username=new_user.username).first()

		if user1 is not None or user2 is not None:
			abort(409)
		
		db.session.add(new_user)
		db.session.commit()
		return {'user':marshal(new_user, user_fields)}

class InterestsAPI(Resource):

	def __init__(self):
		
		self.reqparse = reqparse.RequestParser()

		self.reqparse.add_argument('user_id', type=int, required=True,
									help='No UserID provided',
									location='json')
	
		self.reqparse.add_argument('books', type=str, required=True,
									help='No Books provided',
									location='json')
		
		self.reqparse.add_argument('movies', type=str, required=True,
									help='No Movies provided',
									location='json')
		
		self.reqparse.add_argument('tvshows', type=str, required=True,
									help='No TVShows provided',
									location='json')
		
		self.reqparse.add_argument('food', type=str, required=True,
									help='No Username provided',
									location='json')
		
		self.reqparse.add_argument('hobbies', type=str, required=True,
									help='No Hobbies provided',
									location='json')
		
		self.reqparse.add_argument('hate', type=str, required=True,
									help='No Hate provided',
									location='json')
	
		self.reqparse.add_argument('dreams', type=str, required=True,
									help='No Dreams provided',
									location='json')
		
		self.reqparse.add_argument('dreamcity', type=str, required=True,
									help='No Dreamcity provided',
									location='json')

	def get(self, user_id):
		interests = Interests.query.filter_by(user_id=user_id).first()
		if interests is None:
			abort(404)
		return { 'interests': marshal(interests, interest_fields) }
	
	def post(self):
		args = self.reqparse.parse_args()
		new_interests = Interests(user_id = args['user_id'],
								books = args['books'],
								movies = args['movies'],
								tvshows = args['tvshows'],
								food = args['food'],
								hobbies = args['hobbies'],
								hate = args['hate'],
								dreams = args['dreams'],
								dreamcity = args['dreamcity'])
		
		interests1 = Interests.query.filter_by(user_id=new_interests.user_id).first()

		if interests1 is not None:
			interests1.modify(new_interests)
		else:
			db.session.add(new_interests)
		db.session.commit()
		return {'interest':marshal(new_interests,interest_fields)}
	
	
api.add_resource(UserAPI, '/api/users/<int:id>', endpoint='user')
api.add_resource(UserAPI, '/api/users', endpoint='user_add')
api.add_resource(InterestsAPI, '/api/interests/<int:user_id>', endpoint='interests')
api.add_resource(InterestsAPI, '/api/interests', endpoint='interests_add')

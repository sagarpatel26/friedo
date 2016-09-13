from flask import jsonify, abort, make_response
from flask_restful import Resource, reqparse, fields, marshal
from app import app, db, api
from models import User

user_fields = { 'id':fields.Integer, 'username':fields.String, 'email':fields.String }  

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

'''
class InterestsAPI(Resource):

	def __init__(self):
		
		self.reqparse = reqparse.RequestParser()
		
		self.reqparse.add_argument('user_id', type=str, required=True,
									help='No Username provided',
									location='json')
'''
api.add_resource(UserAPI, '/api/user/<int:id>', endpoint='user')
api.add_resource(UserAPI, '/api/user/add', endpoint='user_add')

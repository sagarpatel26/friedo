from flask import jsonify, abort, make_response, request, g, url_for
from flask_restful import Resource, reqparse, fields, marshal
from app import app, db, api, auth
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

@auth.verify_password
def verify_password(username_or_token, password):
# first try to authenticate by token
	user = User.verify_auth_token(username_or_token)
	if not user:
	# try to authenticate with username/password
		user = User.query.filter_by(username=username_or_token).first()
		if not user or not user.verify_password(password):
			return False

	g.user = user
	return True

class UserAPI(Resource):
	
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
	
	@auth.login_required
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



@app.route('/api/token')
@auth.login_required
def get_auth_token():
	token = g.user.generate_auth_token(600)
	ints = Interests.query.get(g.user.id)
	first_time = False
	if ints is None:
		first_time = True
	return jsonify({'user_id':g.user.id, 'username':g.user.username, 'email':g.user.email,'token': token.decode('ascii'), 'duration': 600, 'first_time':first_time})



from friedo_brain import get_top
@app.route('/api/suggested_friends/<int:user_id>')
#@auth.login_required
def get_suggested_friends(user_id):
	ai = Interests.query.all()
	a = {'all_interests': marshal(ai, interest_fields)}
	id_l = get_top(user_id, 10, a)
	us_l = []
	for ids in id_l:
		u = User.query.get(int(ids))
		us_l.append(u.username)
	
	return jsonify({'SFL':us_l})

@app.route('/api/verify_token')
@auth.login_required
def verify_token():
	return jsonify({'message':'this is secured!!'})




@app.route('/api/all_interests')
def all_interests():
	ai = Interests.query.all()
	return jsonify({ 'all_interests': marshal(ai, interest_fields)})

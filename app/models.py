from app import db, app
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(260))
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, password, email):
		self.username = username
		self.password = generate_password_hash(password)
		self.email    = email

	def __repr__(self):
		return '<User %r>' % (self.username)


	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)
	
	def verify_password(self, password):
		return check_password_hash(self.password, password)
	
	def generate_auth_token(self, expiration=600):
		s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
		return s.dumps({'id': self.id})

	@staticmethod
	def verify_auth_token(token):
		s= Serializer(app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None    # valid token, but expired
		except BadSignature:
			return None    # invalid token
		user = User.query.get(data['id'])
		return user

class Interests(db.Model): 

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	books = db.Column(db.String(30))
	movies = db.Column(db.String(30))
	tvshows = db.Column(db.String(30))
	food = db.Column(db.String(30))
	hobbies = db.Column(db.String(30))
	hate = db.Column(db.String(30))
	dreams = db.Column(db.String(30))
	dreamcity = db.Column(db.String(30))

	def __init__(self,
				 user_id,
				 books,
				 movies,
				 tvshows,
				 food,
				 hobbies,
				 hate,
				 dreams,
				 dreamcity):

		self.user_id = user_id
		self.books = books
		self.movies = movies
		self.tvshows = tvshows
		self.food = food
		self.hobbies = hobbies
		self.hate = hate			# DDU, Android
		self.dreams = dreams
		self.dreamcity = dreamcity
		
	def modify(self, other):
		
		assert type(other) == Interests, 'Interests.modify the other is not an instance of Interests class.'

		self.books = other.books
		self.movies = other.movies
		self.tvshows = other.tvshows
		self.food = other.food
		self.hobbies = other.hobbies
		self.hate = other.hate			# DDU, Android
		self.dreams = other.dreams
		self.dreamcity = other.dreamcity
	
	def __repr__(self):
		return '<Interest %r>' % self.id

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(260))
	email = db.Column(db.String(120), unique=True)

	def __repr__(self):
		return '<User %r>' % (self.username)

class Interests(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	books = db.Column(db.String(10))
	movies = db.Column(db.String(10))
	tvshows = db.Column(db.String(10))
	food = db.Column(db.String(10))
	hobbies = db.Column(db.String(10))
	hate = db.Column(db.String(10))
	dreams = db.Column(db.String(10))
	dreamcity = db.Column(db.String(10))
	
	def __repr__(self):
		return '<Interest %d>' % id

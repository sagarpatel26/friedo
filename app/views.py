from flask import request
from app import app
from models import User

@app.route('/')
def index():
	return 'Welcome to Freido /n By Sagar Patel & Chaitya Shah!!'

@app.route('/login', methods=['POST'])
def login():
	if request.json is None:
		return 'BAD'
	
	if  'username' not in request.json and 'password' not in request.json:
		return 'BAD'
	
	username = request.json['username']
	password = request.json['password']

	user = User.query.filter_by(username = username).first()
	
	if user is None:
		return 'No user found!'

	print user.password, password
	if password != user.password:
		return 'Wrong Password!'
	
	return 'OK'+str(user.id)

@app.route('/api/questions', methods=['GET'])
def getQuestions():
	with open('./app/questions.json') as questions_json:
		return questions_json.read()
	questions_json.close()

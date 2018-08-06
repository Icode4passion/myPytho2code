from flask import Flask
from flask_restplus import Resource , Api

app = Flask('__name__')
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
	"""docstring for HelloWorld"""
	def get(self):
		return {'hello':'world'}

if __name__ == '__main__':
	app.run(debug = True)
		

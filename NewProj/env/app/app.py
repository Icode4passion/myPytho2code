from flask import Flask,render_template,request

app = Flask(__name__)

# @app.route('/')
# def index():
# 	return 'Hello My App'

# @app.route('/hello/<name>')
# def hello_world(name):
# 	return 'Hello this is %s page'% name

# @app.route('/hello')
# def hello():
# 	return 'Under Hello'

# @app.route('/python')
# def python():
# 	return 'python'

# @app.route('/page/<int:id>')
# def show_page(id):
# 	return 'Page Number %d'% id

# @app.route('/admin')
# def hello_admin():
# 	return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
# 	return 'Hello Guest %s'% guest

# @app.route('/user/<name>')
# def hello_user(user):
# 	if name == 'admin':
# 		return redirect(url_for('hello_admin'))
# 	else :
# 		return redirect(url_for('hello_guest',guest = name))


# @app.route('/hello/<user>')
# def index(user):
# 	return render_template('hello.html', name = user)


# @app.route('/mark/<int:score>')
# def marks(score):
# 	return render_template('score.html' , marks = score)

@app.route('/state')
def book_details():
	dist = {'telangana':'hyderabad','karnataka':'bangaore','tamilnadu':'chennai','maharastra':'mumbai'}
	return render_template('state.html', details = dist)

# @app.route('/person')
# def biodata():
# 	my_lst = {'First Name':'Mahesh',
# 				'Last Name' : 'Rao',
# 				'Phone': '1234567',
# 				'HNo' : '1-4-123/B',
# 				'Street':'Gachibowli',
# 				'City' : 'Hyderabad',
# 				'State': 'Telangana',
# 				'Pin':'500032'
# 	}
# 	return render_template('personal.html', list = my_lst)

# @app.route('/')
# def hello_js():
# 	return render_template('index.html')


# @app.route('/')
# def student():
# 	return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#    	result = request.form
#    	return render_template("result.html",result = result)





if __name__ == '__main__':
	app.run(debug = True)
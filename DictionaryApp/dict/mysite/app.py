from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template("index.html")

@app.route('/',methods=["POST"])
def my_form_post():
	text = request.form['text']
	p_text = text.upper()
	return p_text

if __name__ == '__main__':
	app.run()


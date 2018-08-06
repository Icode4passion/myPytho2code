from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from flask.ext.security  import Security , SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password1!@localhost/flaskmovie'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_HASH'] = "plaintext"

db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(255), unique=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))

#     def __init__(self,id,username,email,password):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.password = password
    
# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='testuser@gmail.com', password='password')
#     db.session.commit()


@app.route('/')
def index():
    myUser = User.query.all()
    return render_template('index.html',myUser = myUser)

@app.route('/post_user', methods=["GET","POST"])
def post_user():
    user = User(request.form['id'],
        request.form['username'],
        request.form['email'],
        request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/profile/<email>')
def profile(email):
    user = User.query.filter_by(email=email).first()
    return render_template('profile.html',user=user)


if __name__ == "__main__":
    app.run(debug=True)
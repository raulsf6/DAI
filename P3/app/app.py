from flask import Flask, session
from flask import render_template
from flask import request
import random
from pickleshare import PickleShareDB

app = Flask(__name__)

app.secret_key = 'randomKey'
db = PickleShareDB('./testdb')
db['Users'] = {}
db['Users']['Raul'] = {}
db['Users']['Raul']['name'] = "Raúl" 
db['Users']['Raul']['password'] = "12345"
db['Users']['Raul']['email'] = "raulsf66@gmail.com"
db['Users']['Raul']['address'] = "C/ Imagine" 

@app.route('/')
def index():
    handle_session(session, request)
    
    return render_template("index.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))

@app.route('/login', methods = ['GET'])
def login():
    handle_session(session, request)

    return render_template("login.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))

@app.route('/login', methods = ['POST'])
def login_form():
    form_user = request.form.get('user')
    form_passwd = request.form.get('password')
    user = db['Users'].get(form_user, {})
    passwd = user.get('password')
    if (passwd == form_passwd):
        session['logged'] = True
        session['user'] = user
        session['visited'] = []
        session['visited'].append(request.base_url)

    return render_template("login.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))


@app.route('/signup', methods = ['GET'])
def signup():
    handle_session(session, request)

    return render_template("signup.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))

@app.route('/signup', methods = ['POST'])
def signup_form():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    password = request.form.get('password')

    user = {
        'name': name,
        'email': email,
        'address': address,
        'password': password
    }

    db['Users'][name] = user

    session['logged'] = True
    session['user'] = user
    session['visited'] = []
    session['visited'].append(request.base_url)

    return render_template("signup.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))

@app.route('/contacto')
def contacto():
    handle_session(session, request)

    return render_template("login.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))

@app.route('/quienessomos')
def quienes_somos():
    handle_session(session, request)

    return render_template("login.html", logged=session.get('logged', False), user=session.get('user', None), visited=session.get('visited', None))
    

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


def handle_session(session, request):
    if 'logged' in session:
        session['logged'] = True
        session['visited'].insert(0, request.base_url)
        if (len(session['visited']) > 3):
            session['visited'] = session['visited'][0:3]
        else:
            session['visited'] = session['visited']
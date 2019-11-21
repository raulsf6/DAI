from flask import Flask, session
from flask import render_template
from flask import request
import re
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'randomKey'
client = MongoClient("mongo", 27017)
db = client.SampleCollections



@app.route('/')
def index():
    query = request.args.get('query', -1)

    if (query == -1):
        pokemons = db.samples_pokemon.find({})
    else:
        query = re.compile(query, re.IGNORECASE)
        pokemons = db.samples_pokemon.find({"name":query})
    
    print(pokemons)
    return render_template("index.html", pokemons=pokemons)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
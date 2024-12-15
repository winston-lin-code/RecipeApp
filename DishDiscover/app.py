from flask import Flask, request, render_template,redirect
import requests
import json
from pymongo import MongoClient
app = Flask(__name__)
API_KEY = "256cf3fe85184a72afd5f83c8159e7d9"
BASE_URL = "https://api.spoonacular.com/recipes/autocomplete"
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://winstonlin0714:cool@cluster0.7wxik.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client.dish_discovery_db
collection = db.items


@app.route('/')
def index():
 
 
    return render_template('index.html')
@app.route('/pantry')
def pantry():
    items = collection.find() 
    item_list = [item['Ingredient'] for item in items]
    return render_template('pantry.html', items=item_list)
@app.route('/add_item', methods = ['POST'])
def add_item():
    item_name = request.form.get('item')
    print("ITEM NAME ", item_name)
    if item_name:
        collection.insert_one({'Ingredient':item_name})
    return redirect('http://localhost:5000/pantry',code=302)
@app.route('/favorite')
def favorite():
    return render_template('favorite.html')
if __name__ == '__main__':
    app.run(debug=True)
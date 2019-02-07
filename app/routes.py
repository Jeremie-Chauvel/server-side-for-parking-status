from flask import render_template
import json
import requests
from app import app

url = "localhost:5000/parking_update"

parking = [
        {
            "id": 1,
            "place": 3
            },
        {
            "id": 2,
            "place": 0
            }
    ]

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', parking=parking)

@app.route('/update/<int:id_>/<int:place>', methods=['GET', 'POST'])
def update(id_, place):
    """requete pour mettre à jour le nombre de palce dans une allé"""
    if id_ in (1,2) and place in (0,1,2,3):
        parking[id_-1]["place"] = place
    return json.dumps(parking)

@app.route('/get_update', methods=['GET'])
def get_update():
    """requete pour recuperer l'état des allés"""
    return json.dumps(parking)


from flask import render_template
import json
from app import app

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
parking_status = [
        {
            "id": 1,
            "stat": "000"
            },
        {
            "id": 2,
            "stat": "111"
            }
    ]
@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', parking=parking)

@app.route('/update/<int:id_>/<alle_stat>', methods=['GET', 'POST'])
def update(id_, alle_stat):
    """requete pour mettre à jour le nombre de palce dans une allé"""
    if id_ in (1,2) and len(alle_stat) == 3 and ("1" in alle_stat or "0" in alle_stat):
        parking[id_-1]["place"] = convert_to_place(alle_stat)
        parking_status[id_-1]["stat"] = alle_stat
    return json.dumps(parking_status)

@app.route('/get_update', methods=['GET'])
def get_update():
    """requete pour recuperer l'état des allés"""
    return json.dumps(parking_status)

def convert_to_place(alle_stat):
    place = 3
    for k in alle_stat:
        place -= int(k)
    return place
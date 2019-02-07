from flask import render_template
from flask import jsonify
import request
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

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', parking=parking)

@app.route('/update/<int:id>/<int:place>', methods=['GET', 'POST'])
def update(id_, place):
    """requetes pour mettre à jour le nombre de palce dans une allé"""
    if id_ in (1,2) and place in (0,1,2,3):
        parking[id_-1]["place"] = place


# server.py

import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('flask_app/model/y_pred1.pkl','rb'))

@app.route('/result', methods=['GET', 'POST'])
def result():
    #data = request.get_json(force=True)
    y_pred = model.predict(id)
    
    lott_type = request.form["type"]
    id = request.form["id"]
    
    return jsonify(y_pred)



if __name__ == '__main__':
    app.run(port=5000, debug=True)   
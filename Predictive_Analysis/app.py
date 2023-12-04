import csv
from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

def read_csv(file_name):
    coordinates = []
    csv_path = "static/"+file_name
    df = pd.read_csv(csv_path)

    for row in df.iterrows():

        latitude = float(row['DeliveryLocation(Latitude)'])
        longitude = float(row['DeliveryLocation(Longitude)'])
        coordinates.append({"latitude": latitude, "longitude": longitude})

    return coordinates

@app.route('/coordinates/all_orders', methods=['GET'])
def get_coordinates():

    try:
        coordinates = read_csv(file_name="food_delivery_data")
        return jsonify({"coordinates": coordinates})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/coordinates/burger_orders', methods=['GET'])
def get_coordinates():

    try:
        coordinates = read_csv(file_name="Burger_Orders.csv")
        return jsonify({"coordinates": coordinates})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/coordinates/pasta_orders', methods=['GET'])
def get_coordinates():
    
    try:
        coordinates = read_csv(file_name="Pasta_Orders.csv")
        return jsonify({"coordinates": coordinates})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/coordinates/pizza_orders', methods=['GET'])
def get_coordinates():
    
    try:
        coordinates = read_csv(file_name="Pizza_Orders.csv")
        return jsonify({"coordinates": coordinates})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/coordinates/sandwhiches', methods=['GET'])
def get_coordinates():

    try:
        coordinates = read_csv(file_name="Sandwhiches_Orders.csv")
        return jsonify({"coordinates": coordinates})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/coordinates/sushi', methods=['GET'])
def get_coordinates():
    
    try:
        coordinates = read_csv(file_name="Sushi_Orders.csv")
        return jsonify({"coordinates": coordinates})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

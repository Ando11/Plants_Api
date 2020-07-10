from flask import Flask, request, jsonify
# import request
# from flask_sqlalchemy import SQLAlchemy 
# from flask_marshmallow import Marshmallow 
import os, json 

app=Flask(__name__)

@app.route('/', methods=['GET']) #'/'=empty route
def get():
    return jsonify({'msg': 'Hello I\'m Ubuntu'})

if __name__== '__main__':
    app.run(debug=True) 


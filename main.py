import os
import flask
from flask import request, jsonify, flash
from flask_restful import reqparse
# from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from run import model


app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def home():
    return "<h1>You have reached to the server of DeepFake Detection</h1>"

@app.route('/upload', methods=['POST'])
def result():
    dataParser = reqparse.RequestParser()
    dataParser.add_argument('name')
    dataParser.add_argument('file')
    data = dataParser.parse_args()
    name = data['name']
    file= data['file']

    result = model(file)
    print(name, file)
        
    return jsonify(result)

# app.secret_key = os.urandom(24)
app.run()
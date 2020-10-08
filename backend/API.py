import flask
from flask import request, jsonify, Response
import pickle
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app,supports_credentials=True)

@app.route('/', methods=['GET'])
def home():
    return ""


@app.route('/api/v1/users/login', methods=['POST'])
def api_login():
    #read in user objects
    users = pickle.load(open("users.pickle","rb"))
    body = request.form
    reqUser = body["username"]
    reqPass = body["passHash"]
    for i in users["users"]:
        if(i["username"]==reqUser and i["passHash"] == reqPass):
            return "Success",200
    return "Invalid Credentials",400


@app.route('/api/v1/lists/get', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    lists = pickle.load(open("lists.pickle","rb"))
    for i in lists["lists"]:
        if(i["id"] == id):
            return i,200
    return "",400

app.run()

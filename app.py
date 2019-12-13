from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "Hello test!"

@app.route("/greeting")
def greeting():
    name = request.args.get('name')
    return "<p><h3>Hello "+name+"</h3></p>"

@app.route("/testjson")
def testjson():
    get_id = request.args.get('id')
    d = dict()
    d['id']=get_id
    d['score']=[{'quiz1':20,'quiz2':30,'quiz3':25},{'quiz1':21,'quiz2':23,'quiz3':19}]
    return jsonify(d)

@app.route("/insertmenu")
def insertmenu():
 	client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
 	db = client.student_scores
 	file = open('menu.csv', 'r')
 	list_of_menu = []
 	for line in file:
 		menu = line.split(',')
 		m = {'item':menu[0], 'store':int(menu[4]), 'cal':int(menu[2]), 'filter':menu[1], 'price':menu[3]}
 		list_of_menu.append(m)
	db.menus.delete_many({})
 	result = db.menus.insert_many(list_of_menu, ordered=False)
 	return "upload done"

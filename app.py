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

@app.route("/insertscore")
def getscore():
	client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
	db = client.student_scores
	file = open('score.csv', 'r')
	list_of_score = []
	for line in file:
		score = line.split(',')
		score = [int(e) for e in score]
		dscore = {'id':score[0], 'quiz1':score[1], 'quiz2':score[2], 'quiz3':score[3], 'quiz4':score[4], 'quiz5':score[5], 'sum': sum(score[1:])}
		list_of_score.append(dscore)
	db.scores.delete_many({})
	result = db.scores.insert_many(list_of_score, ordered=False)
	return "upload done"

@app.route("/insertmenu")
 def getscore():
 	client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
 	db = client.student_scores
 	file = open('menu.csv', 'r')
 	list_of_menu = []
 	for line in file:
 		menu = line.split(',')
 		m = {'item':menu[0], 'store':int(menu[1]), 'cal':int(menu[2]), 'filter':menu[3], 'price':menu[4]}
 		list_of_menu.append(m)
 	result = db.menus.insert_many(list_of_menu, ordered=False)
 	return "upload done"

 @app.route("/showmenu")
 def showmenu():
 	client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
 	db = client.icanteen_menus
 	getid = request.args.get('store_number')
 	docs = db.menus.find({'store':int(getid)})
 	r = []
 	for doc in docs:
 		ret = {'item':doc[0], 'store':int(doc[1]), 'cal':int(doc[2]), 'filter':doc[3], 'price':doc[4]}
 		r.append(ret)
 	return jsonify(r)

@app.route("/findscore")
def findscore():
	client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
	db = client.student_scores
	getid = request.args.get('id')
	docs = db.scores.find_one({'id':int(getid)})
	ret = {'id':docs['id'], 'quiz1':docs['quiz1'], 'quiz2':docs['quiz2'], 'quiz3':docs['quiz3'], 'quiz4':docs['quiz4'], 'quiz5':docs['quiz5'], 'sum':docs['sum']}
	r = dict()
	r['data'] = ret
	return jsonify(r)

@app.route("/showscore")
def showscore():
	client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
	db = client.student_scores
	docs = db.scores.find({'quiz1':9})
	allscore = []
	for doc in docs:
		ret = {'id':doc['id'], 'quiz1':doc['quiz1'], 'quiz2':doc['quiz2'], 'quiz3':doc['quiz3'], 'quiz4':doc['quiz4'], 'quiz5':doc['quiz5'], 'sum':doc['sum']}
		allscore.append(ret)
	return jsonify(allscore)

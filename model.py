#import logging
import pdb
import pymongo
from flask import Flask,request
from flask_pymongo import PyMongo 
from config import MongoDB 


# logging.basicConfig(level=logging.INFO)

class Mongo(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()

	# # 	self.arg = arg
	# app.config['MONGO3_HOST'] = 'another.host.example.com'
	# app.config['MONGO3_PORT'] = 27017
	# app.config['MONGO3_DBNAME'] = 'dbname_three'
	# mongo3 = PyMongo(app, config_prefix='MONGO3')
	# app = Flask(__name__)
	
	@staticmethod 
	def linkdb():
		connection = pymongo.MongoClient('127.0.0.1',27017)
		tdb = connection.api
		post = tdb.api
		
		post.insert({"id":"1", "url":"30", "ss":"Python"})
		print("donw")


		# io= PyMongo(app)
		# con=io.db.api.find()
		# if con:
		# 	print io,"conc\n"

		# 	return True
		# else:
		# 	return "db contion fail"
	
	@staticmethod 
	def findid():
		connection = pymongo.MongoClient()
		db = connection.api
		apiTable = db.api
		
		alist=apiTable.find()
		api=[]

		
		

		print alist
		# pdb.set_trace()
		
		# pdb.set_trace()
		for i in alist:
			i.pop('_id')
			api.append(i)
		print api
    # return dict(result='success',li=api )
    	# return json.dumps(api)
	
		# return id
if __name__ == '__main__':
	# app = Flask(__name__)
	# Mongo.linkdb()
	Mongo.findid()

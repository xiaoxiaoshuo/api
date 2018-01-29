from flask import Flask,request
from flask_pymongo import PyMongo 
from config import MongoDB 
import json
from flask import jsonify
from flask_cors import CORS
import logging
import pdb
logging.basicConfig(level=logging.INFO)

class mongodb(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()

	# 	self.arg = arg
	
	@staticmethod 
	def linkdb(app,config_prefix="MONGO"):
		# app = Flask(__name__)
		io= PyMongo(app)
		con=io.db.api.find()
		if con:
			print io,"conc\n"

			return True
		else:
			return "db contion fail"

	@staticmethod 
	def findid(app):
		io= PyMongo(app,config_prefix="MONGO")
		id=io.db.api.find({},{id:1}).sort({id:1}).limit(1)
		return id

		

#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2017/9/21 08:19 
# @Author  : Swper 
# @Site    : http://www.58jb.com/ 
# @File    : config.py 
# @Software: PyCharm 
 
#MONGODB CONFIG 
class MongoDB(): 
    MONGO_HOST = "127.0.0.1" 
    MONGO_PORT = 27017 
    MONGO_DBNAME = "api" 

    #def __init__(self, alist,api,connection,db,apiTable):
	# 	self.connection = pymongo.MongoClient('127.0.0.1',27017)
	# 	self.db = connection.api
	# 	self.apiTable = db.api
		
	# 	self.alist=apiTable.find()
	# 	self.api=[]
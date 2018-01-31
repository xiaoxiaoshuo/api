# -*- coding: utf-8 -*-
"""
    flask.helpers
    ~~~~~~~~~~~~~

    Implements various helpers.

    :copyright: (c) 2018 by xiaoxiaoshuo.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask,request
from flask_pymongo import PyMongo 
from config import MongoDB 
import json
from flask import jsonify
from flask_cors import CORS
import logging
import pdb

logging.basicConfig(level=logging.INFO)



#reauest method of check
def handelMethods(method,requestMethod):
    if method==requestMethod:
        print method,requestMethod,"t\n"
        return True
    else:
        print method,requestMethod,"f\n"
        #return requestMethod,"error  request method"
        return jsonify({"msg":"error request method","code":400})
        # return False
    

def checkRequestParemeter(requestData):
    if requestData=="" or requestData==None:#why
        return jsonify({"msg":"requestData for None","code":400})
        print "\trequest data:",type(requestData),"\tdata:"+requestData
    else:
        try:
            print "\trequest data two:",type(requestData),"\tdata:"+requestData
            

            dataOb=eval(requestData)
            # pdb.set_trace()
            print dataOb.get('url'),"xianshi\n"
            # print dataOb['url'],"url\n"
            print type(dataOb.get('url'))
            # pdb.set_trace()
            if dataOb.get('url')==None or dataOb.get('method')==None:

                return jsonify({"msg":"url or method feil lose","code":400})
            else:
                if dataOb['url']=="" or dataOb['method']=="":
                    pdb.set_trace()
                    return jsonify({"msg":"url or method for null","code":400})
                    pdb.set_trace()
                else:
                    # print "\tto dict data:",type(dataOb),"\t",dataOb
                    return "zio"
                        

            # return ""
        except Exception as ex:
            print "\nconvert object fail"
            return jsonify({"code":500,"msg":"service fail"})


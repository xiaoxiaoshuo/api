from flask import Flask,request
from flask_pymongo import PyMongo 
#from config import MongoDB 
import json
from flask import jsonify
from flask_cors import CORS
import logging
import pdb
from model import Mongo
from helpers import handelMethods,checkRequestParemeter
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

CORS(app)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     # users = mongo.db.api.insert({"ss":3}) 
#     #return render_template('index.html',onlines_users=onlines_users) 
#     # if users:
#         # return "aa"
#     # else:
#         # return  "add"
#     return render_template('index.html')
# def jsonStyle():

#     pass

    
@app.route('/apilist', methods=['GET'])
def apilist():
    apilist=mongo.db.api.find()
    api=[]
    for i in apilist:
        i.pop('_id')
        api.append(i)


    # return dict(result='success',li=api )
    return json.dumps(api)

@app.route('/api/saveapi' ,methods=['GET', 'POST','PUT','DELETE','OPTIONS'])
def saveapi():
    # request.method=='POST'

    if handelMethods('POST',request.method) or checkRequestParemeter(request.get_data()):
        # return "ceshi1"
        # requestData=
        mo=Mongo()
        link=mo.linkdb(app)
        if link:
            print link
            id=mo.findid(app)
            print id,"id\n"
            pdb.set_trace()
            return "xx"
            pdb.set_trace()

        else:
            pass
            return mo.linkdb(app)
        
    else:
        # return jsonify({"msg":"error request method","code":400})
        # return "zio" 
        # return "cuowufanfa"
        if handelMethods('POST',request.method):
            pass
            return handelMethods('POST',request.method),
        else:
            return checkRequestParemeter(request.get_data())
    
    

    # return 'ceshi'

    # if requestData=="":#why
    #     return json.dumps({"msg":"requestData for None","code":400})
    #     print "\trequest data:",type(requestData),"\tdata:"+requestData
    # else:
    #     try:
    #         print "\trequest data:",type(requestData),"\tdata:"+requestData
    #         dataOb=eval(requestData)
    #         if dataOb.get('url')==None:
    #             return json.dumps({"msg":"url feil lose","code":400})
    #             if dataob['url']=="":
    #                 return json.dumps({"msg":"url for null","code":400})
    #             else:
    #                 return ""

    #         print "\tto dict data:",type(dataOb),"\t",dataOb

    #         return ""
    #     except Exception as ex:
    #         print "\nconvert object fail"
    #         return json.dumps({"code":500,"msg":"service fail"})

        

    


    # isin=data.find('url')
    
    
    # dataob=json.loads(datajson)

  
    # dataob=dict(data)
    
    #dict={'url':url,'method':method,'head':head,'body':body}
    # users = mongo.db.api.insert(dict) 
    # dict={'url':url}
    
    # if isin==-1:
    #     print isin
    #     print "no saveapicon"
    #     return "no saveapi"
    # else:
    #     #mongo.db.api.insert(datajson) 
    #     print "saveapi"
        # return "saveapi to data success"
    # return ""
    
    
       
    # return render_template('index.html')

# if __name__ == '__main__':
app.run(host='0.0.0.0',debug=True)
    
    
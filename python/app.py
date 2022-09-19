import os
import flask
import pymongo
import json
from flask import request, jsonify

username=os.environ['MONGO_INITDB_ROOT_USERNAME']
password=os.environ['MONGO_INITDB_ROOT_PASSWORD']

myclient = pymongo.MongoClient("mongodb://{}:{}@mongo:27017/".format(username,password))
app = flask.Flask(__name__)
app.config["DEBUG"] = True

dblist = myclient.list_database_names()
mydb = myclient["mydatabase"]
mycoll = mydb["names"]

# use this api to fetch data to users
@app.route('/api/v1/database/fetch', methods=['GET'])
def fetch_data():

    data = []

    raw_data=mycoll.find()

    for i in raw_data:
        i['_id'] = str(i['_id'])
        data.append(i)

    return(jsonify(data))

#use this api to insert new data
@app.route('/api/v1/database/insert', methods=['POST'])
def insert_data():

    arguments=request.args.to_dict()

    mycoll.insert_one(arguments)

    return("Insertion Successful")

#use this api to update data. Under development
#@app.route('/api/v1/database/update', methods=['PATCH'])
#def patch_data():

#use this api to delete data
@app.route('/api/v1/database/delete', methods=['DELETE'])
def delete_data():

    arguments=request.args.to_dict()

    mycoll.delete_many(arguments)

    return("Deletion Successful")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)

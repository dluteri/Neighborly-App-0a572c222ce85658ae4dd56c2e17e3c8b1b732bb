import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        # try:
        url = "mongodb://lutericosmosdb:7rA5smehaujVZGLqpX7GShYdzniOU8N31gQUPysYP5voOGqUL1GMfUXB4HqcfvaQl6lEuMf1V32G3hofaoDwDA==@lutericosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lutericosmosdb@"
        client = pymongo.MongoClient(url)
        database = client['luteridb']
        collection = database['posts']

        query = {'_id': str(id)}
        result = collection.find_one(query)
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        # except:
        #     return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
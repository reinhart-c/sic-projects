from flask import Flask, request
from pymongo.mongo_client import MongoClient
import datetime

getSensorData = Flask(__name__)

@getSensorData.route("/")
def entry_point() :
    return "Welcome to the API for Applikasi Menerima Data Sensor"

@getSensorData.route("/sensor1", methods = [ "POST" ] ) 
def menyimpan_atau_mengirimkan_sensor_data() :
    if  request.method == "POST" :
        body = request.get_json()
        uri = ""
        client = MongoClient(uri)
        database_for_processing = client["db"]
        collection_data_suhu = database_for_processing["data"]
        collection_data_suhu.insert_one({ "timestamp" : str( datetime.datetime.now() ), "data_sensor_kelembapan" : body["hum"] , "data_sensor_suhu" : body["temp"]})
        return "Sukses menerima Data kelembapan dan Data suhu pada waktu : " + str( datetime.datetime.now()  )
    else :
       return { "list_kelembapan_saat_ini" : list_kelembapan,
               "list_suhu_saat_ini" : list_suhu }
    
if __name__ == "__main__" :
    list_kelembapan = []
    list_suhu = []
    getSensorData.run( debug= True)
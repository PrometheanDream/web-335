from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name":"Crash",
    "last_name":"Bandicoot",
    "email":"tikitiki@me.com",
    "employee_id":"0005",
    "date_created":datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id":"0005"}))
import pymongo
from datetime import *

today = date.today()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["vehiclesDB"]
mycol = mydb["Cars"]


for x in mycol.find({}, {"Fitness Validity":1, "_id":0}):
  datestr = x["Fitness Validity"]
  datestr = datestr.replace("-", " ")
  dateobj = datetime.strptime(datestr, '%d %b %Y')
  if(dateobj.date() > today):
      print("Fit")

  else:
      print("Unfit")

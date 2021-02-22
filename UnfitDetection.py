import pymongo
from datetime import *
from NumberPlateRecog import ImgToStr

today = date.today()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["vehiclesDB"]
mycol = mydb["Cars"]


def vehicleFinder(numplate):
    x = mycol.find_one({"Vehicle Number": numplate})

    if x is None:
        return None

    datestr = x["Fitness Validity"]
    datestr = datestr.replace("-", " ")
    dateobj = datetime.strptime(datestr, '%d %b %Y')
    if (dateobj.date() > today):
        print("Fit")
    else:
        print("Unfit")
        mycol.find_one_and_update(
            {"Vehicle Number": numplate},
            {"$set": {"Unfitflag": "1"}},
            upsert=True
        )
    print(x["Model"])
    print(x["Vehicle Number"])


# vehicleFinder(ImgToStr("Activa.jpg"))

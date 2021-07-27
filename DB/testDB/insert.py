import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testDB"]
mycol = mydb["testCollection"]

def function():
    key = 0+1
    answer = "yes"
    def insertToDB():
        mylist = [
        { "_id": key, "value": answer}
        ]
        x = mycol.insert_many(mylist)
    insertToDB()
function()

#print a list of the _id values of the inserted documents:
# print(x.inserted_ids)

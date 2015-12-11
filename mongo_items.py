import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("ds027415.mongolab.com", 27415)
db = client.todoshuchang
db.authenticate("todo", "todo")

def mongo_get_items(status = -1):
    if (status >= 0):
        items = db.items.find({'status':status})
    else:
        items = db.items.find()
    items = [ item for item in items ]
    for item in items:
        item["id"] = str(item["_id"])
        item["_id"] = None
    return items

def mongo_new_item(task, status):
    db.items.insert({'task': task, 'status': status})

def mongo_get_item(id):
    item = db.items.find_one({"_id":ObjectId(id)})
    if (item):
        item["id"] = str(item["_id"])
        item["_id"] = None
    return item

def mongo_save_item(item):
    id = ObjectId(item['id'])
    db.items.update_one(
        {"_id":id},
        {"$set":{
            "task":item["task"],
            "status":item["status"]
        }}
    )

def mongo_discard_item(id):
    id = ObjectId(id)
    db.items.delete_one({"_id":id})

# if __name__ == "__main__":
#     db.items.delete_many({})
#     print(get_items())
#     new_item("more really new stuff",0)
#     new_item("another really, really new stuff",1)
#     items = get_items(-1)
#     id = None
#     for item in items:
#         print (item)
#         id = str(item["id"])
#     print("----")
#     print(id)
#     print ('-----')
#     item = get_item(id)
#     print(item)
#     item['task'] = "new version:" + item['task']
#     print(item)
#     save_item(item)
#     print(item)


from tinydb import TinyDB, where


db = TinyDB('./todo.db.json')

def tiny_get_items(status = -1):
    if (status >= 0):
        items = db.search(where('status') == status)
    else:
        items = db.search(where('status') >= 0)
    return items
    
def tiny_new_item(task, status):
    eid = db.insert({'task': task, 'status': status})
    db.update({'id':eid}, eids=[eid])
    
def tiny_get_item(id):
    item = db.get(eid = id)
    return item

def tiny_save_item(item):
    eid = item['id']
    db.update({
        'task':item['task'],
        'status':item['status']
    }, eids=[eid])

def tiny_discard_item(id):
    eid = id
    db.remove(eids=[eid])
#

# if __name__ == "__main__":
#     new_item("more really new stuff",0)
#     new_item("another really, really new stuff",1)
#     items = get_items(-1)
#     for item in items:
#         print (item)
#     print ('-----')
#     item = get_item(3)
#     item['task'] = "new version:" + item['task']
#     save_item(item)
#     print(item)
     

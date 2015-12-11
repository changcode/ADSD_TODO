from bottle import default_app, run, route, get, post, request, template, static_file
from items import *
from mongo_items import *

if __name__ == "__main__":
    HOME = "./"
else:
    HOME = "/home/ChangCode/mysite/"

import sqlite3
from peewee import *


database = SqliteDatabase(HOME+'todo.db')

class BaseModel(Model):
    class Meta:
        database = database

class Todo(BaseModel):
    status = BooleanField()
    task = CharField()

    class Meta:
        db_table = 'todo'

#mongoDB
@get('/mongodb')
@get('/mongodb/<status:int>')
def mongo_get_list(status=-1):
	items = mongo_get_items(status)
	result = []
	for item in items:
		result.append((item['id'],item['task'],item['status']))
	return template('mongo_list', rows=result)

@get('/mongodb/new')
def mongo_get_new():
	return '''
        <p>Enter a new item...</p><br/>
        <form action="/mongodb/new" method="post">
            To be done: <input name="task" type="text" />
            <input value="Save" type="submit" />
        </form>
    '''

@post('/mongodb/new')
def mongo_post_new():
	task = request.forms.get('task', '').strip()
	mongo_new_item(task,1)
	return mongo_get_list()

@get('/mongodb/edit/<id:re:[a-z0-9]+>')
def mongo_get_edit(id):
	item = mongo_get_item(id)
	print(item['task'])
	return template('mongo_edit', id=id, task=item['task'], status=item['status'])

@post('/mongodb/edit/<id:re:[a-z0-9]+>')
def mongo_post_edit(id):
	task = request.forms.get('task', '').strip()
	status = request.GET.get('status','').strip()
	if status == 'open':
		status = 1
	else:
		status = 0
	item = mongo_get_item(id)
	item['task'] = task
	item['status'] = status
	mongo_save_item(item)
	return mongo_get_list()

@get('/mongodb/delete/<id:re:[a-z0-9]+>')
def mongo_confirm_delete_item(id):
	item = mongo_get_item(id=id)
	return template('mongo_delete', id=id, task=item['task'], status=item['status'])

@post('/mongodb/delete/<id:re:[a-z0-9]+>')
def mongo_delete_item(id):
	mongo_discard_item(id)
	return mongo_get_list()


#tinyDB

@route('/tinydb')
@route('/tinydb/<status:int>')
def tinydb(status=-1):
	items = tiny_get_items(status)
	result = []
	for item in items:
		result.append((item['id'],item['task'],item['status']))
	return template('tinydb', rows=result)

@get('/tinydb/new')
def get_new():
    return '''
        <p>Enter a new item...</p><br/>
        <form action="/tinydb/new" method="post">
            To be done: <input name="task" type="text" />
            <input value="Save" type="submit" />
        </form      '''

@post('/tinydb/new')
def post_new():
    task = request.forms.get('task', '').strip()
    tiny_new_item(task,1)
    return tinydb()

@get('/tinydb/edit/<id:int>')
def get_edit(id):
    item = tiny_get_item(id)
    return template('tinydb_edit', id=id, task=item['task'], status=item['status'])

@post('/tinydb/edit/<id:int>')
def post_edit(id):
	task = request.forms.get('task', '').strip()
	status = request.GET.get('status','').strip()
	if status == 'open':
		status = 1
	else:
		status = 0
	item = tiny_get_item(id)
	item['task'] = task
	item['status'] = status
	tiny_save_item(item)
	return tinydb()

@get('/tinydb/delete/<id:int>')
def confirm_delete_item(id):
	item = tiny_get_item(id)
	return template('tinydb_delete_view', id=id, task=item['task'], status=item['status'])

@post('/tinydb/delete/<id:int>')
def delete_item(id):
	tiny_discard_item(id)
	return tinydb()

#PeeWee
@route('/model')
def model_list():
	query = Todo.select().where(Todo.status).order_by(Todo.task.asc())

	result = []

	for todo in query:
		result.append((todo.id,todo.task,todo.status))

	output = template('model_list_view', rows=result)
	return output

#sqlite3
@route('/todo')
@route('/todo/<status:int>')
def todo_list(status=-1):
	conn = sqlite3.connect(HOME+'todo.db')
	c = conn.cursor()
	if (status >= 0):
		c.execute("SELECT id, task, status FROM todo WHERE status LIKE '"+str(status)+"'")
	else:
		c.execute("SELECT id, task, status FROM todo")
	result = c.fetchall()
	output = template('make_table', rows=result)
	return output

@get('/new') # or @route('/login')
def new_item_request():
	return template('new')

@post('/new')
def new_item():
	new = request.forms.get('task', '').strip()

	conn = sqlite3.connect(HOME+'todo.db')
	c = conn.cursor()

	c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
	new_id = c.lastrowid

	conn.commit()
	c.close()

	#return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
	return todo_list(1)

@route('/edit/<no:int>', method='GET')
def edit_item(no):
	if request.GET.get('save','').strip():
		edit = request.GET.get('task','').strip()
		status = request.GET.get('status','').strip()

		if status == 'open':
			status = 1
		else:
			status = 0

		conn = sqlite3.connect(HOME+'todo.db')
		c = conn.cursor()
		c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
		conn.commit()

		return '<p>The item number %s was successfully updated</p>' % no
	else:
		conn = sqlite3.connect(HOME+'todo.db')
		c = conn.cursor()
		c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
		cur_data = c.fetchone()

		return template('edit_task', old=cur_data, no=no)

@route('/delete/<no:int>', method='GET')
def delete_item(no):
	conn = sqlite3.connect(HOME+'todo.db')
	c = conn.cursor()
	c.execute("DELETE FROM todo WHERE id LIKE ?", (str(no)))
	conn.commit()
	return '<p>The new task was DELETED from the database, the ID was ' + str(no) + '</p>'

@route('/')
def hello_world():
	output = template('index')
	return output

@route('/<filename:path>')
def server_static(filename):
	return static_file(filename, root='static/')

@get('/login') # or @route('/login')
def login():
	return '''
		<form action="/login" method="post">
			Username: <input name="username" type="text" />
			Password: <input name="password" type="password" />
			<input value="Login" type="submit" />
		</form>
	'''

def check_login(username, password):
	if username == "greg" and password == "database":
		return True
	return False

@post('/login') # or @route('/login', method='POST')
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	print (username)
	print (password)
	if check_login(username, password):
		return "<p>Your login information was correct.</p>"
	else:
		return "<p>Login failed.</p>"

if __name__ == "__main__":
    run(reloader = True, host="0.0.0.0")
else:
    application = default_app()
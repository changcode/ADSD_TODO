from bottle import default_app, route, get, post, request, template

import sqlite3

HOME = "/home/ChangCode/mysite/"

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
	return '''
		<p>Enter a new item...</p><br/>
		<form action="/new" method="post">
			To be done: <input name="task" type="text" />
			<input value="Save" type="submit" />
		</form>
	'''

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

@route('/')
def hello_world():
    return 'Hello there from this very nice Bottle page! :-)'

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

application = default_app()


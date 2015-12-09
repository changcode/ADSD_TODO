from bottle import default_app, run, route, get, post, request, template, static_file

import sqlite3
if __name__ == "__main__":
    HOME = "./"
else:
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
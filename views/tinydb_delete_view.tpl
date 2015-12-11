<p>Delete the task with ID = {{id}}</p>
<form action="/tinydb/delete/{{id}}" method="post">
Task to delete:
<hr/>
<br/>
<strong>{{task}}</strong>
<br/>
<hr/>
<input type="submit" name="confirm" value="Confirm deletion..." />
</form>

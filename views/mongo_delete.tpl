<p>Delete the task with ID = {{id}}</p>
<form action="/mongodb/delete/{{id}}" method="post">
Task to delete:
<hr/>
<br/>
<strong>{{task}}</strong>
<br/>
<hr/>
<input type="submit" name="confirm" value="Confirm deletion..." />
</form>

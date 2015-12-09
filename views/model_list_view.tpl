<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="../../favicon.ico">

        <title>ADSD To-Do List</title>

        <!-- Bootstrap core CSS -->
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
        <!-- Bootstrap theme -->
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" rel="stylesheet">
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <link href="../../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

        <!-- Custom styles for this template -->
        <link href="/theme.css" rel="stylesheet">

        <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
        <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
        <script src="../../assets/js/ie-emulation-modes-warning.js"></script>

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <!-- Fixed navbar -->
        <nav class="navbar navbar-inverse navbar-fixed-top">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">ToDo List</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
                <li><a href="/todo">ToDo List</a></li>
                <li class="active"><a href="/model">Model(PeeWee)</a></li>
                <li><a href="/tinydb">TinyDB</a></li>
                <li><a href="/mongodb">MongoDB</a></li>
                <li><a href="/mapreduce">MapReduce</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div>
        </nav>

        <div class="container">
            <div class="page-header">
                <h1>Model List View</h1>
                <h2>The open items are as follows(Model List):</h2>
            </div>
            <p>The open items are as follows:</p>
            <div class="col-md">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>Seq</th>
                            <th>Description</th>
                            <th>Marker</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    %for row in rows:
                        <tr>
                            <td><a href="/edit/{{row[0]}}">{{row[0]}}</a></td>
                            <td><a href="/edit/{{row[0]}}">{{row[1]}}</a></td>
                            <td><a href="/edit/{{row[0]}}">{{row[2]}}</a></td>
                            <td><a href="delete/{{row[0]}}"><img src="/trash.png" style="width:16px;height:16px;border:0;"/></a></td>
                        </tr>
                    %end
                </table>
            </div>
        <hr/>
        <p>Enter a new item...</p><br/>
        <form action="/new" method="post">
            To be done: <input name="task" type="text" />
            <input value="Save new item..." type="submit" />
        </form>
    </body>
</html>
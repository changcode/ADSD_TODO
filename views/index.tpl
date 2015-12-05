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

  <body role="document">

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
            <li class="active"><a href="/">Home</a></li>
            <li><a href="/todo">ToDo List</a></li>
            <li><a href="#contact">Contact</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container theme-showcase" role="main">

      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class="jumbotron">
        <h1>ADSD ToDo List</h1>
        <p>This to do list is driven by Bottlepy and Bootstrap, for ADSD class</p>
      </div>

      <div class="page-header">
        <h1>Tables</h1>
      </div>
      <div class="row">
        <div class="col-md-6">
          <table class="table">
            <thead>
              <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
              </tr>
              <tr>
                <td>3</td>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col-md-6">
          <table class="table table-striped">
            <thead>
              <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
              </tr>
              <tr>
                <td>3</td>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="row">
        <div class="col-md-6">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="2">1</td>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
              </tr>
              <tr>
                <td>Mark</td>
                <td>Otto</td>
                <td>@TwBootstrap</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
              </tr>
              <tr>
                <td>3</td>
                <td colspan="2">Larry the Bird</td>
                <td>@twitter</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col-md-6">
          <table class="table table-condensed">
            <thead>
              <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
              </tr>
              <tr>
                <td>3</td>
                <td colspan="2">Larry the Bird</td>
                <td>@twitter</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="page-header">
        <h1>List groups</h1>
      </div>
      <div class="row">
        <div class="col-sm-4">
          <ul class="list-group">
            <li class="list-group-item">Cras justo odio</li>
            <li class="list-group-item">Dapibus ac facilisis in</li>
            <li class="list-group-item">Morbi leo risus</li>
            <li class="list-group-item">Porta ac consectetur ac</li>
            <li class="list-group-item">Vestibulum at eros</li>
          </ul>
        </div><!-- /.col-sm-4 -->
        <div class="col-sm-4">
          <div class="list-group">
            <a href="#" class="list-group-item active">
              Cras justo odio
            </a>
            <a href="#" class="list-group-item">Dapibus ac facilisis in</a>
            <a href="#" class="list-group-item">Morbi leo risus</a>
            <a href="#" class="list-group-item">Porta ac consectetur ac</a>
            <a href="#" class="list-group-item">Vestibulum at eros</a>
          </div>
        </div><!-- /.col-sm-4 -->
        <div class="col-sm-4">
          <div class="list-group">
            <a href="#" class="list-group-item active">
              <h4 class="list-group-item-heading">List group item heading</h4>
              <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
            </a>
            <a href="#" class="list-group-item">
              <h4 class="list-group-item-heading">List group item heading</h4>
              <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
            </a>
            <a href="#" class="list-group-item">
              <h4 class="list-group-item-heading">List group item heading</h4>
              <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
            </a>
          </div>
        </div><!-- /.col-sm-4 -->
      </div>

    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script src="../../assets/js/docs.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

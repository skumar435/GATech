@extends('layout')
@section('content')
	<!DOCTYPE HTML>
	<html>
	<style>
	.button {
	background-color: #4CAF50;
	border: 3px solid #228B22;
	color: white;
	padding: 15px 32px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 4px 2px;
	cursor: pointer;
	}
	.button:hover {
   background-color: yellow;
	 color: black;
 }
 .button:active {
  background-color: yellow;
	color: black;

}
	.button2 {
	background-color: #4CAF50;
	border: 3px solid #228B22;
	color: white;
	padding: 15px 32px;
	text-align: center;
	text-decoration: none;
	display: inline-block;
	font-size: 16px;
	margin: 4px 2px;
	cursor: pointer;
	}

	</style>
		<head>
			<title>Pipeline</title>
			<script src="js/jquery.min.js"></script>
			<script src="js/jquery.scrolly.min.js"></script>
			<script src="js/skel.min.js"></script>
			<script src="js/init.js"></script>
			<noscript>
				<link rel="stylesheet" href="css/skel.css" />
				<link rel="stylesheet" href="css/style.css" />
				<link rel="stylesheet" href="css/style-wide.css" />
			</noscript>
		</head>
		<body>
			<br><br>
			<!-- First -->
				<section id="first" class="main">

	<!-- Second -->
					<section id="second" class="main">
				<div>
						<div id = "initial" class="content">
							<br>
								<form method="POST" action="#">
										<h1> Select Stage to Execute</h1>
										<a href='assemble' class="button">Genome Assembly</a>
										<a href='gene-pred' class="button">Gene Prediction + Functional Annotation</a>
										<!-- <a href='#' class="button"></a> -->
										<a href='comp-geno' class="button">Comparative Genomics</a>
										<br>
								</form>
								<!-- <button onclick="myFunction()">Batch Mode</button> -->
								<!-- <form action="">
	  <input type="radio" name="gender" value="male"> Male<br>
	  <input type="radio" name="gender" value="female"> Female<br>
	  <input type="radio" name="gender" value="other"> Other
	</form> -->

								<script>
								function myFunction() {
								  var x = document.getElementById("final");
								  if (x.style.display === "none") {
								    x.style.display = "block";
								  } else {
								    x.style.display = "none";
								  }
								}
								function myFunction1() {
								  var x = document.getElementById("upload");
								  if (x.style.display === "none") {
								    x.style.display = "block";
								  } else {
								    x.style.display = "none";
								  }
								}
								</script>
							</div>
								<div id = "final" class="content" style="display: none;">
								<br>
								<form method="POST" action="#">
										<h1> Select Stage to End</h1>
										<a id = "test" onclick="myFunction1()" href='#' class="button">Gene Prediction</a>
										<a href='#' class="button">Functional Annotation</a>
										<a href='#' class="button">Comparative Genomics</a>
										<br>
								</form>
								<br>
						</div>
				</div>
				<br><br>


				<div id="upload" class="container"  style="display: none;">
				    <div class="panel panel-primary">
				      <!-- <div class="panel-heading"><h2>Gene Prediction</h2></div> -->
				      <div class="panel-body">
				        @if ($message = Session::get('success'))
				        <div class="alert alert-success alert-block">
				                <strong>{{ $message }}</strong>
				        </div>
				        @endif
				        @if (count($errors) > 0)
				            <div class="alert alert-danger">
				                <strong>Whoops!</strong> There were some problems with your input.
				                <ul>
				                    @foreach ($errors->all() as $error)
				                        <li>{{ $error }}</li>
				                    @endforeach
				                </ul>
				            </div>
				        @endif
				      </div>
				    </div>
				</div>

				<!-- <div id = "submit"class="form-group">
					   <button style="cursor:pointer align:center" type="submit" class="button2">Submit</button>
				</div> -->

		</body>
	</html>
@endsection

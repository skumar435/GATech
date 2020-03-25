<!DOCTYPE HTML>
<html>
<style>
html, body {
		background-color: #fff;
		color: #636b6f;
		font-family: 'Raleway', sans-serif;
		font-weight: 100;
		height: 100vh;
		margin: 0;
}
		.full-height {
				height: 100vh;
		}

		.flex-center {
				align-items: center;
				display: flex;
				justify-content: center;
		}

		.position-ref {
				position: relative;
		}

		.top-right {
				position: absolute;
				right: 10px;
				top: 18px;
		}

		.content {
				text-align: center;
		}

		.title {
				font-size: 84px;
		}

		.links > a {
				color: #636b6f;
				padding: 0 25px;
				font-size: 12px;
				font-weight: 600;
				letter-spacing: .1rem;
				text-decoration: none;
				text-transform: uppercase;
		}

		.m-b-md {
				margin-bottom: 30px;
		}
.button {
background-color: #4CAF50;
border: none;
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
		<title>Salmonella Enterica Predictive Web-server</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
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

		<!-- Header -->
			<section id="header" class="dark">
				<div class="container">
				<header>
					<h1>Welcome to the Salmonella Enterica Predictive Web-server</h1>
					<p>Created by Team-2 Web-server Group</p>
				</header>
				<footer>
					<a href="#first" class="button scrolly">Proceed to View Available Pipelines</a>
				</footer>
			</div>
			</section>

		<!-- First -->
			<section id="first" class="main">

				<header>
					<div class="container">
						<h2>Pipelines Available</h2>
						<p>The following pipelines are available to run:<br/></p>
						<p>"Add some information about our pipelines here"</p>
					</div>
				</header>


				<div class="content dark style1 featured">
					<div class="container">
						<div class="row">
							<div class="12u">
								<footer>
									<a href="#second" class="button scrolly">Proceed to Selection</a>
								</footer>
							</div>
						</div>
					</div>
				</div>
			</section>

<!-- Second -->
				<section id="second" class="main">
			<div>
					<div class="content">
						<br>
							<form method="POST" action="{{ config('app.url')}}/salmonella">
									<h1> Select Stage to Start</h1>
									<a href='#' class="button">Genome Assembly</a>
									<a href='#' class="button">Genome Prediction</a>
									<a href='#' class="button">Functional Annotation</a>
									<a href='#' class="button">Comparative Genomics</a>
									<br>
							</form>
							<br>
							<form method="POST" action="{{ config('app.url')}}/salmonella">
									<h1> Select Stage to End</h1>
									<a href='#' class="button">Genome Assembly</a>
									<a href='#' class="button">Genome Prediction</a>
									<a href='#' class="button">Functional Annotation</a>
									<a href='#' class="button">Comparative Genomics</a>
									<br>
							</form>
							<br>
					</div>
			</div>

			<div class="content dark style1 featured">
				<div class="container">
					<div class="row">
						<div class="12u">
							<footer>
							</footer>
						</div>
					</div>
				</div>
			</div>

		</selection>
		<!-- Footer -->
			<section id="footer">
				<ul class="icons">
					<li><a href="https://github.gatech.edu/compgenomics2019/Team2-WebServer" class="icon fa-github"><span class="label">GitHub</span></a></li>
				</ul>

				<div class="copyright">
					<ul class="menu">
						<li>&copy; April 2019 Team-2 Web-Server Group</li>
					</ul>
				</div>
			</section>

	</body>
</html>

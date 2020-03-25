<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>

        <!-- Styles -->
        <style>
		html, body {
			background-color: white;
			color: #636b6f;
			font-family: 'Nunito', sans-serif;
			font-weight: 20;
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

		.top-left {
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
			font-size: 13px;
			font-weight: 600;
			letter-spacing: .1rem;
			text-decoration: none;
			text-transform: uppercase;
		}

		.m-b-md {
			margin-bottom: 30px;
		}
        </style>

    </head>
    <body>
		<div class="top-right links">

			<a href="/">Home</a>
			<a href="/index">Pipelines</a>
			<a href="https://github.gatech.edu/compgenomics2019/Team2-WebServer">GitHub</a>
		</div>
	@yield('content')
    </body>
</html>

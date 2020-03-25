@extends('layout')

<!DOCTYPE html>

<html>

<head>

    <title>Comparative Genomics</title>

    <link rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.css">

</head>



<body>

<div class="container">



    <div class="panel panel-primary">

      <div class="panel-heading"><h2>Comparative Genomics</h2></div>

      <div class="panel-body">

		  <p> Comparative genomics can help identify outbreak vs sporadic strains. <br>
		  Assessment of functional & structural similarities and differences between <br>
		  isolates can also be accomplished. </p>

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

        <form action="#" method="get" target="_blank">
          E-mail: <input type="text" name="email"><br><br>
        </form>

        <form action="{{ route('fasta.upload.post', 2) }}" method="POST" enctype="multipart/form-data">

            @csrf

            <div class="row">



                <div class="col-md-6">

                    <input type="file" name="fasta" class="form-control">

                </div>



                <div class="col-md-6">

                    <button type="submit" class="btn btn-success">Start comparing</button>

                </div>



            </div>

        </form>



      </div>

    </div>

</div>

</body>



</html>

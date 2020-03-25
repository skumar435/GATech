@extends('layout')

<!DOCTYPE html>

<html>

<head>

    <title>Gene Prediction & Functional Annotation</title>

    <link rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.css">
	<style>

	</style>
</head>

<body>

<div class="container">



    <div class="panel panel-primary">

      <div class="panel-heading"><h2>Gene Prediction & Functional Annotation</h2></div>

      <div class="panel-body">
		  <p> Gene prediction is one of the first and most important steps in understanding <br>
		    the genome of a species once it has been sequenced. Gene prediction takes in <br>
		    a contig and identifies regions of genomic DNA that encode genes. </p>
			<p> Functional annotation collects information and describes biological identity. <br>
			  Biological roles of genomic features are identified and can be used to draw biological inferences.<br>
			  Thus, biochemical function, biological function, regulation, and expression can <br>
			  be investigated with respect to genomic features.</p>


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
          <!-- <input type="submit" value="Submit" href="{{route('mail.send')}}"> -->
        </form>

        <form action="{{ route('fasta.upload.post', 1) }}" method="POST" enctype="multipart/form-data">

            @csrf

            <div class="row">



                <div class="col-md-6">
					<br>
                    <input type="file" name="fasta" class="form-control">

                </div>



                <div class="col-md-6">
					<br>
                    <button type="submit" class="btn btn-success">Start Predicting</button>

                </div>



            </div>

        </form>



      </div>

    </div>

</div>

</body>



</html>

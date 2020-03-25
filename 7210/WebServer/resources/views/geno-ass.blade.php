@extends('layout')

<!DOCTYPE html>

<html>

<head>

    <title>Genome Assembly</title>

    <link rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.css">
	<style>
	html, body {
    width  : 100%;
    height : 100%;
	}
	#overlay-back {
	    position   : absolute;
	    top        : 0;
	    left       : 0;
	    width      : 100%;
	    height     : 100%;
	    background : #000;
	    opacity    : 0.6;
	    filter     : alpha(opacity=60);
	    z-index    : 5;
	    display    : none;
	}
	#overlay {
	    position : absolute;
	    top      : 0;
	    left     : 0;
	    width    : 100%;
	    height   : 100%;
	    z-index  : 10;
	    display  : none;
	}
	</style>
</head>



<body>

<div class="container">



    <div class="panel panel-primary">

      <div class="panel-heading"><h2>Genome Assembly</h2></div>

      <div class="panel-body">
		  <p> The goal of a sequence assembler is to produce long contiguous pieces of
		  <br> sequence (contigs) from these reads. The contigs are ordered <br>
		    and oriented in relation to one another to form scaffolds. The distances <br>
		    between a set of paired end reads is useful information for this purpose.</p>


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



        <form action="{{ route('fasta.upload.post', 3) }}" method="POST" enctype="multipart/form-data">

            @csrf

            <div class="row">



                <div class="col-md-6">

                    <input type="file" name="fasta" class="form-control">

                </div>

                <div class="col-md-6">

                    <input type="file" name="fasta" class="form-control">

                </div>

                <div class="col-md-6">
<br>
                    <button type="submit" class="btn btn-success">Upload</button>

                </div>

            </div>

        </form>



      </div>

    </div>

</div>

</body>



</html>

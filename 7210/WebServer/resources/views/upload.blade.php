@extends('layout')
@section('content')
	<html>
	<head>
	<title>Upload Files</title>
	</head>
	<h1> Upload Files </h1>
	<div class="form-group">
            <label for="email">Enter Email:</label>
            <input type="email" class="form-control" id="email" name="email">
    </div>

	<p>Upload File</p>
	<form action=""{{ route('image.upload.post') }}"" method="post" enctype="multipart/form-data" action="/upload" onsubmit="return checkform(this);">
			<input type="file" name="fileToUpload" id="fileToUpload">
			<input type="submit" value="Upload" align='right' name="submit"><br><br>
	<div class="form-group">
		   <button style="cursor:pointer" type="submit" class="btn btn-primary">Submit</button>
	</div>
</html>
@endsection

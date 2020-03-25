<!doctype html>
<html lang="en">
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="csrf-token" content="{{ csrf_token() }}">
  <title>Laravel 5.8 Google Recatpcha Verification - Tutsmake.com</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" />
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.0/jquery.validate.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.0/additional-methods.min.js"></script>
  <style>
   .error{ color:red; }
  </style>
</head>

<body>

<div class="container">
    <h2 style="margin-top: 10px;" class="text-center">Laravel 5.8 Google Recatpcha Verification - <a href="https://www.tutsmake.com" target="_blank">TutsMake</a></h2>
    <br><br><br>
    <div class="row justify-content-center">
    <div class="col-md-8">
    <a href="https://www.tutsmake.com/laravel-5-8-v2-google-recaptcha-integration" class="btn btn-secondary">Back to Post</a>
    <br><br>

    @if ($message = Session::get('success'))
    <div class="alert alert-success alert-block">
        <button type="button" class="close" data-dismiss="alert">×</button>
          <strong>{{ $message }}</strong>
    </div>
    <br>
    @endif

    <form id="captcha-form" method="post" action="{{url('store-captcha-form')}}">
      @csrf
      <div class="form-group">
        <label for="formGroupExampleInput">Name</label>
        <input type="text" name="name" class="form-control" id="formGroupExampleInput" placeholder="Please enter name">
        <span class="text-danger">{{ $errors->first('name') }}</span>
      </div>
      <div class="form-group">
        <label for="email">Email Id</label>
        <input type="text" name="email" class="form-control" id="email" placeholder="Please enter email id">
        <span class="text-danger">{{ $errors->first('email') }}</span>
      </div>
      <div class="form-group">
        <label for="mobile_number">Mobile Number</label>
        <input type="text" name="mobile_number" class="form-control" id="mobile_number" placeholder="Please enter mobile number">
        <span class="text-danger">{{ $errors->first('mobile_number') }}</span>
      </div>
      <div class="form-group">
        <label for="captcha">Captcha</label>
          {!! NoCaptcha::renderJs() !!}
          {!! NoCaptcha::display() !!}
        <span class="text-danger">{{ $errors->first('g-recaptcha-response') }}</span>
      </div>
      <div class="form-group">
       <button type="submit" class="btn btn-success">Submit</button>
      </div>
    </form>
</div>
</div>
</div>

</body>
</html>

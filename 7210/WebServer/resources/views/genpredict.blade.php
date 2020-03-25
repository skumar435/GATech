
<body>

<hr>
        <style>
            html, body {
                background-color: #fff;
                color: #090a0b;
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

.button2 {
  background-color: #008CBA;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
        </style>

<center>
<h1 style="font-size:60px;">Gene Prediction</h1>
<p> Gene prediction is one of the first and most important steps in understanding <br>
  the genome of a species once it has been sequenced. Gene prediction takes in <br>
  a contig and identifies regions of genomic DNA that encode genes. </p>

    <div class="container">
        <form class="form-horizontal" method="POST" action="file/file_upload" enctype="multipart/form-data">
            <input type="hidden" name="_token" value="PsSKJjpcYWfU1AN145K1SHVJvarnLYkQc5NjS9fO">
            <div class="form-row">
                <div class="col-md-3 mb-3">
                    <label for="file">Click to upload file </label>
                    <input id="file" type="file" class="form-control" name="filename" required="">
                </div>
                <br>
                </br>


  
    <div class="container">
        <form class="form-horizontal" method="POST" action="file/downloadOrDelete" enctype="multipart/form-data">
            <input type="hidden" name="_token" value="PsSKJjpcYWfU1AN145K1SHVJvarnLYkQc5NjS9fO">
            <div class="form-row">
                <div class="col-md-3 mb-3">
                    <label for="file">Input file name</label>
                    <input type="text" class="form-control" id="newFileName" name="fileName" required="">
                </div>
      <br>
    </br>                
                <div class="col-md-2 mb-3">
                    <label>Click to upload files and begin pipeline!</label>
                    <button type="submit" class="btn btn-primary">Upload</button>
                </div>

        </form>
    <br>
    </br>

    </div>

    <br>
    </br>
                <div class="col-md-2 mb-3">
                    <label>Download files</label>
                    <button type="submit" class="btn btn-primary" name="btn" value="download">Download</button>
                </div>
        <br>
    </br>            
                <div class="col-md-1 mb-3">
                    <label>Delete file</label>
                    <button type="submit" class="btn btn-primary" name="btn" value="delete">Delete</button>
                </div>
            </div>
        </form>
    </div>

    <div class="container-fluid" style="background-color: gray; position: fixed; left: 0; bottom: 0;">
        <footer style="text-align: center;">
            <br>
            <p style="color: white;"> Team 2 Predictive Webserver Group</p>
            <br>
        </footer>
    </div>
    </center>


</body>

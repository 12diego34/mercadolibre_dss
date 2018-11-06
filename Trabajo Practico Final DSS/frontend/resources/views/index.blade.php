
<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Bare - Start Bootstrap Template</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href={{ asset("css/bootstrap.min.css") }}>
    <link rel="stylesheet" href={{ asset("css/sticky-footer.css") }}>

  </head>

  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
      <div class="container">
        <a class="navbar-brand" href="#">Start Bootstrap</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">
      <div class="row">
        <div class="col-lg-12 text-center">
          <h1 id="titulo" class="mt-5">A Bootstrap 4 Starter Template</h1>
          <p class="lead">Complete with pre-defined file paths and responsive navigation!</p>
          <div class="container">
              <div class="row">
                <!--  <form action="" method="POST" enctype="multipart/form-data">--> <!-- <form action="http://127.0.0.1:5000/prediccion" method="post" enctype=multipart/form-data> -->
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="margin-bottom:5px;">
                        <div class="panel-heading">
                                <div style="text-align:center;">
                                  <div class="form-group">
                                    <label for="images">File input</label>
                                    <input type="file" id="filechooser" name="images" accept="image/*">
                                    <p class="help-block">Select Images to Upload.</p>
                                    <img id="imagen"  width="300px"/> 
                                    <br>
                                    <br>
                                    <!-- <input type="submit" value="Predecir" class="btn btn-success"> -->
                                    <input type="button" value="Predecir" class="btn btn-success" onclick="myFunction()">
                                  </div>
                                </div>
                        </div>
                </div>

                    
                <!--  </form> -->
              </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    
    <footer class="footer">
      <div class="container">
        <span class="text-muted">Place sticky footer content here.</span>
      </div>
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src={{ asset("js/jquery-3.3.1.min.js") }}></script>
    <script src={{ asset("js/popper.min.js") }}></script>
    <script src={{ asset("js/bootstrap.min.js") }}></script>
    <script src={{ asset("js/app.js") }}></script>
    <script>
          
          var reader = "";
          var entrada = ""
          function readURL(input) {
              if (input.files && input.files[0]) {
                  reader = new FileReader();
                  entrada = input
                  reader.onload = function (e) {
                      $('#imagen').attr('src', e.target.result);
                  }

                  reader.readAsDataURL(input.files[0]);
              }
          }

          $("#filechooser").change(function(){
              readURL(this);
          });

          function myFunction(){
              console.log("hiciste click");
              


              var imagen = reader.readAsDataURL(entrada.files[0]);
              console.log("imagen")
              var formData = new FormData();
              formData.append("inputImagen", imagen);
              //formData.append("fileToUpload", ['te envio esta']);

              $.ajax({
                url: "http://127.0.0.1:5000/prediccion",
                type: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    // .. do something
                    console.log(response)
                },
                error: function(jqXHR, textStatus, errorMessage) {
                    console.log(errorMessage); // Optional
                }
              });
            
          }
    </script>
  </body>

</html>


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
    <div class="content">
    <div class="container">
      <div class="row">
        <div class="col-lg-12 text-center">
          <h1 id="titulo" class="mt-5">A Bootstrap 4 Starter Template</h1>
          <p class="lead">Complete with pre-defined file paths and responsive navigation!</p>
          <div class="container">
              <div class="row">
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
              <div class="row">
                  <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="margin-bottom:5px;">
                        <div class="panel-heading">
                            <div style="text-align:center;">
                                  <div class="table-responsive">
                                      <table id="tabla" class="table table-sm">
                                          <thead>
                                              <tr>
                                                <th scope="col">Modelo</th>
                                                <th scope="col">Resultado</th>
                                              </tr>
                                          </thead>
                                          <tbody>
                                              

                                          </tbody>
                                        </table>
                                  </div> 
                            </div>
                        </div>
                  </div>
              </div>
          </div>
        </div>
      </div>
    </div> <!--container-->
    </div><!--content-->


                          


            
    <!-- Footer -->
    <!-- https://css-tricks.com/couple-takes-sticky-footer/ -->
    <br>
    <br>
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


          





function myFunction()
{
  $("#tabla > tbody").html("");


  //var url = "url/action";                
  var url = "url/action";                
  var image = $('#imagen').attr('src');

  //Inicio Prueba
  var block = image.split(";");
  var contentType = block[0].split(":")[1];
  var realData = block[1].split(",")[1];
  

  //Fin Prueba

  //var base64ImageContent = image.replace(/^data:image\/(png|jpg);base64,/, "");
  //var blob = base64ToBlob(base64ImageContent, 'image/png');                
  var formData = new FormData();
  formData.append('picture', realData);

  $.ajax({
      url: "http://127.0.0.1:5000/prediccion",
      type: "POST", 
      cache: false,
      contentType: false,
      processData: false,
      success: function(response) {
                      // .. do something
                      console.log(response['result'])
                      console.log(response['result'][0]['nombre_modelo'])
                      console.log(response['result'][0]['label'])
                      console.log(response['result'].length)

                      for(var i=0;i<response['result'].length;i++){
                         var fila = "<tr><td>" + response['result'][i]['nombre_modelo'] + "</td><td>" + response['result'][i]['label'] +"</td></tr>";
                         $("#tabla").append(fila);
                      }
                      

                       
                          
                        
                       
                  },
      data: formData})
          .done(function(e){
              alert('done!');
          });
  }


          


    </script>
  </body>

</html>

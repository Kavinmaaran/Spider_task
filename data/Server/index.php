<?php
include '../load.php';
function form($name, $dept, $email, $rollno)
{
    $servername = "db";
    $username = "root";
    $password = "example";
    $dbname = "form";
    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    $sql ="INSERT INTO `form_details` (`name`, `dept`, `email`, `rollno`)
    VALUES ('$name', '$dept', '$email', '$rollno');";
    $error=false;
    try {
      if ($conn->query($sql) === true) {
        $error=false;
    } else {
        $error=$conn->connect_error;
    }
        $conn->close();
        return $error;
    }
    catch(Exception $e) {
      $error = true;
      return $error;
      echo 'Message: ' .$e->getMessage();
    }
}
$form=false;

if (isset($_POST['name']) and isset($_POST['dept']) and isset($_POST['email']) and isset($_POST['rollno'])) {
    $name=$_POST['name'];
    $dept=$_POST['dept'];
    $email=$_POST['email'];
    $rollno=$_POST['rollno'];
    $form=true;
    $error=form($name, $dept, $email, $rollno);
    echo $error;
}
if ($form) {
    if (!$error) {
        header("Location: http://ecorpcredit/success.php", true, 301);
        exit();
    } 
    else{
        header("Location: http://ecorpcredit", true, 301);
        echo "TRY AGAIN";
        exit();
    }
    }else {?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

    <title>Form</title>
  </head>
  <body class="bg-light">
    
    <div class="container">
      <main>
        <div class="py-5 text-center">
          <h2>Form</h2>
        </div>
          <div class="col-md-7 col-lg-8 container">
            <h4 class="mb-3">Information Collection Forms</h4>
            <form action="/index.php" method="post">
              <div class="row g-3">
                <div class="col-sm-6">
                  <label for="Name" class="form-label">Name</label>
                  <input name="name" type="text" class="form-control" id="Name" placeholder="">
                </div>
    
                <div class="col-sm-6">
                  <label for="dept" class="form-label">Department</label>
                  <input name="dept" type="text" class="form-control" id="dept" placeholder="">
                </div>
    
                <div class="col-12">
                  <label for="email" class="form-label">Email</label>
                  <input name="email" type="email" class="form-control" id="email" placeholder="you@example.com">
                  <div class="invalid-feedback">
                </div>
    
                <div class="col-12">
                  <label for="rollno" class="form-label">Roll No.</label>
                  <input name="rollno" type="text" class="form-control" id="rollno" placeholder="Please enter your Roll No." >
                </div>
    
              <hr class="my-4">
    
              <button class="w-100 btn btn-primary btn-lg" type="submit">Submit</button>
            </form>
          </div>
        </div>
      </main>
    
      <footer class="my-5 pt-5 text-muted text-center text-small">
      </footer>
    </div>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
  </body>
</html>
<?php }?>
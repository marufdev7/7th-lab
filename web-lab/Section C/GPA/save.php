<?php

$conn = mysqli_connect("localhost","root","","studentdb");

$tableCreateQuery = "CREATE TABLE IF NOT EXISTS result (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll VARCHAR(50) NOT NULL,
    marks INT,
    gpa FLOAT
)";

mysqli_query($conn, $tableCreateQuery);

$name = $_POST['name'];
$roll = $_POST['roll'];
$marks = $_POST['marks'];

/* GPA Calculation */

if($marks >= 80)
    $gpa = 4.00;
elseif($marks >= 70)
    $gpa = 3.50;
elseif($marks >= 60)
    $gpa = 3.00;
elseif($marks >= 50)
    $gpa = 2.50;
elseif($marks >= 40)
    $gpa = 2.00;
else
    $gpa = 0.00;

/* Insert into Database */

$sql = "INSERT INTO result(name,roll,marks,gpa)
VALUES('$name','$roll','$marks','$gpa')";

mysqli_query($conn,$sql);

header("Location: display.php");

?>
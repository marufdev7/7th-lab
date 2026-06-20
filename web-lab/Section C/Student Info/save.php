<?php

$conn = mysqli_connect("localhost","root","","studentdb");

$name = $_POST['name'];
$email = $_POST['email'];
$password = $_POST['password'];
$address = $_POST['address'];
$gender = $_POST['gender'];
$skills = implode(",", $_POST['skills']);
$department = $_POST['department'];

// Create Database
$tableCreateQuery = "CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    address TEXT,
    gender ENUM('Male', 'Female', 'Other'),
    skills TEXT,
    department VARCHAR(100)
)";

mysqli_query($conn, $tableCreateQuery);

$sql = "INSERT INTO students
(name,email,password,address,gender,skills,department)
VALUES
('$name','$email','$password','$address','$gender','$skills','$department')";

mysqli_query($conn,$sql);

header("Location: display.php");
exit();

?>
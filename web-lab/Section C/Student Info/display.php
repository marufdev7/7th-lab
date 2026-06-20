<?php

$conn = mysqli_connect("localhost","root","","studentdb");

$result = mysqli_query($conn,"SELECT * FROM students");

echo "<h2>Stored Information</h2>";

echo "<table border='1'>
<tr>
<th>ID</th>
<th>Name</th>
<th>Email</th>
<th>Password</th>
<th>Address</th>
<th>Gender</th>
<th>Skills</th>
<th>Department</th>
</tr>";

while($row = mysqli_fetch_assoc($result))
{
    echo "<tr>";
    echo "<td>".$row['id']."</td>";
    echo "<td>".$row['name']."</td>";
    echo "<td>".$row['email']."</td>";
    echo "<td>".$row['password']."</td>";
    echo "<td>".$row['address']."</td>";
    echo "<td>".$row['gender']."</td>";
    echo "<td>".$row['skills']."</td>";
    echo "<td>".$row['department']."</td>";
    echo "</tr>";
}

echo "</table>";

?>
<?php

$conn = mysqli_connect("localhost","root","","studentdb");

$result = mysqli_query($conn,"SELECT * FROM result");

echo "<h2>Student Result</h2>";

echo "<table border='1'>
<tr>
<th>Name</th>
<th>Roll</th>
<th>Marks</th>
<th>GPA</th>
</tr>";

while($row = mysqli_fetch_assoc($result))
{
    echo "<tr>";
    echo "<td>".$row['name']."</td>";
    echo "<td>".$row['roll']."</td>";
    echo "<td>".$row['marks']."</td>";
    echo "<td>".$row['gpa']."</td>";
    echo "</tr>";
}

echo "</table>";

?>
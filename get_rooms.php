<?php

$servername = "localhost";
$username = "root";
$password = "59BwheAFCi5Z";
$dbname = "witsofteng";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = sprintf('SELECT * FROM Rooms WHERE id = $_POST['RoomID']');

$result = $conn->query($sql)

if ($result === TRUE) {
    while($row = $result->fetch_assoc()) {
		echo $row;
	}
} else {
   // echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();


?>
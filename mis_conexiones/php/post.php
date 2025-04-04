<?php
$host = "localhost";
$dbname = "postgres";
$user = "postgres";
$password = "12345";

$conn = pg_connect("host=$host dbname=$dbname user=$user password=$password");

if (!$conn) {
    echo "Error: No se pudo conectar a la base de datos.";
    exit;
}

$result = pg_query($conn, "SELECT * FROM tabla");

while ($row = pg_fetch_assoc($result)) {
    echo "id: " . $row['id'] . " - Nombre: " . $row['nombre'] . "<br>";
}

pg_close($conn);
?>

<?php
require 'vendor/autoload.php';

$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->tienda->usuario;

$documents = $collection->find();

foreach ($documents as $doc) {
    print_r($doc);
}
?>

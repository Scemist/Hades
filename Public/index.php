<?php

ini_set("display_errors", 1);
error_reporting(E_ALL);

require_once  '../vendor/autoload.php';

use App\Bootstrap;

$app = new Bootstrap();
$app->init($_SERVER['REQUEST_URI']);

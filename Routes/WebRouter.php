<?php

namespace Route;

use App\Controller\Home;

class WebRouter
{
	private static $routes = [
		''     => [Home::class, 'index'],
		'home' => [Home::class, 'index'],
	];

	public static function get(string $uri)
	{
		if ($uri[0] == '/')
			$uri = substr($uri, 1);

		if (!array_key_exists($uri, WebRouter::$routes))
			return false;

		return WebRouter::$routes[$uri];
	}
}

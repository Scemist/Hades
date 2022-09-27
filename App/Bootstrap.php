<?php

namespace App;

use Route\WebRouter;
use App\Error\LException;

class Bootstrap
{
	public function init(string $uri)
	{
		try {
			if (!$route = WebRouter::get($uri))
				return throw new LException('Página Não Encontrada', 404);

			$controller = new $route[0]();

			echo $controller->{$route[1]}();

		} catch (LException $exception) {
			$exception->abort();
		}
	}
}

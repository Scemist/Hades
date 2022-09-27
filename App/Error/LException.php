<?php

namespace App\Error;

class LException extends \Exception
{
	public function abort()
	{
		http_response_code($this->getCode());
		echo $this->getMessage();
		die;
	}
}

<?php

    $corpo = $_POST['corpo'];
    $titulo = $_POST['titulo'];

    $instancia = new arquivo();
    $instancia -> criar($corpo, $titulo);

    class arquivo {

        public $nome = 'arquivo';
        public $titulo;
        public $corpo;
        
        function criar($corpo, $titulo) {

            $this -> corpo = $corpo;
            $this -> titulo = $titulo;

            $fopen = fopen('../documentos/' . $this -> titulo . ".txt", 'wb');
            fwrite($fopen, $corpo);
            fclose($fopen);
        }
        
        function editar() {

        }

        function deletar() {

        }
    }
<?php

    $instancia = new arquivo ();
    $instancia -> criar($_POST['corpo']);

    class arquivo {

        public $nome = 'arquivo';
        public $titulo;
        public $corpo;
        
        function criar($corpo) {

            $this -> corpo = $corpo;

            $fopen = fopen("../documentos/" . $this -> nome . ".txt", 'wb');
            fwrite($fopen, $corpo);
            fclose($fopen);
        }
        
        function editar() {

        }

        function deletar() {

        }
    }
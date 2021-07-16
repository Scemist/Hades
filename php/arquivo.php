<?php

    // $corpo = $_POST['corpo'];
    // $titulo = $_POST['titulo'];

    // $instancia = new arquivo();
    // $instancia -> criar($corpo, $titulo);

    if ($_POST):

        switch ($_POST['tipo']):
            case 'criar':
                
                $instancia = new arquivo();
                $instancia -> criar($_POST['titulo']);
            break;

            case 'salvar':
                echo 'salvar';
            break;
            
            default:
                # code...
            break;
        endswitch;
    endif;

    class arquivo {

        public $nome = 'arquivo';
        public $titulo;
        public $corpo;

        function listar() {
            
            $diretorio = 'documentos/';
            $arquivos = scandir($diretorio);
            $arquivos = array_diff($arquivos, array('..', '.'));

            function pegarNome($arquivo) {

                return pathinfo($arquivo, PATHINFO_FILENAME);
            }

            return $arquivos = array_map('pegarNome', $arquivos);
        }
        
        function criar($titulo) {

            $this -> titulo = $titulo;

            $arquivo = fopen('../documentos/' . $this -> titulo . ".txt", 'wb');
            fwrite($arquivo, $this -> titulo);
            fclose($arquivo);

            echo 'Sucesso';
        }
        
        function editar() {

        }

        function deletar() {

        }
    }
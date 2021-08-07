<?php

    if ($_POST):

        switch ($_POST['tipo']):

            case 'criar':    

                $instancia = new arquivo($_POST['titulo']);
                $instancia -> criar();
            break;

            case 'pegarConteudo':

                $instancia = new arquivo($_POST['titulo']);
                $instancia -> pegarConteudo();
            break;

            case 'listar':

                $instancia = new arquivo(null);
                $instancia -> listar();
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

        function __construct($titulo) {

            $this -> titulo = $titulo;
        }

        function listar() {

            $diretorio = $_SERVER['DOCUMENT_ROOT'] . "/documentos/";
            $arquivos = scandir($diretorio);
            $arquivos = array_diff($arquivos, array('.txt', '.gitkeep', '..', '.'));

            function pegarNome($arquivo) {

                return pathinfo($arquivo, PATHINFO_FILENAME);
            }
            
            return $arquivos = array_map('pegarNome', $arquivos);
        }
        
        function criar() {

            $arquivo = fopen('../documentos/' . $this -> titulo . ".txt", 'wb');
            // fwrite($arquivo, $this -> titulo);
            fclose($arquivo);

            $instancia = new arquivo($this -> titulo);
            $arquivos = $instancia -> listar();

            $lista = json_encode($arquivos);

            echo $lista;
            return true;
        }
        
        function pegarConteudo() {

            $arquivo = '../documentos/' . $this -> titulo . '.txt';
            echo file_get_contents($arquivo);
            return true;
        }
        
        function editar() {

        }

        function deletar() {

        }
    }
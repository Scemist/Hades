<?php
    include_once 'php/arquivo.php';
?>

<!DOCTYPE html>

<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/root.css">
        <link rel="stylesheet" href="css/nav.css">
        <link rel="stylesheet" href="css/main.css">

        <title>HADES</title>
    </head>

    <body>
        <nav>
            <h1 id="hades">Hades_</h1>        

            <div class="menu">
                <div class="barra"></div>
                <div class="barra"></div>
                <div class="barra"></div>
            </div>

            <div id="pass">
                <div class="input-grupo">
                    <label>Passphrase 1</label>
                    <input class="caixa" type="password">
                </div>
                
                <div class="input-grupo">
                    <label>Passphrase 2</label>
                    <input class="caixa" type="password" name="passphrase2">
                </div>
                
                <input id="requisicao" type="submit" value="ATUALIZAR">
            </div>
        </nav>

        <main>
            <header class="card card-head">
                <h3 id="dark">Assim falou Zaratustra</h3>
            </header>

            <section id="inicio">
                <div class="card">
                    <div>
                        <h3 class="cabecalho">Documentos_</h3>

                        <?php
                            $instancia = new arquivo();
                            $arquivos = $instancia -> listar();
                            
                            foreach ($arquivos as $arquivo):
                        ?>

                        <button class="lista">
                            <?= $arquivo ?>
                        </button>

                        <?php endforeach; ?>
                    </div>
                </div>

                <div class="card card-foot">
                    <!-- <form action="php/arquivo.php" method="POST"> -->
                        <input type="hidden" name="tipo" value="criar">

                        <input type="text" id="titulo" class="botao" name="titulo" placeholder="Título do Arquivo...">

                        <input id="criar" class="botao" type="submit" value="NOVO ARQUIVO">
                    <!-- </form> -->
                </div>
            </section>
            
            <section id="texto" class="aparente">
                <form action="php/arquivo.php" method="POST">
                    <div class="card">
                        <input type="hidden" name="corpo" id="corpo">

                        <p contenteditable="true" id="p-corpo">
                            Aquele que tem um porquê para viver pode suportar quase qualquer como.
                        </p>
                    </div>

                    <div class="card card-foot">
                        <input type="hidden" name="tipo" value="salvar">

                        <input type="text" id="novotitulo" class="botao" name="titulo" placeholder="Título do Arquivo...">

                        <input id="salvar" class="botao" type="submit" value="SALVAR">
                    </div>
                </form>
            </section>
        </main>
            
        <script src="javascript/slip.js"></script>
        <script src="javascript/app.js"></script>
    </body>
</html>
<?php
   if (isset($_POST["submit"])) {
   $name = $_POST['name'];
   $email = $_POST['email'];
   $message = $_POST['message'];
   $from = 'Informe de erros ou sugestões';
   $to_group = 'reamat@googlegroups.com'; 
   $to = 'reamat@ufrgs.br'; 
   $fromurl = $_POST["from_url"];
   $subject .= 'Aviso sobre a página: ' . $fromurl;

   $ip = $_SERVER['REMOTE_ADDR'];
   $useragent = htmlspecialchars($_SERVER['HTTP_USER_AGENT']);

   $body_group ="\nDe: $name\nRef. a URL: $fromurl\n\nMensagem:\n $message";

   $body ="Identificação:\n\nFrom: $name\nE-Mail:$email\nIP: $ip\nUser agent: $useragent\n\nInforme:\n\nRef. a URL: $fromurl\n\nMensagem:\n $message";

   //Check if message has been entered
   if (!$_POST['message']) {
   $errMessage .= "Por favor, digite sua mensagem. ";
   }

   // If there are no errors, send the email
   if (!$errMessage) {
   if ((mail ($to, $subject, $body, $from)) and (mail ($to_group, $subject, $body_group, $from))) {
   $result = '<div class="alert alert-success">Obrigado por sua colaboração! Participe diretamente da escrita deste recurso educacional. <a href="participe.html">Saiba mais aqui</a>!.</div>';
   } else {
   $result ='<div class="alert alert-danger">Desculpe, houve um erro ao enviar sua mensagem. Caso o problema persista, considere entrar em contato pelo e-mail: <a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a>.</div>';
   }
   }
   }
   ?>

<!DOCTYPE html>
<html lang="pt">
  <head>
    
    <meta charset="utf-8">
    <meta name="Description"
	  CONTENT="Recursos Educacionais Abertos de Matemática (REAMAT),
		   Instituto de Matemática e Estatística (IME), 
		   Universidade Federal do Rio Grande do Sul (UFRGS).">
    <meta name="keywords" content="recursos educacionais abertos,
				   matemática,
                                   cálculo numérico,
                                   avisar sobre erros e sugestões">
    <title>REAMAT - Avisar</title>
    <meta name="author" content="reamat@ufrgs.br">
    <link rel="shortcut icon" type="image/x-icon" href="./pics/favicon.ico" />
    <link href='http://fonts.googleapis.com/css?family=Open Sans:400,700'
	  rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="./bootstrap/css/bootstrap.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="./bootstrap/js/bootstrap.min.js"></script>
    <link href="./index.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

    <style>
      .carousel-inner .item a img {
      width: 200px;
      margin: auto;
      }
    </style>

  </head>

  <body>
    <?php $fromurl0 = $_SERVER['HTTP_REFERER']; ?>

    <!-- ********** BEGIN: ALERT ********** -->

    <div class="alert alert-danger" style="text-align:center">
      Esta página está em desenvolvimento. Para reportar erros ou dar sugestões, abra um <i>issue</i> em <a href="https://github.com/reamat/webpage" target="_blank">https://github.com/reamat/webpage</a>.
    </div>
	
    <!-- ********** END: ALERT ********** -->


    <div class="row">
      <div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2">

    <!-- ********** BEGIN: NAVBAR ********* -->
    	
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header">
	      <a class="navbar-brand" href="index.html">REAMAT<br></a>
	      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
		<span class="sr-only">Toggle navigation</span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
	      </button>
	    </div>
	    
	    <!-- Collect the nav links, forms, and other content for toggling -->
	    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	      <ul class="nav navbar-nav">
		<li><a href="index.html">Início</a></li>
		<li class="dropdown">
		  <a href="#" class="dropdown-toggle"
		     data-toggle="dropdown" 
		     role="button" aria-haspopup="true"
		     aria-expanded="false">Recursos
		    <span class="caret"></span></a>
		  <ul class="dropdown-menu">
		    <li><a href="./linear/index.html">Álgebra Linear</a></li>
		    <li><a href="./numerico/index.html">Cálculo Numérico</a></li>
		    <li><a href="./transformadas/index.html">Transformadas Integrais</a></li>
		  </ul>
		</li>		
		<li class="active"><a href="participe.html">Participar</a></li>
		<li><a href="organizadores.html">Organizadores</a></li>
	      </ul>
	    </div><!-- /.navbar-collapse -->
	  </div><!-- /.container-fluid -->
	</nav>

	<!-- ********* END: NAVBAR ******** -->
	
	<div class="titulo">
	  <div class="container-fluid">
  	    <h2 class="text-center" style="margin-bottom:0px;"> Informe de erros ou sugestões</h2>
	  </div>
	</div>

	<form class="form-horizontal" role="form" method="post" action="aviso.php">
  	  <h4 class="text-center"> Por favor, forneça seu nome e e-mail para que possamos entrar em contato.</h4>
	  <div class="form-group">
	    <label for="name" class="col-sm-2 control-label">Nome</label>
	    <div class="col-sm-10">
	      <input type="text" class="form-control" id="name" name="name" placeholder="(opcional)" value="<?php echo htmlspecialchars($_POST['name']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="email" class="col-sm-2 control-label">E-mail</label>
	    <div class="col-sm-10">
	      <input type="email" class="form-control" id="email" name="email" placeholder="(opcional)" value="<?php echo htmlspecialchars($_POST['email']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="from_url" class="col-sm-2 control-label">Ref. à página</label>
	    <div class="col-sm-10">
	      <input type="text" class="form-control" id="from_url" name="from_url" placeholder="<?php if (isset($_SERVER['HTTP_REFERER'])) { echo htmlspecialchars($_SERVER['HTTP_REFERER']);} else {echo 'Informe o link da página referente ao seu aviso';} ?>" value="<?php echo htmlspecialchars($_SERVER['HTTP_REFERER']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="message" class="col-sm-2 control-label">Mensagem*</label>
	    <div class="col-sm-10">
	      <textarea class="form-control" rows="4" name="message" placeholder="Digite seu aviso de erro ou sugestão aqui."><?php echo htmlspecialchars($_POST['message']);?></textarea>
	    <p><small>*Sua mensagem será publicada na lista de e-mails <a href="https://groups.google.com/forum/#!forum/reamat" target="blank">https://groups.google.com/forum/#!forum/reamat</a>. O endereço de e-mail informado não é publicado na lista.</small></p>
	      <?php echo "<p class='text-danger'>$errMessage</p>";?>
	    </div>
	  </div>
	  <div class="form-group">
	    <div class="col-sm-10 col-sm-offset-2">
	      <input id="submit" name="submit" type="submit" value="Enviar" class="btn btn-primary">
	    </div>
	  </div>
	  <div class="form-group">
	    <div class="col-sm-10 col-sm-offset-2">
	      <?php echo $result; ?>	
	    </div>
	  </div>
	</form> 

	<!-- ************* BEGIN: BOTTOM PANEL ********** -->

	<div class="panel panel-default">
	  <div class="container-fluid">
	    <div class="panel-body">
	      <div class="row">
		<div class="col-md-4">
		  <ul class="list-unstyled">
		    <li>Recursos
		      <ul class="list-unstyled">
			<li><a href="./linear/index.html">Álgebra Linear</a></li>
			<li><a href="./numerico/index.html">Cálculo Numérico</a></li>
			<li><a href="./transformadas/index.html">Transformadas Integrais</a></li>
			<li><a
			       href="https://github.com/reamat"
			       target="_blank">Repositórios</a></li>
		      </ul>
		    </li>
		  </ul>
		</div>		
		<div class="col-md-3">
		  <ul class="list-unstyled">
		    <li>Projeto
		      <ul class="list-unstyled">
			<li><a href="index.html">Página Inicial</a></li>
			<li><a href="participe.html">Participe</a></li>
			<li><a href="organizadores.html">Organizadores</a></li>
		      </ul>
		    </li>
		  </ul>
		</div>
		<div class="col-md-3">
		  <ul class="list-unstyled">
		    <li>IME - UFRGS
		      <ul class="list-unstyled">
			<li><a href="https://www.ufrgs.br/ime/">Página do IME</a></li>
			<li><a href="http://www.ufrgs.br">Página da UFRGS</a></li>
		      </ul>
		    </li>
		  </ul>
		</div>
	      </div>
	    </div>
	  </div>
	  <div class="panel-footer">
	    <div class="container-fluid">
	      <img src="./figs/favicon.ico" alt="UFRGS">UFRGS - IME - Recursos Educacionais Abertos de Matemática. Contato: <a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a>.
	    </div>
	  </div>
	</div>

	<!-- ************* END: BOTTOM PANEL ********** -->


  </body>
</html>

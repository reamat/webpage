<?php
   if (isset($_POST["submit"])) {
   $name = $_POST['name'];
   $email = $_POST['email'];
   $message = $_POST['message'];
   $from = 'Informe de erros ou sugestões';
   $to = 'livroscolaborativos@gmail.com'; 
   $fromurl = $_POST["from_url"];
   if ($fromurl == '') {
   $fromurl = $_SERVER['HTTP_REFERER'];
   }
   $subject .= 'Aviso sobre a página: ' . $fromurl;

   $ip = $_SERVER['REMOTE_ADDR'];
   $useragent = htmlspecialchars($_SERVER['HTTP_USER_AGENT']);

   
   $body ="Identificação:\n\nFrom: $name\nE-Mail:$email\nIP: $ip\nUser agent: $useragent\n\nInforme:\n\nRef. a URL: $fromurl\n\nMensage:\n $message";

   //Check if message has been entered
   if (!$_POST['message']) {
   $errMessage .= "Por favor, digite sua mensagem. ";
   }

   // If there are no errors, send the email
   if (!$errMessage) {
   if (mail ($to, $subject, $body, $from)) {
   $result = '<div class="alert alert-success">Obrigado por sua colaboração! Participe diretamente da escrita do livro colaborativo. <a href="participe.html">Saiba mais aqui</a>!.</div>';
   } else {
   $result ='<div class="alert alert-danger">Desculpe, houve um erro ao enviar sua mensagem. Caso o problema persista, considere entre em contato pelo e-mail: <a href="mailto:livroscolaborativos@gmail.com" target="_top">livroscolaborativos@gmail.com</a>.</div>';
   }
   }
   }
   ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Informe de erro ou sugestão para Cálculo Numérico - Um Livro Colaborativo.">
    <meta name="author" content="livroscolaborativos@gmail.com">
    <title>Informe de erros ou sugestões.</title>
    <link href='http://fonts.googleapis.com/css?family=Open Sans:400,700'
	  rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="./bootstrap-3.3.5-dist/css/bootstrap.css">
    <link href="aviso.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="./bootstrap-3.3.5-dist/js/bootstrap.min.js"></script>
  </head>
  <body>

    <div class="row">
      <div class="col-xs-12 col-xs-offset-0 col-md-8 col-md-offset-2">
	
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header">
	      <a class="navbar-brand" href="index.html">Cálculo Numérico<br><small>Um Livro Colaborativo</small></a>
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
		<li class="active"><a href="index.html">Projeto</a></li>
		<li class="dropdown">
		  <a href="#" class="dropdown-toggle" data-toggle="dropdown" 
		     role="button" aria-haspopup="true" aria-expanded="false">Livro
		    <span class="caret"></span></a>
		  <ul class="dropdown-menu">
		    <li><a href="./livro/main.html">Versão Scilab</a></li>
		    <li role="separator" class="divider"></li>
		    <li><a href="./livro-oct/main.html">Versão GNU Octave</a></li>
		    <li role="separator" class="divider"></li>
		    <li><a href="./livro-py/main.html">Versão Python</a></li>
		  </ul>
		</li>		
		<li><a href="participe.html">Participe</a></li>
		<li><a
		       href="https://github.com/livroscolaborativos/CalculoNumerico"
		       target="_blank">Repositório</a></li>
		<li><a href="organizadores.html">Organizadores</a></li>
		<li><a href="derivados.html">Trabalhos Derivados</a></li>
	      </ul>
	    </div><!-- /.navbar-collapse -->
	  </div><!-- /.container-fluid -->
	</nav>
	
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
	      <input type="text" class="form-control" id="from_url" name="from_url" placeholder="<?php if (isset($_SERVER['HTTP_REFERER'])) { echo htmlspecialchars($_SERVER['HTTP_REFERER']);} else {echo 'Informe o link da página referente ao seu aviso';} ?>" value="<?php echo htmlspecialchars($_POST['from_url']); ?>">
	    </div>
	  </div>
	  <div class="form-group">
	    <label for="message" class="col-sm-2 control-label">Mensagem</label>
	    <div class="col-sm-10">
	      <textarea class="form-control" rows="4" name="message" placeholder="Digite seu aviso de erro ou sugestão aqui."><?php echo htmlspecialchars($_POST['message']);?></textarea>
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


      <div class="panel panel-default">
	<div class="container-fluid">
	  <div class="panel-body">
	    <div class="row">
	      <div class="col-md-3">
		<ul class="list-unstyled">
		  <li>Livro
		    <ul class="list-unstyled">
		      <li><a
			     href="./livro/main.html">Versão Scilab</a></li>
		      <li><a href="./livro-oct/main.html">Versão GNU Octave</a></li>
		      <li><a href="./livro-py/main.html">Versão Python</a></li>
		      <li><a
			     href="https://github.com/livroscolaborativos/CalculoNumerico"
			     target="_blank">Repositório</a></li>
		      <li><a
			     href="https://groups.google.com/forum/#!forum/livro_colaborativo">Lista
			  de Discussão</a></li>
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
		      <li><a href="derivados.html">Trabalhos Derivados</a></li>
		    </ul>
		  </li>
		</ul>
	      </div>
	      <div class="col-md-3">
		<ul class="list-unstyled">
		  <li>IME - UFRGS
		    <ul class="list-unstyled">
		      <li><a href="http://www.ufrgs.br/mat">Página do IME</a></li>
		      <li><a href="http://www.ufrgs.br">Página da UFRGS</a></li>
		    </ul>
		  </li>
		</ul>
	      </div>
	      
	    </div>
	  </div>
	  <p style="font-size: small">* As versões do livro disponíveis no site podem estar desatualizadas, veja a 
	    <a href="https://github.com/livroscolaborativos/CalculoNumerico/blob/master/main.pdf"
	       target="_blank">versão PDF atual</a> no <a href="https://github.com/livroscolaborativos/CalculoNumerico" target="_blank">repositório GitHub oficial</a> do projeto.</p>
	</div>
	<div class="panel-footer">
	  <div class="container-fluid">
	    <img src="./favicon.ico" alt="UFRGS">UFRGS - IME - Cálculo
	    Numérico - Um Livro Colaborativo. Contato: <a href="mailto:livroscolaborativos@gmail.com" target="_top">livroscolaborativos@gmail.com</a>.
	  </div>
	</div>
      </div>


    </div>
</div>   



<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
</body>
</html>

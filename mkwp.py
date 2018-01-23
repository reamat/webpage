#!/usr/bin/python3

'''
Construção do portal reamat.

Autor: Pedro H A Konzen - UFRGS - 01/2018
'''

import sys
import os
import string
import datetime

#parameters
sdir = "."

#************************************************#
# Preliminares
#************************************************#
print("Preliminares ...")

if not(os.path.isdir(sdir+"//on_server")):
    os.system("mkdir "+sdir+"//on_server");

if not(os.path.isdir(sdir+"//on_server//bootstrap")):
    os.system("cp -rf "+sdir+"//bootstrap-3.3.7-dist "
                       +sdir+"//on_server//bootstrap")

if not(os.path.isdir(sdir+"//on_server//MathJax")):
    os.system("cp -rf "+sdir+"//MathJax-master "
                       +sdir+"//on_server//MathJax")

if not(os.path.isdir(sdir+"//on_server//fonts")):
    os.system("cp -rf "+sdir+"//fonts "
                       +sdir+"//on_server//fonts")

if not(os.path.isdir(sdir+"//on_server//figs")):
    os.system("cp -rf "+sdir+"//figs "
                       +sdir+"//on_server//figs")

os.system("cp index.css "+sdir+"//on_server//index.css")

os.system("cp aviso.php "+sdir+"//on_server//aviso.php")

#global alert
ifile = open(sdir+"//globalAlert.aux",'r')
globalAlert = ifile.read()
ifile.close()    

#list of hotsites
ifile = open(sdir+"//lisths.aux",'r')
lisths = ""
for line in ifile:
    hsname = line.split(";")
    lisths += '<li><a href="./'+hsname[0]+'/index.html">'\
           +hsname[1].strip("\n")+'</a></li>'
ifile.close()

print("Preliminares ... feito!")
    
#************************************************#
# index.html
#************************************************#
print("Construindo index.htm ...")
    
os.system("cp index.aux "+sdir+"//on_server//index.html")
ifile = open(sdir+"//on_server//index.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++","")
text = text.replace("+++keywords+++","")

#global alert
text = text.replace("+++alertaGeral+++",globalAlert)

#navbar
text = text.replace("+++navbar:inicio:active+++",'class="active"')
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:forum:active+++","")
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++","")
text = text.replace("+++listaDeHotsites+++",lisths)

#jumbotron
text = text.replace("+++jumbotron:subtitle+++",
                    "Recursos Educacionais Abertos de Matemática")

#presentation
text = text.replace("+++presentation:coluna1+++",
'\
<h3>Sobre</h3>\
<p>\
<a href="./livro/main.html"><strong>REAMAT</strong></a> \
é um projeto de escrita colaborativa de recursos \
educacionais abertos sobre tópicos de matemática \
e suas aplicações.</p>\
<p>\
Nosso objetivo é de fomentar o desenvolvimento \
de materiais didáticos pela colaboração entre \
professores e alunos de universidades, institutos de \
educação e demais interessados no estudo e \
aplicação da matemática nos mais diversos ramos da \
ciência e tecnologia.</p>\
<p>\
O sucesso do projeto depende da colaboração! Participe \
diretamenta da escrita dos recursos educacionais, dê \
sugestões ou nos avise de erros e imprecisões. Toda a \
colaboração é bem vinda. Veja como participar \
<a href="participe.html">aqui</a>.</p>\
<p>\
Nós preparamos uma série de ações para ajudá-lo a \
participar. Em primeiro lugar, o acesso irrestrito aos \
materias pode se dar através deste site. Além disso, os códigos \
fontes e a documentação dos recursos estão disponíveis em \
<a href="https://github.com/reamat" \
target="_blank">repositórios GitHub</a> públicos.</p>\
<p>\
Nada disso estaria completo sem uma licença apropriada à \
colaboração. Por isso, escolhemos disponilizar os \
materiais sob licença \
<a href="https://creativecommons.org/licenses/by-sa/3.0/" \
target="_blank"> Creative Commons \
Atribuição-CompartilhaIgual 3.0 Não Adaptada \
(<strong>CC-BY-SA 3.0</strong>) \
</a>. Ou seja, você pode <strong>copiar</strong>, \
<strong>redistribuir</strong>, \
<strong>alterar</strong> e construir um novo material para \
qualquer uso, inclusive comercial. Leia a \
<a href="https://creativecommons.org/licenses/by-sa/3.0/" \
target="_blank">licença</a> para maiores informações.</p>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3>Recursos disponíveis</h3>\
<ul class="list-unstyled"> '\
+lisths+\
'</ul>\
<h3>Repositórios GitHub</h3>\
<ul class="list-unstyled">\
  <li><a href="https://github.com/reamat">https://github.com/reamat</a></li>\
</ul>\
<h3>Contato</h3>\
<ul class="list-unstyled">\
<li><a href="mailto:reamat@ufrgs.br">reamat@ufrgs.br</a></li>\
</ul>\
')

#bottom
data = datetime.datetime.now()
text = text.replace("+++atualizadoem+++",
'<p style="text-align:right">Página gerada em ' +
str(data.day) + '/' + str(data.month) + '/' + str(data.year) +
' às ' + str(data.hour) + ':' + str(data.minute) + ':' + str(data.second) +
'.</p>'\
)

ofile = open(sdir+"//on_server//index.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo index.html ... feito!")

#************************************************#
# forum.html
#************************************************#
print("Construindo forum.htm ...")
    
os.system("cp index.aux "+sdir+"//on_server//forum.html")
ifile = open(sdir+"//on_server//forum.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Fórum")
text = text.replace("+++keywords+++",",fórum")

#global alert
text = text.replace("+++alertaGeral+++",globalAlert)

#navbar
text = text.replace("+++navbar:inicio:active+++","")
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:forum:active+++",'class="active"')
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++","")
text = text.replace("+++listaDeHotsites+++",lisths)

#jumbotron
text = text.replace("+++jumbotron:subtitle+++",
                    "Fórum")

#presentation
s = text.index('<!-- ********* BEGIN: PRESENTATION *********** -->')
e = text.rindex('<!-- ********* BEGIN: PRESENTATION *********** -->')
text = text.replace(text[s:e],
'\
<iframe id="forum_embed"\
src="javascript:void(0)"\
scrolling="no"\
frameborder="0"\
width="900"\
height="700">\
</iframe>\
<script type="text/javascript">\
document.getElementById("forum_embed").src =\
"https://groups.google.com/forum/embed/?place=forum/reamat"\
+ "&showsearch=true&showpopout=true&showtabs=false"\
+ "&parenturl=" + encodeURIComponent(window.location.href);\
</script>\
')

#bottom
data = datetime.datetime.now()
text = text.replace("+++atualizadoem+++",
'<p style="text-align:right">Página gerada em ' +
str(data.day) + '/' + str(data.month) + '/' + str(data.year) +
' às ' + str(data.hour) + ':' + str(data.minute) + ':' + str(data.second) +
'.</p>'\
)

ofile = open(sdir+"//on_server//forum.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo forum.html ... feito!")


#************************************************#
# participe.html
#************************************************#
print("Construindo participe.htm ...")
    
os.system("cp index.aux "+sdir+"//on_server//participe.html")
ifile = open(sdir+"//on_server//participe.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Participe")
text = text.replace("+++keywords+++","participe")

#global alert
text = text.replace("+++alertaGeral+++",globalAlert)

#navbar
text = text.replace("+++navbar:inicio:active+++","")
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:forum:active+++","")
text = text.replace("+++navbar:participe:active+++",'class="active"')
text = text.replace("+++navbar:organizadores:active+++","")
text = text.replace("+++listaDeHotsites+++",lisths)

#jumbotron
text = text.replace("+++jumbotron:subtitle+++",
                    "Participe")

#presentation
text = text.replace("+++presentation:coluna1+++",
'\
<h3>Participe</h3>\
<p>\
   Há várias maneiras de participar da escrita dos \
   recursos educacionais abertos de matemática. \
   Toda a colaboração é bem vinda, seja ela um aviso \
   de erro ou sugestão, uma reformulação de uma parte \
   do material, ou mesmo um novo recurso educacional.\
</p>\
<h3>Edite você mesmo</h3>\
<p>\
O código-fonte dos materiais em desenvolvimento estão \
disponíveis em repositórios GitHub públicos \
(veja <a href="https://github.com/reamat" target="blank">aqui</a>). \
Faça um <i>fork</i> do repositório para o qual deseja colaborar, \
edite e, então, faça seu <i>Pull request</i>. Em seguida, um dos organizadores \
dará encaminhamento à sua colaboração.</p>\
<h3>Fórum</h3>\
<p>Participe de nosso <a href="./fórum.html">fórum</a>, opine e ajude-nos no desenvolvimento do projeto.</p>\
<h3>Outras formas de colaboração</h3>\
<p>Toda a colaração é bem vinda! Caso tenha encontrado algum erro, imprecisão ou tenha alguma sugestão a fazer, escreva para nosso e-mail:</p>\
<p style="text-align: center;"><a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a></p>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3><span class="glyphicon glyphicon-edit"></span> Edição rápida</h3>\
<p>\
Utilize o botão <span class="glyphicon glyphicon-edit"></span> disponível nas páginas dos recursos para encaminhar edições rápidas. Ao clicar no botão, você será redirecionado ao código-fonte no GitHub do material referente à página que está consultando. Edite e registre seu <i>commit</i>. Um dos organizadores do projeto irá dar encaminhado à sua colaboração.</p>\
<h3><span class="glyphicon glyphicon-warning-sign"></span> Informe de Erros e Sugestões</h3>\
<p>\
Utilize o botão <span class="glyphicon glyphicon-warning-sign"></span> disponível nas páginas dos recursos para nos informar sobre erros ou dar sugestões. Ao clicar no botão, você será redirecionado para um formulário. Complete-o e clique no botão enviar. Pronto, seu informe será encaminhado para nosso <a  href="./forum.html">fórum</a> e um dos colaboradores poderá dar encaminhamento.</p>\
<h3>Aviso de violação de <i>copyright</i></h3>\
<p>Caso encontre qualquer violação de <i>copyright</i> em qualquer parte dos recursos disponibilizados, por favor, nos informe pelo e-mail:</p>\
<p style="text-align: center;"><a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a></p>\
<p>Iremos cuidar para analisar seu aviso o mais prontamente possível e removeremos o material que não esteja de acordo com a licença CC-BY-SA 3.0.</p>\
')

#bottom
data = datetime.datetime.now()
text = text.replace("+++atualizadoem+++",
'<p style="text-align:right">Página gerada em ' +
str(data.day) + '/' + str(data.month) + '/' + str(data.year) +
' às ' + str(data.hour) + ':' + str(data.minute) + ':' + str(data.second) +
'.</p>'\
)

ofile = open(sdir+"//on_server//participe.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo participe.html ... feito!")



#************************************************#
# organizadores.html
#************************************************#
print("Construindo organizadores.htm ...")
    
os.system("cp index.aux "+sdir+"//on_server//organizadores.html")
ifile = open(sdir+"//on_server//organizadores.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Organizadores")
text = text.replace("+++keywords+++","organizadores")

#global alert
text = text.replace("+++alertaGeral+++",globalAlert)

#navbar
text = text.replace("+++navbar:inicio:active+++","")
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:forum:active+++","")
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++",'class="active"')
text = text.replace("+++listaDeHotsites+++",lisths)

#jumbotron
text = text.replace("+++jumbotron:subtitle+++",
                    "Organizadores")

#presentation
text = text.replace("+++presentation:coluna1+++",
'\
<h4>REAMAT - Álgebra Linear</h4>\
<ul class="list-unstyled">\
<li><a href="https://chasqueweb.ufrgs.br/~dmarcon/" target="_blank">Diego Marcon Farias - UFRGS</a></li>\
<li><a href="http://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
<li><a href="https://chasqueweb.ufrgs.br/~rafaelrigao/" target="_blank">Rafael Rigão Souza - UFRGS</a></li>\
</ul>\
<h4>REAMAT - Cálculo Numérico</h4>\
<ul class="list-unstyled">\
<li><a href="https://chasqueweb.ufrgs.br/~djusto/" target="_blank">Dagoberto Adriano Rizzotto Justo - UFRGS</a></li>\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="http://www.mat.ufrgs.br/~fabio" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="http://www.mat.ufrgs.br/~guidi/" target="_blank">Leonardo Fernandes Guidi - UFRGS</a></li>\
<li><a href="http://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h4>REAMAT - Computação Científica</h4>\
<ul class="list-unstyled">\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="http://www.mat.ufrgs.br/~fabio" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="http://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
<h4>REAMAT - Transformadas Integrais</h4>\
<ul class="list-unstyled">\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="http://www.mat.ufrgs.br/~fabio" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="http://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
')

#bottom
data = datetime.datetime.now()
text = text.replace("+++atualizadoem+++",
'<p style="text-align:right">Página gerada em ' +
str(data.day) + '/' + str(data.month) + '/' + str(data.year) +
' às ' + str(data.hour) + ':' + str(data.minute) + ':' + str(data.second) +
'.</p>'\
)

ofile = open(sdir+"//on_server//organizadores.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo organizadores.html ... feito!")

print("Congratulations! Program ended successfully. :)")

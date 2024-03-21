#!/usr/bin/python3

'''
Construção do portal reamat.

Autor: Pedro H A Konzen - UFRGS - 01/2018
Alterações: Fabio Azevedo - UFRGS -04/2018
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

if not(os.path.isdir(sdir+"/on_server")):
    os.system("mkdir "+sdir+"/on_server");

if not(os.path.isdir(sdir+"/on_server/bootstrap")):
    os.system("cp -rf "+sdir+"/bootstrap-3.3.7-dist "
                       +sdir+"/on_server/bootstrap")

if not(os.path.isdir(sdir+"/on_server/MathJax")):
    os.system("cp -rf "+sdir+"/MathJax-master "
                       +sdir+"/on_server/MathJax")

if not(os.path.isdir(sdir+"/on_server/fonts")):
    os.system("cp -rf "+sdir+"/fonts "
                       +sdir+"/on_server/fonts")

os.system("cp -rf "+sdir+"/figs "
                       +sdir+"/on_server/")

os.system("cp index.css "+sdir+"/on_server/index.css")

#global alert
ifile = open(sdir+"/globalAlert.aux",'r')
globalAlert = ifile.read()
ifile.close()    

#list of hotsites
ifile = open(sdir+"/lisths.aux",'r')
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
    
os.system("cp index.aux "+sdir+"/on_server/index.html")
ifile = open(sdir+"/on_server/index.html", 'r')
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

#presentation 			##substituí string no código por leitura de arquivo. (Fábio 19 de abril de 2018)
ifile = open(sdir+"/sobre.aux",'r')
text = text.replace("+++presentation:coluna1+++",ifile.read().replace("+++SDIR+++",sdir ))
ifile.close()


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
<h3>Outras informações</h3>\
<ul class="list-unstyled">\
<li><a href="perguntas_frequentes.html">Respostas a perguntas frequentes</a></li>\
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

ofile = open(sdir+"/on_server/index.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo index.html ... feito!")

#************************************************#
# forum.html
#************************************************#
print("Construindo forum.htm ...")
    
os.system("cp index.aux "+sdir+"/on_server/forum.html")
ifile = open(sdir+"/on_server/forum.html", 'r')
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
<p>O objetivo deste fórum é de servir como uma ferramenta \
de comunicação entre usuários e colaboradores do projeto. \
Deixe aqui qualquer dúvida, informe de erros ou sugestão \
relacionada aos recursos disponíveis.</p>\
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

ofile = open(sdir+"/on_server/forum.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo forum.html ... feito!")


#************************************************#
# participe.html
#************************************************#
print("Construindo participe.htm ...")
    
os.system("cp index.aux "+sdir+"/on_server/participe.html")
ifile = open(sdir+"/on_server/participe.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Participe")
text = text.replace("+++keywords+++",",participe")

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
<p>Participe de nosso <a href="./forum.html">fórum</a>, opine e ajude-nos no desenvolvimento do projeto.</p>\
<h3>Outras formas de colaboração</h3>\
<p>Toda a colaração é bem vinda! Caso tenha encontrado algum erro, imprecisão ou tenha alguma sugestão a fazer, escreva para nosso e-mail:</p>\
<p style="text-align: center;"><a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a></p>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3><span class="glyphicon glyphicon-edit"></span> Edição rápida</h3>\
<p>\
Utilize o botão <span class="glyphicon glyphicon-edit"></span> disponível nas páginas dos recursos para encaminhar edições rápidas. Ao clicar no botão, você será redirecionado ao código-fonte no GitHub do material referente à página que está consultando. Edite e registre seu <i>commit</i>. Então, um dos organizadores dará encaminhameto à sua colaboração.</p>\
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

ofile = open(sdir+"/on_server/participe.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo participe.html ... feito!")



#************************************************#
# organizadores.html
#************************************************#
print("Construindo organizadores.htm ...")
    
os.system("cp index.aux "+sdir+"/on_server/organizadores.html")
ifile = open(sdir+"/on_server/organizadores.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Organizadores")
text = text.replace("+++keywords+++",",organizadores")

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
<li><a href="https://professor.ufrgs.br/azevedo/" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="http:/professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
<li><a href="https://chasqueweb.ufrgs.br/~rafaelrigao/" target="_blank">Rafael Rigão Souza - UFRGS</a></li>\
</ul>\
<h4>REAMAT - Cálculo</h4>\
<ul class="list-unstyled">\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="https://professor.ufrgs.br/azevedo/" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="http:/professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
<h4>REAMAT - Cálculo Numérico</h4>\
<ul class="list-unstyled">\
<li><a href="https://chasqueweb.ufrgs.br/~djusto/" target="_blank">Dagoberto Adriano Rizzotto Justo - UFRGS</a></li>\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="https://professor.ufrgs.br/azevedo/" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="https://www.udesc.br/professor/helder.lima" target="_blank">Helder Geovane Gomes de Lima - UDESC</a></li>\
<li><a href="http:/www.mat.ufrgs.br/~guidi/" target="_blank">Leonardo Fernandes Guidi - UFRGS</a></li>\
<li><a href="http:/professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h4>REAMAT - Computação Científica</h4>\
<ul class="list-unstyled">\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="https://professor.ufrgs.br/azevedo/" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="https://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
<h4>REAMAT - Pré-cálculo</h4>\
<ul class="list-unstyled">\
<li><a href="https://sites.google.com/site/trecosmatematicos" target="_blank">Francieli Triches - UFSC</a></li>\
<li><a href="https://www.udesc.br/professor/helder.lima" target="_blank">Helder Geovane Gomes de Lima - UDESC</a></li>\
</ul>\
<h4>REAMAT - Transformadas Integrais</h4>\
<ul class="list-unstyled">\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></h4></li>\
<li><a href="https://professor.ufrgs.br/azevedo/" target="_blank">Fabio Souto de Azevedo - UFRGS</a></h4></li>\
<li><a href="https://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
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




#************************************************#
# perguntas_frequentes.html
# Incluído por Fabio dia 17 de abril de 2018
#************************************************#
print("Construindo perguntas_frequentes.htm ...")
    
os.system("cp index.aux "+sdir+"/on_server/perguntas_frequentes.html")
ifile = open(sdir+"/on_server/perguntas_frequentes.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Perguntas frequentes")
text = text.replace("+++keywords+++",",perguntas-frequentes")

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
                    "Perguntas frequentes")

#presentation


question=[]
answer=[]


#faq
ifile = open(sdir+"/faq.txt",'r')
rea_list = ifile.readlines()
token=''
k=0
for line in rea_list:
	if len(line)>2:
		if line[0:2]=='P)':
			token='P'
			k=k+1
			question.append(line[2:])

		if line[0:2]=='R)':
			token='R'
			answer.append(line[2:])

		if line[0:2]!='R)' and line[0:2]!='P)' and line[0]!='#':
			if token == 'R':
				answer[k-1]=answer[k-1]+line


ifile.close()    



n_cut_columns=6 ####You must do it by hand!

###Columa da esquerda
text_faq=""
for k in range(0,n_cut_columns):
	basic_text_faq = '<h3>+++question+++</h3><p>+++answer+++</p>'
	basic_text_faq = basic_text_faq.replace("+++question+++", question[k])
	basic_text_faq = basic_text_faq.replace("+++answer+++", answer[k])
	text_faq=text_faq + basic_text_faq


text_faq = text_faq.replace("+++indent+++","<br>&nbsp;&nbsp;&nbsp;")

text = text.replace("+++presentation:coluna1+++",text_faq)


###Columa da direita
text_faq=""
for k in range(n_cut_columns,len(question)):
	basic_text_faq = '<h3>+++question+++</h3><p>+++answer+++</p>'
	basic_text_faq = basic_text_faq.replace("+++question+++", question[k])
	basic_text_faq = basic_text_faq.replace("+++answer+++", answer[k])
	text_faq=text_faq + basic_text_faq


text_faq = text_faq.replace("+++indent+++","<br>&nbsp;&nbsp;&nbsp;")

text = text.replace("+++presentation:coluna2+++",text_faq)


#bottom
data = datetime.datetime.now()
text = text.replace("+++atualizadoem+++",
'<p style="text-align:right">Página gerada em ' +
str(data.day) + '/' + str(data.month) + '/' + str(data.year) +
' às ' + str(data.hour) + ':' + str(data.minute) + ':' + str(data.second) +
'.</p>'\
)

ofile = open(sdir+"//on_server//perguntas_frequentes.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo perguntas_frequentes.html ... feito!")



#************************************************#
# aviso.php
#************************************************#
print("Construindo aviso.php ...")
    
os.system("cp aviso.php "+sdir+"//on_server//aviso.php")
ifile = open(sdir+"//on_server//aviso.php", 'r')
text = ifile.read()
ifile.close()

#global alert
text = text.replace("+++alertaGeral+++",globalAlert)

#navbar
text = text.replace("+++listaDeHotsites+++",lisths)

#bottom
data = datetime.datetime.now()
text = text.replace("+++atualizadoem+++",
'<p style="text-align:right">Página gerada em ' +
str(data.day) + '/' + str(data.month) + '/' + str(data.year) +
' às ' + str(data.hour) + ':' + str(data.minute) + ':' + str(data.second) +
'.</p>'\
)

ofile = open(sdir+"//on_server//aviso.php", 'w')
ofile.write(text)
ofile.close()

print("Construindo aviso.php ... feito!")

print("Congratulations! Program ended successfully. :)")

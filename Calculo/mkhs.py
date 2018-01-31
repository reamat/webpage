#!/usr/bin/python3

'''
Constroi o hotsite reamat/AlgebraLinear.

Autor: Pedro H A Konzen - UFRGS - 01/2018
'''

import sys
import os
import string
import datetime

nomeDoRecurso = "Cálculo"
nomeDoRepo = "Calculo"

#parameters
sdir = ".."

#************************************************#
# Preliminares
#************************************************#
print("Preliminares ...")

if not(os.path.isdir(sdir+"/on_server/"+nomeDoRepo)):
    os.system("mkdir "+sdir+"/on_server/"+nomeDoRepo);

os.system("cp -rf "+sdir+"/"+nomeDoRepo+"/figs "
              +sdir+"/on_server/"+nomeDoRepo+"/")

os.system("cp index.css "+sdir+"/on_server/"+nomeDoRepo+"//index.css")

ifile = open(sdir+"//globalAlert.aux",'r')
globalAlert = ifile.read()
ifile.close()

#list of hotsites
ifile = open(sdir+"//lisths.aux",'r')
lisths = ""
for line in ifile:
    hsname = line.split(";")
    lisths += '<li><a href="../'+hsname[0]+'/index.html">'\
           +hsname[1].strip("\n")+'</a></li>'
ifile.close()


print("Preliminares ... feito!")
    
#************************************************#
# index.html
#************************************************#
print("Construindo index.htm ...")
    
os.system("cp index.aux "+sdir+"/on_server/"+nomeDoRepo+"/index.html")
ifile = open(sdir+"/on_server/"+nomeDoRepo+"/index.html", 'r')
text = ifile.read()
ifile.close()

#project names
text = text.replace("+++nomeDoRecurso+++",nomeDoRecurso)
text = text.replace("+++nomeDoRepo+++",nomeDoRepo)

#head
text = text.replace("+++title+++","")
text = text.replace("+++keywords+++","")

#global alert
text = text.replace("+++alertaGeral+++",globalAlert)

#navbar
text = text.replace("+++navbar:reamat:active+++","")
text = text.replace("+++navbar:projeto:active+++",'class="active"')
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++","")
text = text.replace("+++listaDeHotsites+++",lisths)

#jumbotron
text = text.replace("+++jumbotron:subtitle+++","")

#presentation
text = text.replace("+++presentation:coluna1+++",
'\
<h3>Sobre</h3>\
<p><strong>REAMAT - Cálculo</strong> \
é um projeto de escrita colaborativa de recursos \
educacionais abertos sobre cálculo diferencial e integral.</p>\
<p>Nosso objetivo é de fomentar o desenvolvimento \
de materiais didáticos pela colaboração entre \
professores e alunos de universidades, institutos de \
educação e demais interessados no estudo e \
aplicação do cálculo nos mais diversos ramos da \
ciência e tecnologia.</p>\
<p>Para tanto, disponibilizamos em repositório público \
<a href="https://github.com/reamat/Calculo" target="blank">\
GitHub</a> todo o código-fonte dos materiais \
em desenvolvimento sob licença \
<a href="https://creativecommons.org/licenses/by-sa/3.0/" \
target="_blank"> Creative Commons \
Atribuição-CompartilhaIgual 3.0 Não Adaptada \
(<strong>CC-BY-SA 3.0</strong>)</a>. \
Ou seja, você pode <strong>copiar</strong>, \
<strong>redistribuir</strong>, \
<strong>alterar</strong> e construir um novo material para \
qualquer uso, inclusive comercial. Leia a \
<a href="https://creativecommons.org/licenses/by-sa/3.0/" \
target="_blank">licença</a> para maiores informações. \
</p>\
<p>\
O sucesso do projeto depende da colaboração! Participe \
diretamenta da escrita dos recursos educacionais, dê \
sugestões ou nos avise de erros e imprecisões. Toda a \
colaboração é bem vinda. Veja como participar \
<a href="../participe.html">aqui</a>. \
</p>\
<p>\
Veja mais sobre o projeto REAMAT <a href="../index.html">aqui</a>.\
</p>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3>Recursos disponíveis</h3>\
<ul class="list-unstyled">\
<li><h4>Livros Colaborativos</h4>\
<ul class="list-unstyled">\
<li><a href="./livro-cfuv/main.html">\
Cálculo de funções de uma variável</a>\
</li>\
<li><a href="./livro-cfvv/main.html">\
Cálculo de funções de várias variáveis</a>\
</li>\
<li><a href="./livro-cv/main.html">\
Cálculo vetorial</a>\
</li>\
</ul>\
</li>\
</ul>\
<h3>Repositório GitHub</h3>\
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/Calculo"\
target="_blank">\
https://github.com/reamat/Calculo</a></li>\
</ul>\
<h3>Contato</h3>\
<ul class="list-unstyled">\
<li><a href="mailto:reamat@ufrgs.br">\
reamat@ufrgs.br</a></li>\
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

ofile = open(sdir+"//on_server//"+nomeDoRepo+"//index.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo index.html ... feito!")

print("Congratulations! Program ended successfully. :)")



#!/usr/bin/python3

'''
Constroi o hotsite reamat/Computação científica.

Autor: Pedro H A Konzen - UFRGS - 01/2018
'''

import sys
import os
import string
import datetime

nomeDoRecurso = "Computação Científica"
nomeDoRepo = "ComputacaoCientifica"

#parameters
sdir = ".."

#************************************************#
# Preliminares
#************************************************#
print("Preliminares ...")

if not(os.path.isdir(sdir+"//on_server//"+nomeDoRepo)):
    os.system("mkdir "+sdir+"//on_server//"+nomeDoRepo);

os.system("cp -rf "+sdir+"/"+nomeDoRepo+"/figs "
              +sdir+"/on_server/"+nomeDoRepo+"/")

os.system("cp index.css "+sdir+"//on_server//"+nomeDoRepo+"//index.css")

ifile = open(sdir+"//globalAlert.aux","r")
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
    
os.system("cp index.aux "+sdir+"//on_server//"+nomeDoRepo+"//index.html")
ifile = open(sdir+"//on_server//"+nomeDoRepo+"//index.html", 'r')
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
<p>\
<strong>REAMAT</strong> \
é um projeto de escrita colaborativa de recursos \
educacionais abertos (REA) sobre tópicos de matemática \
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
diretamente da escrita dos recursos educacionais, dê \
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
<ul class="list-unstyled">\
<li><h4><a href="livro/main.html">Livro Colaborativo</a></h4>\
</li>\
</ul>\
<h3>Repositório GitHub</h3>\
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/ComputacaoCientifica"\
target="_blank">\
https://github.com/reamat/ComputacaoCientifica</a></li>\
</ul>\
<h3>Outras informações</h3>\
<ul class="list-unstyled">\
<li><a href="perguntas_frequentes.html">Respostas a perguntas frequentes</a></li>\
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

print("Congratulations! ./ComputacaoCientifica/mkhs.py ended successfully. :)")



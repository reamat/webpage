#!/usr/bin/python3

'''
Constroi o hotsite reamat/AlgebraLinear.

Autor: Pedro H A Konzen - UFRGS - 01/2018
'''

import sys
import os
import string
import datetime

nomeDoRecurso = "Transformadas Integrais"
nomeDoRepo = "TransformadasIntegrais"

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

#presentation 			##substituí string no código por leitura de arquivo. (Fábio 19 de abril de 2018)
ifile = open(sdir+"/sobre.aux",'r')
text = text.replace("+++presentation:coluna1+++",ifile.read())
ifile.close()

textsc ='\
<h3>Recursos disponíveis</h3>\
<ul class="list-unstyled">\
<li><h4>Livros Colaborativos</h4>\
<ul class="list-unstyled">\
<li><a href="./livro-af/main.html">\
Análise de Fourier</a>\
</li>\
<li><a href="./livro-tl/main.html">\
Transformada de Laplace</a>\
</li>\
</ul>\
</li>\
</ul>\
<h3>Repositório GitHub</h3>\
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/TransformadasIntegrais"\
target="_blank">\
https://github.com/reamat/TransformadasIntegrais</a></li>\
</ul>'

ifile = open(sdir+"/secondcolumn.aux",'r')
textsc=textsc+ifile.read()
ifile.close()

text = text.replace("+++presentation:coluna2+++",textsc)


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

print("Congratulations! ./TransformadasIntegrais/mkhs.py ended successfully. :)")



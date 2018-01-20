#!/usr/bin/python3

'''
Constroi o hotsite reamat/CalculoNumerico.

Autor: Pedro H A Konzen - UFRGS - 01/2018
'''

import sys
import os
import string
import datetime

#parameters
sdir = ".."

#************************************************#
# Preliminares
#************************************************#
print("Preliminares ...")

if not(os.path.isdir(sdir+"//on_server//CalculoNumerico")):
    os.system("mkdir "+sdir+"//on_server//CalculoNumerico");

if not(os.path.isdir(sdir+"//on_server//CalculoNumerico//figs")):
    os.system("cp -rf "+sdir+"//CalculoNumerico/figs "
                       +sdir+"//on_server//CalculoNumerico//figs")

os.system("cp index.css "+sdir+"//on_server//CalculoNumerico//index.css")

print("Preliminares ... feito!")
    
#************************************************#
# index.html
#************************************************#
print("Construindo index.htm ...")
    
os.system("cp index.aux "+sdir+"//on_server//CalculoNumerico//index.html")
ifile = open(sdir+"//on_server//CalculoNumerico//index.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++","")
text = text.replace("+++keywords+++","")

#navbar
text = text.replace("+++navbar:reamat:active+++","")
text = text.replace("+++navbar:projeto:active+++",'class="active"')
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++","")

#jumbotron
text = text.replace("+++jumbotron:subtitle+++","")

#presentation
text = text.replace("+++presentation:coluna1+++",
'\
<h3>Sobre</h3>\
<p><strong>REAMAT - Cálculo Numérico</strong>\
é uma realização do projeto <a href="../index.html">\
<strong>REAMAT</strong></a>\
de escrita colaborativa de recursos\
educacionais abertos sobre tópicos de matemática\
em nível de um curso de graduação nas áreas das\
ciências exatas e da terra.\
</p>\
<p>\
Veja mais sobre o REAMAT <a href="../index.html">aqui</a>.\
</p>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3>Recursos disponíveis</h3>\
<ul class="list-unstyled">\
<li><h4>Livros Colaborativos</h4>\
<ul class="list-unstyled">\
<li><a href="./livro-oct/main.html">\
Cálculo Numérico - Versão GNU Octave</a>\
</li>\
<li><a href="./livro-sci/main.html">\
Cálculo Numérico - Versão Scilab</a>\
</li>\
<li><a href="./livro-py/main.html">\
Cálculo Numérico - Versão Python</a>\
</li>\
</ul>\
</li>\
</ul>\
<h3>Repositório GitHub</h3>\
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/CalculoNumerico"\
target="_blank">\
https://github.com/reamat/CalculoNumerico</a></li>\
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

ofile = open(sdir+"//on_server//CalculoNumerico//index.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo index.html ... feito!")

print("Congratulations! Program ended successfully. :)")



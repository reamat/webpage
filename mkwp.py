#!/usr/bin/python3

'''
Construção do portal reamat.

Autor: Pedro H A Konzen - UFRGS - 01/2018
'''

import sys
import os
import shutil
from os import walk
import numpy as np
import string
import urllib.parse

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

if not(os.path.isdir(sdir+"//on_server//pics")):
    os.system("cp -rf "+sdir+"//pics "
                       +sdir+"//on_server//pics")

os.system("cp index.css "+sdir+"//on_server//index.css")

print("Preliminares ... feito!")
    
#************************************************#
# index.html
#************************************************#
print("Construindo index.htm ...")
    
os.system("cp index_aux.html "+sdir+"//on_server//index.html")
ifile = open(sdir+"//on_server//index.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++","")
text = text.replace("+++keywords+++","")

#navbar
text = text.replace("+++navbar:inicio:active+++",'class="active"')
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++","")

#jumbotron
text = text.replace("+++jumbotron:subtitle+++",
                    "Recursos Educacionais Abertos de Matemática")

#presentation
text = text.replace("+++presentation:coluna1+++",
'\
<h3>Sobre</h3>\
<p>\
  <a href="./livro/main.html"><strong>REAMAT</strong></a>\
  é um projeto de escrita colaborativa de recursos \
  educacionais abertos sobre tópicos de matemática \
  em nível de um curso de graduação nas áreas das \
  ciências exatas e da terra. \
</p>\
<p>\
  Nosso objetivo é de produzir um material de excelente \
  qualidade e de acesso livre pela colaboração entre \
  professores e alunos de universidades, institutos de \
  educação e demais interessados no estudo, análise e \
  aplicação da matemática nos mais diversos ramos da \
  ciência e da tecnologia.\
</p>\
<p>\
  O sucesso do projeto depende da colaboração! Participe \
  diretamenta da escrita dos recursos educacionais, dê \
  sugestões ou nos avise de erros e imprecisões. Toda a \
  colaboração é bem vinda. Veja mais \
  <a href="participe.html">aqui</a>. \
</p>\
<p>\
  Nós preparamos uma série de ações para ajudá-lo a \
  participar. Em primeiro lugar, o acesso irrestrito aos \
  materias pode se dar através deste site. Além disso, os códigos \
  fontes e documentação dos recursos estão disponíveis em \
  <a href="https://github.com/reamat" \
  target="_blank">repositório GitHub</a> público. \
</p>\
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
  target="_blank">licença</a> para maiores informações. \
</p>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3>Recursos disponíveis</h3>\
<ul class="list-unstyled"> \
  <li><a href=".//linear//index.html">Álgebra Linear</a></li>\
  <li><a href="./numerico/index.html">Cálculo Numérico</a></li>\
  <li><a href="./transformadas/index.html">Transformadas Integrais</a></li>\
</ul>\
<h3>Repositórios GitHub</h3>\
<ul class="list-unstyled">\
  <li><a href="https://github.com/reamat">https://github.com/reamat</a></li>\
</ul>\
<h3>Contato</h3>\
<ul class="list-unstyled">\
<li><a href="mailto:reamat@ufrgs.br">reamat@ufrgs.br</a></li>\
</ul>\
')


ofile = open(sdir+"//on_server//index.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo index.html ... feito!")


#************************************************#
# participe.html
#************************************************#
print("Construindo participe.htm ...")
    
os.system("cp index_aux.html "+sdir+"//on_server//participe.html")
ifile = open(sdir+"//on_server//participe.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Participe")
text = text.replace("+++keywords+++","participe")

#navbar
text = text.replace("+++navbar:inicio:active+++","")
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:participe:active+++",'class="active"')
text = text.replace("+++navbar:organizadores:active+++","")

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
<h3>Acesse o repositório oficial dos recursos</h3>\
<ul class="list-unstyled">\
<li>Álgebra linear</li> \
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/AlgebraLinear">https://github.com/reamat/AlgebraLinear</a></li>\
</ul>\
<li>Cálculo numérico</li>\
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/CalculoNumerico">https://github.com/reamat/CalculoNumerico</a></li>\
</ul>\
<li>Transformadas integrais</li>\
<ul class="list-unstyled">\
<li><a href="https://github.com/reamat/TransformadasIntegrais">https://github.com/reamat/TransformadasIntegrais</a></li>\
</ul>\
</ul>\
')

text = text.replace("+++presentation:coluna2+++",
'\
<h3>Outras formas de colaboração</h3>\
<p>Toda a colaração é bem vinda! Caso tenha encontrado algum erro, imprecisão ou tenha alguma sugestão a fazer, escreva para nosso e-mail:</p>\
<p style="text-align: center;"><a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a></p>\
<h3>Aviso de violação de <i>copyright</i></h3>\
<p>Caso encontre qualquer violação de <i>copyright</i> em qualquer parte dos recursos disponibilizados, por favor, nos informe pelo e-mail:</p>\
<p style="text-align: center;"><a href="mailto:reamat@ufrgs.br" target="_top">reamat@ufrgs.br</a></p>\
<p>Iremos cuidar para analisar seu aviso o mais prontamente possível e removeremos o material que não esteja de acordo com a licença CC-BY-SA 3.0.</p>\
')


ofile = open(sdir+"//on_server//participe.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo participe.html ... feito!")



#************************************************#
# organizadores.html
#************************************************#
print("Construindo organizadores.htm ...")
    
os.system("cp index_aux.html "+sdir+"//on_server//organizadores.html")
ifile = open(sdir+"//on_server//organizadores.html", 'r')
text = ifile.read()
ifile.close()

#head
text = text.replace("+++title+++"," - Organizadores")
text = text.replace("+++keywords+++","organizadores")

#navbar
text = text.replace("+++navbar:inicio:active+++","")
text = text.replace("+++navbar:recursos:active+++","")
text = text.replace("+++navbar:participe:active+++","")
text = text.replace("+++navbar:organizadores:active+++",'class="active"')

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
<h4>REAMAT - Tranformadas Integrais</h4>\
<ul class="list-unstyled">\
<li><a href="" target="_blank">Esequia Sauter - UFRGS</a></li>\
<li><a href="http://www.mat.ufrgs.br/~fabio" target="_blank">Fabio Souto de Azevedo - UFRGS</a></li>\
<li><a href="http://professor.ufrgs.br/pedro/" target="_blank">Pedro Henrique de Almeida Konzen - UFRGS</a></li>\
</ul>\
')


ofile = open(sdir+"//on_server//organizadores.html", 'w')
ofile.write(text)
ofile.close()

print("Construindo organizadores.html ... feito!")




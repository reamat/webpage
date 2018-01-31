#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

########################################
#
# ATENÇÃO
#
# POR SEGURANÇA, NÃO EDITE ESTE ARQUIVO.
#
########################################

pdf: main.tex
	cp config-book.knd config.knd
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main
	cp main.pdf livro.pdf

html: main.html

main.html: main.tex
	cp config-html.knd config.knd
	mkdir -p ./html
	rm -f ./html/*
	latex main
	bibtex main
	latex main
	latex main
	htlatex main.tex "myconfig.cfg,3,notoc*" " -cunihtf" "-d./html/"
	cp config-book.knd config.knd

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.bbl \
	*.idx *.ilg *.ind *.blg *.backup \
	*.4tc *.lg *.tmp *.xref *.png *.html \
	*.4ct *.css *.idv *.maf *.mtc *.mtc0 \
	*.xml


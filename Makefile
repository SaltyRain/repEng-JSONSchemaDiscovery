.PHONY: report clean

DIRECTORY=rep-eng-paper
PAPERNAME=paper

report: $(DIRECTORY)/$(PAPERNAME).pdf

$(DIRECTORY)/$(PAPERNAME).pdf: $(DIRECTORY)/$(PAPERNAME).tex $(DIRECTORY)/acmart.cls $(DIRECTORY)/literature.bib $(DIRECTORY)/ACM-Reference-Format.bst
	cd $(DIRECTORY) && pdflatex $(PAPERNAME).tex; bibtex $(PAPERNAME); pdflatex $(PAPERNAME).tex; pdflatex $(PAPERNAME).tex;

clean:
	rm -rfv $(DIRECTORY)/*.pdf $(DIRECTORY)/*.log $(DIRECTORY)/*.aux $(DIRECTORY)/*.out $(DIRECTORY)/*.bbl $(DIRECTORY)/*.blg
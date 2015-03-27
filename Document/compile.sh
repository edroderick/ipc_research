rm *.bbl
rm *.aux
rm *.log
rm *.blg
rm *.out
thefile=draft
pdflatex $thefile.tex
bibtex $thefile.aux
pdflatex $thefile.tex
pdflatex $thefile.tex
rm *.bbl
rm *.aux
rm *.log
rm *.blg
rm *.out
open $thefile.pdf
#evince $thefile.pdf

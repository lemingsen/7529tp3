@echo off
ECHO Presione cualquier tecla para limpiar los archivos temporales de texlive,
ECHO o CTRL+C para cancelar...
PAUSE>nul
del .\tp*_grupo*.aux
del .\tp*_grupo*.fdb_latexmk
del .\tp*_grupo*.fls
del .\tp*_grupo*.log
del .\tp*_grupo*.pdf
del .\tp*_grupo*.synctex.gz
del .\tp*_grupo*.toc

del .\src\*.aux
del .\src\*.fdb_latexmk
del .\src\*.fls
del .\src\*.log
del .\src\*.pdf
del .\src\*.synctex.gz
del .\src\*.toc

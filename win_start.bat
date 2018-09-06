@ECHO "Activamos ENVIRONMENT"
activate test & ^
jupyter nbconvert test.ipynb --execute --to notebook & ^
jupyter notebook test.nbconvert.ipynb 
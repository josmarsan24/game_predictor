# PREDICCIÓN DE PARTIDOS DE NBA
Este repositorio es el trabajo de fin de grado de José Martín Sánchez, el objetivo es realizar un modelo para predicir partidos de la temporada 2021-2022 de la NBA

## Guía de instalación en Ubuntu
Instalar python (3.8.10 en mi caso), git, pip, pandas y flask:
- sudo apt update
- sudo apt install python3.8
- python --version

- sudo apt install python3-pip
- pip install pandas
- pip install Flask

- sudo apt-get install git-all

Clonar el repositorio:
- git clone https://github.com/josmarsan24/game_predictor.git

Crear un entorno virtual:
- python3 -m venv entorno
- source entorno/bin/activate

Ejecutar el flask:
- export FLASK_APP=app 
- export FLASK_ENV=development
- flask run


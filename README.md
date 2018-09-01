# PyConES2018: Introducción a Data Science en Python

Materiales para el taller 'Introducción a Data Science en Python' en la PyConES2018 realizado por los organizadores del meetup PyDataMallorca.

Twitter: https://twitter.com/PyDataMallorca

Meetup: https://www.meetup.com/PyData-Mallorca/

# Preparación para antes del taller

**NOTA: es muy importante que acudas al taller con todo instalado, para que puedas aprovechar al máximo todo lo que explicaremos.**

Necesitarás lo siguiente:

* Un portátil.
* Descargar los materiales para el curso y descomprimirlos en el portátil ([usa este enlace para descargarlos](https://github.com/PyDataMallorca/PyConES2018_Introduccion_a_data_science_en_Python/archive/master.zip)).
* Python 3.6 o superior instalado.
* Las librerías que vamos a usar (Jupyter, Numpy, Matplotlib, Pandas y Scikit-Learn).

Formas de conseguir lo anterior:

**Instalación de Anaconda**

La forma más sencilla sería instalando Anaconda para vuestro sistema operativo. La distribución Anaconda junto con instrucciones de cómo instalarlo lo podéis encontrar [en este enlace](https://www.anaconda.com/download/) (seleccionad la versión que incluya Python 3.6 o superior). La distribución Anaconda os instalará python 3.6 y un montón de paquetes que se usan en muchos ámbitos del data science y de la ciencia e ingeniería en general. Os dejamos también vídeos que hemos preparado para facilitaros el proceso:

* Para instalar Anaconda en linux: https://www.youtube.com/watch?v=b9LV1J7vPuw&t=192s
* Para instalar Anaconda en MacOS: Seguid las instrucciones de Linux de la línea anterior.
* Para instalar Anaconda en windows: https://www.youtube.com/watch?v=MSnNTODnSBg

**Instalación de miniconda**

Una segunda forma sería instalando MiniConda. Lo podéis descargar [desde este enlace](https://conda.io/miniconda.html) (seleccionad la versión que incluya Python 3.6 o superior). Una vez instalado MiniConda tenéis Python y una serie de utilidades instaladas. Os dejamos también vídeos que hemos preparado para facilitaros el proceso:

* Para instalar Miniconda en linux: https://www.youtube.com/watch?v=liqnwft_cbs
* Para instalar Miniconda en MacOS: Seguid las instrucciones de Linux de la línea anterior.
* Para instalar Miniconda en windows: https://www.youtube.com/watch?v=aYhlDfGhwuU

**Instalación de paquetes específicos**

Para instalar el resto de paquetes necesarios podéis abrir una terminal (Linux/Mac) o el AnacondaPrompt (Windows), ejecutad lo siguiente (dependiendo del sistema operativo en el que estéis deberéis ejecutar unas cosas u otras).

`cd ruta/a/la/carpeta/descargada/y/descomprimida` (Linux o Mac)

`cd C:\ruta\a\la\carpeta\descargada\y\descomprimida` (Windows)

`conda env create -f environment.yml` (Linux, Mac, Windows)


# En el taller

Como en el paso anterior habéis instalado los paquetes necesarios, solamente tenéis que activar el entorno que creasteis y usar los paquetes. Para ello, en la misma terminal que los pasos anteriores deberéis ejecutar

`source activate taller_DS_pycones2018`

Y finalmente también ejecutar jupyter notebook para acceder al tutorial. Atención: se abrirá un navegador web.

`jupyter notebook`



# TO-DO

* Preparar vídeo con cómo instalarlo todo par facilitar este paso.

# Temática del taller

1. Introducción al taller. Para empezar, comentaremos qué es Data Science, Big Data, Machine Learning y otros conceptos relacionados y cómo encaja el lenguaje Python en todo ello. Asimismo, enunciaremos los requisitos que debería tener un analista de datos.

2. Introducción a Jupyter. En el taller utilizaremos Jupyter, que es una aplicación que permite editar código Python, así como también otros lenguajes como R, Julia o Scala, de forma conjunta con texto enriquecido y que es ampliamente utilizado en el análisis de datos actualmente. En este bloque explicaremos cómo utilizarlo y sus funcionalidades principales.

3. Breve introducción a la anatomía de un numpy array. Todo el ecosistema científico Python usa de forma generalizada los arrays de numpy en sus tripas. En este bloque intentaremos explicar cómo funciona un numpy array para que le podáis sacar el máximo provecho numérico a Python.

4. Tratamiento de datos mediante Pandas. Pandas es la librería principal de carga, consulta y modificación de datos en Python. En este bloque realizaremos diversos ejercicios para conocer las funcionalidades más importantes de Pandas y prepararnos para los siguientes bloques.

5. Visualización de datos con Matplotlib. Por su parte, Matplotlib es una librería de Python que nos permite construir gráficos. Durante este apartado veremos cómo crear gráficos fácilmente mediante esta librería y realizaremos ejercicios para poner en práctica esta librería.

6. Resolución de un problema de clasificación mediante scikit-learn. Posteriormente, propondremos un problema de clasificación y explicaremos un algoritmo matemático que permita su resolución, ¡no te asustes! No entraremos en explicaciones matemáticas profundas, pero sí intentaremos comprender cómo funcionan estos algoritmos de forma general y en particular para el algoritmo de clasificación escogido. Haremos ejercicios y jugaremos con los datos para poder entender mejor cómo funciona un algoritmo de este tipo. Utilizaremos scikit-learn, que es la librería de Python que nos permite implementar soluciones de Machine Learning.

# Autores y colaboradores (por orden alfabético)

* Jordi Contestí

* Kiko Correoso ([pybonacci.org](https://pybonacci.org), [twitter](https://twitter.com/Pybonacci)).

* Guillem Duran

* Juan Carlos González

* Antònia Tugores

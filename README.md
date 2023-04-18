<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# <p align=center> **MLOPS - Streaming Services** </h1>
# <p align=center> **Proyecto Individual realizado por Manuel Urquijo** </h3>


### Descripción. </h4>

El objetivo principal de este proyecto es crear una API, donde se puedan realizar ciertas consultas requeridas por un cliente a una base de datos que se construyó a partir de varios archivos, pertenecientes a plataformas de streaming que se mencionarán a lo largo del trabajo. 

El [repositorio](https://github.com/maurquijo/mlops_streaming/tree/main/Dataset "repositorio") que vamos a utilizar se trata de diferentes archivos de tipo .csv, que reflejan las películas y series que se encuentran en las siguientes plataformas de streaming:
- Amazon Prime.
- Disney Plus.
- Hulu.
- Netflix. 

Cada uno de ellos consta de ciertas filas y columnas donde se podrán ver el tipo de filmación (si es una película o una serie/programa de televisión), el título de la obra, el/la director/a, el elenco que lo compone, el país donde se realizó la producción, la fecha en la que se agregó a la plataforma, el año en el que se filmó, el público destinado, su duración, la categoría en la que pertenece, y por último, una breve descripción de la película o serie.

<hr>

### Proceso de ETL (Extract, Transform, Load).

Dentro de este [archivo](https://github.com/maurquijo/mlops_streaming/blob/main/MLOPs_Streaming_Services.ipynb "archivo"), se podrá observar todo el proceso de ETL de los datos. 

Cabe mencionar que se realizaron diferentes transformaciones que se consideraron necesarias para poder llevar a cabo este proyecto, teniendo en cuenta la posible elaboración de un sistema de recomendación para nuevos usuarios de las plataformas mencionadas en un futuro.

Generalmente, las transformaciones que se ejecutaron tienen que ver con el tratado de valores y campos nulos, cambios de formato de los tipos de datos que se encontraban en los archivos originales,  creación de nuevas columnas y renombrar existentes, entre otras modificaciones. 

<hr>

### Desarrollo de la API.

En este [archivo](https://github.com/maurquijo/mlops_streaming/blob/main/funciones.py "archivo"), se podrán ver las funciones desarrolladas para poder consultar a los datos obtenidos, a través de parámetros variables que ingrese el usuario. Luego, se tomaron las funciones del archivo mencionado anteriormente, y se construyó una API para que se puedan realizar las consultas de manera correcta desde cualquier dispositivo, donde se puede acceder mediante este [link](https://mlops-pi.onrender.com/docs#/"link").

Dentro de esta aplicación, se podrán realizar las siguientes queries a la base de datos:

1. Película con mayor duración según el año, la plataforma de streaming y su tipo de duración (min). En este [ejemplo](https://mlops-pi.onrender.com/get_max_duration/2017/amazon%20prime/min "ejemplo"), se buscó la película (formato min) con mayor duración en el 2017, dentro de la plataforma Amazon Prime.
2. Cantidad de películas por plataforma con un puntaje mayor a XX en un año determinado. En este [ejemplo](https://mlops-pi.onrender.com/get_score_count/amazon%20prime/3.4/2016 "ejemplo"), se buscó la cantidad de películas con una puntaje mayor a 3.4 en Amazon Prime producida en 2016.
3. Cantidad de películas que se pueden encontrar según la plataforma. En este [ejemplo](https://mlops-pi.onrender.com/get_count_platform/hulu "ejemplo"), se buscó la cantidad de películas/contenido que se encuentra disponible en Hulu.
4. Actor que más se repite en los elencos según la plataforma y el año de la producción cinematográfica. En este [ejemplo](https://mlops-pi.onrender.com/get_actor/netflix/2019 "ejemplo"), se buscó el actor que más se repite en los elencos de las producciones cinematográficas disponibles en Netflix en el año 2019.
6. La cantidad de contenidos/productos que se publicó por país y año. En este [ejemplo](https://mlops-pi.onrender.com/prod_per_country/movie/united%20states/2017 "ejemplo"), se buscó la cantidad de películas originadas en Estados Unidos (indicado como: "united states") que se publicaron en 2017.
7. La cantidad total de contenidos según el rating de audiencia dado (para que publico fue clasificada la pelicula). [ejemplo](https://mlops-pi.onrender.com/get_contents/13%2B "ejemplo"), se buscó la cantidad de contenido que es apto para mayores de 13 años (indicado como: "13+").

Por otro lado, en este [documento de Python](https://github.com/maurquijo/mlops_streaming/blob/main/main.py "documento de Python"), se podrá observar el código utilizado para la creación de la aplicación.

<hr>

### Video explicativo. 

Por otro lado, se desarrrolló un video explicativo para mostrar el proyecto de una manera más amigable. Se puede ver clickeando en este [link](https://www.youtube.com/watch?v=TUYXXxH9EKc&t=7s "link"). 

<hr>

### Herramientas ulitizadas.

- Visual Studio Code.
- Jupyter Notebooks.
- Python.
- Pandas.
- FastApi.
- Uvicorn.
- Render.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Visual_Studio_Code_0.10.1_icon.png/120px-Visual_Studio_Code_0.10.1_icon.png" width="90"/>
<img src="https://jupyter.org/assets/homepage/main-logo.svg" width="90">
<img src="https://www.python.org/static/community_logos/python-logo.png" width="200"/>
<img src="https://www.kindpng.com/picc/m/574-5747046_python-pandas-logo-transparent-hd-png-download.png" width="200"/>
<img src="https://i.imgur.com/p0Nufjn.jpg" width="125"/>
<img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" width="100"/>
<img src="https://ml.globenewswire.com/Resource/Download/19618237-eb42-4ed2-b7a1-1f56419d1279?size=3" width="190">

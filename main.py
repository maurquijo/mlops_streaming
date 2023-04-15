# Se importan el módulo de FastAPI y el archivo de funciones.py para poder realizar las consultas.
from fastapi import FastAPI
import funciones as fn

# Se crea la app donde se realizarán las consultas.
app = FastAPI(title = "MLOPS_PI")

# Se crea un mensaje de explicación de uso de la app para que aparezca cuando se quiera utilizar esta app.
@app.get('/')
def index():
    return 'Bienvenido a la interfaz de consultas de las plataformas de streaming de Amazon Prime, Disney Plus, Hulu y Netflix. Usted podrá obtener los datos que se mencionaron en el archivo llamado Funciones_API.ipynb.'

# Luego, desarrollamos las ingestamos las funciones creadas en el archivo funciones.py para poder obtener los diversos resultados de las consultas generadas por el cliente.   

'''Consulta N°1: Película con mayor duración según el año, la plataforma de streaming y su tipo de duración (min).'''

# Creamos el url para que se pueda realizar dicha consulta.
@app.get('/get_max_duration/{anio}/{plataforma}/{dtype}')
def get_max_duration(anio: int, plataforma :str, dtype: str):
    return fn.get_max_duration(anio, plataforma, dtype)

# Prueba de consulta:

'''Consulta N°2: Cantidad de películas por plataforma con un puntaje mayor a XX en un año determinado.'''

# Creamos el url para que se pueda realizar dicha consulta.
@app.get('/get_score_count/{plataforma}/{scored}/{anio}')
def get_score_count(plataforma: str, scored: float, anio: int):
    return fn.score_count(plataforma, scored, anio)

# Prueba de consulta:

'''Consulta N°3: Cantidad de películas que se pueden encontrar según la plataforma.'''

# Creamos el url para que se pueda realizar dicha consulta.
@app.get('/get_count_platform/{plataforma}')
def get_count_platform(plataforma: str): 
    return fn.count_platform(plataforma)   

# Prueba de consulta:

'''Consulta N°4: Actor que más se repite en los elencos según la plataforma y
 el año de la producción cinematográfica. '''

# Creamos el url para que se pueda realizar dicha consulta.
@app.get('/get_actor/{plataforma}/{anio}')
def get_actor(plataforma: str, anio: int):
    return fn.actor(plataforma,anio)

# Prueba de consulta:

'''Consulta N°5: La cantidad de contenidos/productos que se publicó por país y año.'''

# Creamos el url para que se pueda realizar dicha consulta.
@app.get('/prod_per_country/{tipo}/{pais}/{anio}')
def prod_per_country(tipo: str, pais: str, anio: int):
    return fn.prod_country(tipo,pais,anio)

# Prueba de consulta: 

''' Consulta N°6: La cantidad total de contenidos según el rating
 de audiencia dado (para que publico fue clasificada la pelicula).'''

# Creamos el url para que se pueda realizar dicha consulta.
@app.get('/get_contents/{rating}')
def get_contents(rating:str):
    return fn.contents(rating)

# Prueba de consulta:
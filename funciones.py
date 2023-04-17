'''Desarrollo de funciones para realizar las consultas.

El cliente solicita que desde la API se puedan realizar seis consultas diferentes a nuestros datos. Las consultas son:
1. Película con mayor duración según el año, la plataforma de streaming y su tipo de duración (min).
2. Cantidad de películas por plataforma con un puntaje mayor a XX en un año determinado.
3. Cantidad de películas que se pueden encontrar según la plataforma.
4. Actor que más se repite en los elencos según la plataforma y el año de la producción cinematográfica.
5. La cantidad de contenidos/productos que se publicó por país y año.
6. La cantidad total de contenidos según el rating de audiencia dado (para que publico fue clasificada la pelicula).


En este apartado, se encontrarán las funciones que se realizaron para poder navegar dentro del DataFrame y obtener las respuestas a consultas que se mencionaron anteriormente.
'''

# Antes de comenzar, importamos la librería a utilizar, llamada Pandas.
import pandas as pd

# Primero importamos el archivo para que podamos realizar las consultas necesarias.
plataformas_df = pd.read_csv(r'C:\Users\Manuel\Desktop\Henry\LABS\MLOPS_PI\Dataset\Streaming_services_clean.csv')

# Consulta N°1: Película con mayor duración según el año, la plataforma de streaming y su tipo de duración (min).
def max_duration(anio: int, plataforma :str, dtype: str):
    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    gmd_p = plataformas_df 
    
    # Se crean los filtros de  dependiendo la plataforma, el año y si es tipo 'min' o 'season'.
    if dtype == 'min':
        if plataforma.lower() == 'amazon prime':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'a' in x))] 
        elif plataforma.lower() == 'disney plus':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'd' in x))]
        elif plataforma.lower() == 'hulu':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'h' in x))]
        elif plataforma.lower() == 'netflix':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'n' in x))]
        else: 
            # En caso de que se consulte otra plataforma que no esté cargada en la base de datos, se retornará este mensaje explicativo.
            return 'No se encuentra en nuestro dataset la plataforma que desea buscar. Cabe aclarar que sólo tenemos registros pertenecientes a: Amazon Prime, Disney Plus, Hulu y Netflix. Disculpe las molestias ocasiondas.'
    else:    
        return 'La función sólo permite buscar películas con máxima duración. Para realizar la búsqueda ingrese: min.'
    
    # Se crea el filtro para que se obtenga la fila de la película o serie que tiene más duración.
    gmd_p_copia = gmd_p[gmd_p['duration_int'] == (gmd_p['duration_int'].max())]

    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {'pelicula': gmd_p_copia.iloc[0,2]}

# Consulta N°2: Cantidad de películas por plataforma con un puntaje mayor a XX en un año determinado.
def score_count(plataforma: str, scored: float, anio: int):    

    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    gsc_p= plataformas_df
    
    # Se crea el filtro para que se obtenga el resultado correcto segun el año de lanzamiento de la película/serie y que tenga una puntuación mayor a la que establezca el usuario.
    gsc_p = gsc_p[(gsc_p['mean_score'] >= scored) & (gsc_p['release_year'] == anio)]
    
    # Se crea el filtro para que pueda discriminar según la plataforma a buscar.
    if plataforma.lower() == 'amazon prime':
        gsc_pc = gsc_p[gsc_p['id'].apply(lambda x: 'a' in x)]

    elif plataforma.lower() == 'disney plus':
        gsc_pc = gsc_p[gsc_p['id'].apply(lambda x: 'd' in x)]
    
    elif plataforma.lower() == 'hulu':
        gsc_pc = gsc_p[gsc_p['id'].apply(lambda x: 'h' in x)]

    elif plataforma.lower() == 'netflix':
        gsc_pc = gsc_p[gsc_p['id'].apply(lambda x: 'n' in x)]

    # En caso de que se consulte otra plataforma que no esté cargada en la base de datos, se retornará este mensaje explicativo.
    else:
        print('No se encuentra en nuestro dataset la plataforma que desea buscar. Cabe aclarar que sólo tenemos registros pertenecientes a: Amazon Prime, Disney Plus, Hulu y Netflix. Disculpe las molestias ocasiondas')
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {
        'plataforma': plataforma,
        'cantidad': gsc_pc.shape[0],
        'anio': anio,
        'score': scored
    }

# Consulta N°3: Cantidad de películas que se pueden encontrar según la plataforma..
def count_platform(plataforma: str):

# Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    gcp_p = plataformas_df
    
    # Se crea el filtro para que pueda discriminar según la plataforma a buscar.
    if plataforma.lower() == 'amazon prime':
        gcp_pc= gcp_p[gcp_p['id'].apply(lambda x: 'a' in x)]

    elif plataforma.lower() == 'disney plus':
        gcp_pc = gcp_p[gcp_p['id'].apply(lambda x: 'd' in x)]
    
    elif plataforma.lower() == 'hulu':
        gcp_pc = gcp_p[gcp_p['id'].apply(lambda x: 'h' in x)]

    elif plataforma.lower() == 'netflix':
        gcp_pc = gcp_p[gcp_p['id'].apply(lambda x: 'n' in x)]
    
    # En caso de que se consulte otra plataforma que no esté cargada en la base de datos, se retornará este mensaje explicativo.
    else:
        print('No se encuentra en nuestro dataset la plataforma que desea buscar. Cabe aclarar que sólo tenemos registros pertenecientes a: Amazon Prime, Disney Plus, Hulu y Netflix. Disculpe las molestias ocasiondas')
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {'plataforma': plataforma, 'peliculas': gcp_pc.shape[0]}   

# Consulta N°4: Actor que más se repite en los elencos según la plataforma y el año de la producción cinematográfica.
# Se define primero una funcion auxiliar para crear un diccionario con los actores y sus apariciones
def crear_dic_act(lista_serie):
    lista_actores = []
    for i in range(1, len(lista_serie)):
        for a in lista_serie[i]:
            lista_actores.append(a.strip())

    apariciones = {}
    for item in lista_actores:
        if (item in apariciones):
            apariciones[item] += 1
        else:
            apariciones[item] = 1
    return apariciones
    
def actor(plataforma, anio):
    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    ga_p = plataformas_df
    
    # Se crea el filtro para que pueda discriminar según la plataforma, y luego obtener el valor que más se repite. 
    if plataforma.lower() == 'amazon prime':
        ga_pc= ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'a' in x))]
        p = ga_pc['cast'].astype(str)
        p = p.apply(lambda x: x.split(','))
        p = list(p.value_counts().index)

        apariciones = crear_dic_act(p)

        try:
            aux = max(apariciones.values())
            ga_pca = [i for i in apariciones if apariciones[i]==aux][0]
        except:
            return 'Hubo complicaciones intentando encontrar la informacion solicitada.'

    elif plataforma.lower() == 'disney plus':
        ga_pc = ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'd' in x))]
        p = ga_pc['cast'].astype(str)
        p = p.apply(lambda x: x.split(','))
        p = list(p.value_counts().index)

        apariciones = crear_dic_act(p)
        
        try:
            aux = max(apariciones.values())
            ga_pca = [i for i in apariciones if apariciones[i]==aux][0]
        except:
            return 'Hubo complicaciones intentando encontrar la informacion solicitada.'

    elif plataforma.lower() == 'hulu':
        ga_pc = ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'h' in x))]
        p = ga_pc['cast'].astype(str)
        p = p.apply(lambda x: x.split(','))
        p = list(p.value_counts().index)

        print(p)

        apariciones = crear_dic_act(p)

        print(apariciones)
        try:
            aux = max(apariciones.values())
            ga_pca = [i for i in apariciones if apariciones[i]==aux][0]
        except:
            return 'Hubo complicaciones intentando encontrar la informacion solicitada.'

    elif plataforma.lower() == 'netflix':
        ga_pc = ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'n' in x))]
        p = ga_pc['cast'].astype(str)
        p = p.apply(lambda x: x.split(','))
        p = list(p.value_counts().index)

        apariciones = crear_dic_act(p)
    
        try:
            aux = max(apariciones.values())
            ga_pca = [i for i in apariciones if apariciones[i]==aux][0]
        except:
            return 'Hubo complicaciones intentando encontrar la informacion solicitada.'
        
    # En caso de que se consulte otra plataforma que no esté cargada en la base de datos, se retornará este mensaje explicativo.
    else:
        return 'No se encuentra en nuestro dataset la plataforma que desea buscar. Cabe aclarar que sólo tenemos registros pertenecientes a: Amazon Prime, Disney Plus, Hulu y Netflix. Disculpe las molestias ocasiondas'
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {
        'plataforma': plataforma,
        'anio': anio,
        'actor': ga_pca,
        'apariciones': int(aux)
    }

# Consulta N°5: La cantidad de contenidos/productos que se publicó por país y año.
def prod_country(tipo: str, pais: str, anio: int):
    
    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    ppc_p = plataformas_df

    # Se crea un condicional en caso de que se ingrese un valor erróneo en el parámetro 'tipo'.
    if tipo not in ('movie','tv show'):
        
        return 'La función sólo acepta el tipo como movie o tv show. Ingrese algún formato válido.'
    
    else:
        
        # Se crea el filtro para que pueda discriminar según el tipo ('movie' o 'tv show'), pais y anio de la producción cinematográfica.
        ppc_pa = ppc_p[(ppc_p['type'] == tipo) & (ppc_p['country'] == pais) & (ppc_p['release_year'] == anio)]

        # Por último, imprime un mensaje donde contiene los resultados de la consulta.
        return {'pais': pais, 'anio': anio, 'peliculas': int(ppc_pa.count()[0])}

# Consulta N°6: La cantidad total de contenidos según el rating de audiencia dado (para que publico fue clasificada la pelicula).
def contents(rating:str):

    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    gc_p = plataformas_df

    # Se crea el filtro para que pueda discriminar por el rating que eligió el usuario.
    gc_pr = gc_p[(gc_p['rating'] == rating)]

    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {'rating': rating, 'contenido': int(gc_pr.count()[0])}
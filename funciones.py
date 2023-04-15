import pandas as pd

plataformas_df = pd.read_csv(r'.\Dataset\Streaming_services_clean.csv')

# Consulta N°1:
def get_max_duration(anio: int, plataforma :str, dtype: str):
    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    gmd_p = plataformas_df 
    
    # Se crean los filtros de  dependiendo la plataforma, el año y si es tipo 'min' o 'seasons'.
    if plataforma.lower() == 'amazon prime':
        if dtype == 'min':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'a' in x))]
        elif dtype == 'season':
            return 'La función sólo permite buscar películas con máxima duración. Para realizar la búsqueda ingrese: min.'
    
    elif plataforma.lower() == 'disney plus':
        if dtype == 'min':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'd' in x))]
        elif dtype == 'season':
            return 'La función sólo permite buscar películas con máxima duración. Para realizar la búsqueda ingrese: min.'
    
    elif plataforma.lower() == 'hulu':
        if dtype == 'min':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'h' in x))]
        elif dtype == 'season':
            return 'La función sólo permite buscar películas con máxima duración. Para realizar la búsqueda ingrese: min.'
    
    elif plataforma.lower() == 'netflix':
        if dtype == 'min':
            gmd_p = gmd_p[(gmd_p['type'] == 'movie') & (gmd_p['release_year'] == anio) & (gmd_p['duration_type'] == dtype) & (gmd_p['id'].apply(lambda x: 'n' in x))]
        elif dtype == 'season':
            return 'La función sólo permite buscar películas con máxima duración. Para realizar la búsqueda ingrese: min.'
    
    # En caso de que se consulte otra plataforma que no esté cargada en la base de datos, se retornará este mensaje explicativo.
    else: 
        print('No se encuentra en nuestro dataset la plataforma que desea buscar. Cabe aclarar que sólo tenemos registros pertenecientes a: Amazon Prime, Disney Plus, Hulu y Netflix. Disculpe las molestias ocasiondas.')
        return None
    
    # Se crea el filtro para que se obtenga la fila de la película o serie que tiene más duración.
    gmd_p_copia = gmd_p[gmd_p['duration_int'] == (gmd_p['duration_int'].max())]
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {'pelicula': gmd_p_copia.iloc[0,2]}

# Consulta N°2.
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

# Consulta N°3.
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

# Consulta N°4.
def actor(plataforma: str, anio: int):
    
    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    ga_p = plataformas_df
    
    # Se crea el filtro para que pueda discriminar según la plataforma, y luego obtener el valor que más se repite. 
    if plataforma.lower() == 'amazon prime':
        ga_pc= ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'a' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()
        aux = ga_pc.loc[ga_pc['cast'] == ga_pca].count()[0]

    elif plataforma.lower() == 'disney plus':
        ga_pc = ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'd' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()
        aux = ga_pc.loc[ga_pc['cast'] == ga_pca].count()[0]

    elif plataforma.lower() == 'hulu':
        ga_pc = ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'h' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()
        aux = ga_pc.loc[ga_pc['cast'] == ga_pca].count()[0]

    elif plataforma.lower() == 'netflix':
        ga_pc = ga_p[(ga_p['release_year'] == anio) & (ga_p['id'].apply(lambda x: 'n' in x))]
        ga_pca= ga_pc['cast'].value_counts().idxmax()
        aux = ga_pc.loc[ga_pc['cast'] == ga_pca].count()[0]
        
    # En caso de que se consulte otra plataforma que no esté cargada en la base de datos, se retornará este mensaje explicativo.
    else:
        print('No se encuentra en nuestro dataset la plataforma que desea buscar. Cabe aclarar que sólo tenemos registros pertenecientes a: Amazon Prime, Disney Plus, Hulu y Netflix. Disculpe las molestias ocasiondas')
    
    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {
        'plataforma': plataforma,
        'anio': anio,
        'actor': ga_pca,
        'apariciones': aux
    }

# Consulta N°5.
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
        return {'pais': pais, 'anio': anio, 'peliculas': ppc_pa.count()[0]}

# Consulta N°6.
def contents(rating:str):

    # Se realiza una copia de la base de datos para que, en el caso de que pase, no sufra modificaciones la base de datos original.
    gc_p = plataformas_df

    # Se crea el filtro para que pueda discriminar por el rating que eligió el usuario.
    gc_pr = gc_p[(gc_p['rating'] == rating)]

    # Por último, imprime un mensaje donde contiene los resultados de la consulta.
    return {'rating': rating, 'contenido': gc_pr.count()[0]}
"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
from pathlib import Path

def limpiar_col(col: pd.Series):

    column = col.copy()
    column = column.str.lower().str.replace(' ', '_').str.replace('.', '_').str.replace('-', '_').str.strip()

    return column

def limpiar_csv(df: pd.DataFrame):

    df = df.copy()
    df = df.dropna()

    # Col 1, 2, 3, 4: Sexo, Tipo de emprendimiento, Idea Negocio, Barrio
    columnas = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']
    df[columnas] = df[columnas].apply(lambda x: limpiar_col(x).astype('category'))

    # Col 5: Estrato esta bien
    # Col 6: Comuna ciudadano
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int).astype('category')

    # Col 7: Fecha de beneficio
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')

    # Col 8: Monto del crédito
    df['monto_del_credito'] = df['monto_del_credito'].str.removeprefix('$ ').str.replace(',', '').astype(float)

    df.drop_duplicates(inplace=True)

    return df

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    df = pd.read_csv('files/input/solicitudes_de_credito.csv', index_col=0, sep=';')
    df = limpiar_csv(df)
    output_path = Path('files/output')

    output_path.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path / 'solicitudes_de_credito.csv', sep=';')




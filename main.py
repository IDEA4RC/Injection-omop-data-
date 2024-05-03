import psycopg2
import csv
import pandas as pd
import dotenv
import os
from os.path import isdir, isfile, join
from os import walk

# Obtener la ruta completa al archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(dotenv_path)

# Cargar variables de entorno desde el archivo .env
dotenv.load_dotenv(dotenv_path)

# Parámetros de conexión a la base de datos
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")


# Establecer conexión con la base de datos
try:
    conexion = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    print("Conexión exitosa a la base de datos PostgreSQL")
except psycopg2.Error as e:
    print(f"Error al conectar a la base de datos: {e}")

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

def obtener_tabla(nombre_tabla):
  """
  Ejecuta una consulta SQL para obtener los datos de una tabla específica.

  Args:
    nombre_tabla: El nombre de la tabla de la que se quieren obtener los datos.

  Returns:
    Los resultados de la consulta SQL como un objeto de tipo cursor.
  """
  consulta = f"SELECT * FROM {nombre_tabla};"
  cursor.execute(consulta)
  return cursor.fetchall() 


# Ejemplo de uso
tablas = ["attribute_definition","care_site","cdm_source", "cohort","cohort_definition","concept","concept_ancestor","concept_class","concept_class","condition_era","cost", "device_exposure", "domain", "dose_era", "drug_exposure", "drug_strength", "fact_relationship", "location", "location_history", "measurement", "metadata", "note", "note_nlp", "observation", "observation_period", "payer_plan_period", "person", "procedure_ocurrence", "provider", "relationship", "source_to_concept_map","specimen","survey_conduct","visit_detail","visit_ocurrence","vocabulary"]

for tabla in tablas:
  datos_tabla = obtener_tabla(tabla)
  # Procesar los datos de la tabla
  print(f"Datos de la tabla {tabla}:")
  # Convertir los resultados en un DataFrame de Pandas
  df = pd.DataFrame(datos_tabla, columns=[col.name for col in cursor.description])
  # Guardar el DataFrame en un archivo CSV
  df.to_csv(f"datos_cdm_omop {tabla}.csv", index=False)
  print(f"Datos guardados en archivo CSV: datos_cdm_omop{tabla}.csv")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

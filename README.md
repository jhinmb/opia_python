# Predicción del precio de casas en California (servicio web)

<!-- TODO: documento de 10-20 líneas de texto añadido -->

Autores: Alexander Selivanov.

## Contenido del repositorio

Proyecto con todo el codigo para la practica 2 de opia.

* root/
  * app.py: API desarrollada con FastAPI.
  * entrenamiento_modelo_california.py: entrenamiento del modelo.
  * modelo_california.pkl: modelo entrenado.
  * requirements.txt: dependencias del proyecto.
  * medir_tiempos.py: medición de tiempos de respuesta.

## Pasos del despliegue

1. Se creó este repositorio público para el proyecto.
2. Se subió al repositorio un rpoyecto nuevo de python con los archivos del modelo y de la API.
3. Se creó una cuenta en Render (eligiendo la opción de Github).
4. Se conectó el repositorio de GitHub con Render al crear un nuevo Web Service.
5. Se cambió la región del servicio a una más cercana (Frankfurt (EU Central)).
6. Se configuró la carpeta raíz del proyecto como root/.
7. Se configuró el comando de inicio: uvicorn app:app --host 0.0.0.0 --port $PORT 
8. Se termino la creación del web service y se realizo un deploy del ultimo commit del repositorio, donde
se instalaron las dependencias mediante requirements.txt.
9. Se desplegó el servicio automáticamente.

## URL final
<https://opia-python.onrender.com>

# Regresión Lineal API

Una API desarrollada con **FastAPI** que permite realizar análisis de regresión lineal sobre datos proporcionados en formato JSON. La API incluye endpoints para entrenar un modelo y realizar predicciones con base en los datos ingresados.

## Características

- Entrenamiento de un modelo de regresión lineal.
- Predicción de valores utilizando datos previamente entrenados.
- Organización modular para facilitar el mantenimiento y la escalabilidad.

---

## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

- Python 3.8 o superior
- [Poetry](https://python-poetry.org/) para la gestión de dependencias

---

## Instalación

1. Clona el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/regresion-lineal-api.git
    cd regresion-lineal-api
    ```

2. Inicializa el proyecto con **Poetry**:
    ```bash
    poetry install
    ```

3. Activa el entorno virtual:
    ```bash
    poetry shell
    ```

4. Inicia el servidor de desarrollo:
    ```bash
    uvicorn app.main:app --reload
    ```

El servidor estará disponible en: [http://localhost:8001](http://localhost:8001)

---

## Uso

### Endpoints Principales

1. **Entrenar el modelo**  
   **POST** `/train`  
   Envía datos para entrenar el modelo.  

   **Cuerpo del JSON:**
   ```json
   {
       "data": [
           {
               "Precio": 100.0,
               "Marketing": 200.0,
               "Descuento": 10.0,
               "Ventas": 300.0
           },
           {
               "Precio": 120.0,
               "Marketing": 220.0,
               "Descuento": 15.0,
               "Ventas": 350.0
           }
       ]
   }

2. **Usar el modelo**  
   **POST** `/predict`  
   Envía datos para usar el modelo.

   el modelo Json que se envia es para poder predecir las ventas teniendo en cuenta
   el precio, marketing y descuento que se le pondra al producto.

   el modelo nos devolvera una predición de cuanta ventas se podran obtener.  

   **Cuerpo del JSON:**
   ```json
   {
       "data": [
           {
               "Precio": 100.0,
               "Marketing": 200.0,
               "Descuento": 10.0,
           },
       ]
   }

3. **obtener parametros del modelo**  
   **GET** `/parameters`  
   
  Se utiliza para obtener los parametros del modelo, para de esta manera determinar
  las variables independientes que afectan mayormente sobre la cantidad de ventas
  o del valor de la variable dependiente, de esta forma dictaminar cual de esas variables
  realizar un mayor enfoque.

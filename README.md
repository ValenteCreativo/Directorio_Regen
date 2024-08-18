# Directorio de Ecotecnias

Este repositorio contiene una serie de herramientas y aplicaciones para crear un directorio de proveedores de ecotecnias y organizaciones en México y América Latina. El objetivo es facilitar la búsqueda de tecnologías regenerativas para la transformación de la vida urbana hacia un modelo más sostenible.

Esta iniciativa es parte del proyecto Urbanika [ https://urbanika.notion.site/Urbanika-304277770b0e418ea279548983c3c0db ] para crear una red nacional y regional de proveedores confiables de Ecotecnias. 

## Contenidos

1. **`DatosScraper.py`**
   - Script de web scraping en Python para extraer datos del portal [https://ecotec.unam.mx/ecoteca-inicio/directorio-organizaciones-ecotecnias] .
   - Requiere las librerías `requests`, `beautifulsoup4` y `csv`.
   - **Imagen**: ![¡Script Procesando datos! ]<img width="1275" alt="ScrapingDatos" src="https://github.com/user-attachments/assets/893a283c-a1d5-4e1b-ba93-abb6ea79d009">


2. **`Directorio.py`**
   - Aplicación web desarrollada con Dash y Plotly para visualizar el directorio.
   - Permite filtrar y buscar proveedores por categoría.
   - Requiere las librerías `dash`, `pandas` y `plotly`.
   - **Imagen**: ![Página Principal de directorio]<img width="1440" alt="DirectorioPrincipal" src="https://github.com/user-attachments/assets/35b103e1-a825-45a7-b77a-d55e8abdc211">
   - **Imagen**: ![Página Categorias de directorio]<img width="1423" alt="DirectorioCategorias1" src="https://github.com/user-attachments/assets/d98e3126-778d-4ee8-89d9-c721e79649a4">


3. **`Directorio3D.py`**
   - Visualización 3D (prueba) de los datos utilizando Plotly.
   - Requiere las librerías `dash`, `pandas` y `plotly`.
   - **Imagen**: ![Visualizador en 3D de datos del CSV]<img width="1415" alt="Ecotecnias3D" src="https://github.com/user-attachments/assets/75bca48e-bd2d-497b-a236-6ad952ef07da">

4. **`data/PortalAmbiental.CSV`**
   - Archivo CSV generado a partir del scraping con datos de proveedores y organizaciones.
   - **Imagen**: ![Ejemplo Lista en CSV generada con el Script]<img width="752" alt="EjemploListaEcotecnias" src="https://github.com/user-attachments/assets/9dd1dc00-61f9-4826-a6a5-49a6e0d23083">


## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

´bash
pip install 

## librerias
beautifulsoup4
dash
pandas
plotly

## Contribuciones
Este proyecto está en sus primeras etapas y está destinado a ser una herramienta útil para la comunidad. Si tienes sugerencias o mejoras, no dudes en contribuir.

## Contacto
Para más información, ¡mis correos están abiertos! geovalente@proton.me (mailto:geovalente@proton.me) .


## Nota: Este repositorio es parte de la misión de Urbanika para transformar las ciudades en comunidades regenerativas.

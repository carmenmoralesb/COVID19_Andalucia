# Andalucía COVID Dashboard
## _Proyecto de fin de ciclo de DAW_ 

[![N|Solid](https://www.djangoproject.com/m/img/badges/djangomade124x25.gif)](https://nodesource.com/products/nsolid)

Aplicación web realizada para el trabajo de fin de ciclo de Desarrollo de Aplicaciones Web sobre la evolución del COVID en Andalucía.

- Visualización de datos con Chart.js
- Mapeo y tratamiento de datos con Pandas
- HTML5,CSS3, Javascript
- SQL (PostgreSQL)

## Tecnologías utilizadas
Este proyecto utiliza:

- [Django Framework] - The web framework for perfectionists with deadlines. 
- [Twitter Bootstrap] - Great UI boilerplate for modern web apps
- [PostgreSQL] - PostgreSQL: The world's most advanced open source database
- [Pandas] - Fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language
- [Charts.js] - Open source HTML5 Charts for your website
- [jQuery] -  a lightweight, "write less, do more", JavaScript library.

## Instalación en local
**Instalar las dependencias.**
```
pip install -r requirements.txt 
```

**Actualizar los datos**

```
python .\manage.py get_acumulated --territorio [parámetro]
```
Ejemplos de uso 
```
python .\manage.py get_acumulated --territorio -all  # Datos acumulados de Andalucía
python .\manage.py get_acumulated --territorio -mun  # Datos acumulados de municipios
python .\manage.py get_acumulated --territorio -pro  # Datos acumulados de provincias
```

**Obtener el histórico de datos del COVID19 en Andalucía**
```
python .\manage.py get_historic   
```

## Instalación con docker

```
docker-compose up -d --build
```
Ir a http://localhost:8000

La migración y la creación de los modelos se hace automáticamente

## Fuentes de los datos
Los datos recogidos en esta aplicación web son de uso público y de fuentes oficiales.
- Datos de @Pakillo19 - https://github.com/Pakillo/COVID19-Andalucia/blob/master/datos/
- IECA - https://www.juntadeandalucia.es/institutodeestadisticaycartografia/salud/

## License
[MIT](https://choosealicense.com/licenses/mit/)
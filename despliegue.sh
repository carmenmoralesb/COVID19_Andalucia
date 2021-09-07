# Recopilar ficheros estáticos
docker-compose exec web python3 manage.py collectstatic
# Añadimos los territorios de Andalucía
docker-compose exec web python3 manage.py set_territories
# Añadimos los históricos
docker-compose exec web python3 manage.py get_historic
# Añadimos los acumulados de provincias
docker-compose exec web python3 manage.py get_acumulated --territorio -pro
# Añadimos los acumulados de toda la región
docker-compose exec web python3 manage.py get_acumulated --territorio -all
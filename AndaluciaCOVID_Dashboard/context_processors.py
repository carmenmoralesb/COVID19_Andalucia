from .models import *

def getAllTerritories(request):
    return {'territories': Township.objects.all()} 
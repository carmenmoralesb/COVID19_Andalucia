from .models import *

def getAllTerritories(request):
    return {'territories': Township.objects.all()} 


def getDetailName(request):
    path = request.get_full_path()
    primary = list(filter(str.isdigit, str(path)))
    primaryKey = ''.join(map(str, primary))
    territoryName = ""
    print(primary)

    if ('provincia/detail' in path):
        territoryName = Province.objects.all().filter(pk=primaryKey)[0].name
    elif ('municipio/detail'  in path):
        territoryName = Township.objects.all().filter(pk=primaryKey)[0].name
    else:
        territoryName = "" 
    print(territoryName)
    return {'territoryName': territoryName} 

def getLastUpdate(request):
    return {'date': AcumulatedRegion.objects.all().order_by('-date',)[0].date}     
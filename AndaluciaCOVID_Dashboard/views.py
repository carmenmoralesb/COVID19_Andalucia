from os import name
from django.shortcuts import render
import json
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta, date, datetime
from django.template import loader
from django.http import HttpResponse

# APP VIEWS
def dash_general_view(request):
    dataAument = []
    dataHospitalizedCounter = []
    dataICU = []
    etiquetas1 = []
    etiquetas2 = []
    deceasedList = []
    recoveredList = []
    start = datetime.now() - timedelta(days=14)
    start_dt = start.date()
    end_dt = datetime.now().date()
    queryset2 = AcumulatedRegion.objects.filter(date__range=(start_dt, end_dt))
    count = 0
    size = queryset2.count()

    for register in queryset2:
        if (count == 0):
            regComp = queryset2[0]
        count += 1
        if (count < size):
            regComp = queryset2[count]
            etiquetas2.append(
                str(queryset2[count].date.day) + '/' + str(queryset2[count].date.month))
            etiquetas1.append(
                str(queryset2[count].date.day) + '/' + str(queryset2[count].date.month))
        dataICU.append(regComp.ICU - register.ICU)
        dataHospitalizedCounter.append(
            regComp.Hospitalized - register.Hospitalized - dataICU[count-1])

        dataAument.append(register.aument)
        deceasedList.append(regComp.deceased - register.deceased)
        recoveredList.append(regComp.recovered - register.recovered)

    incid14days = Region.objects.filter(pk=0)[0].tasa14days
    incid7days = Region.objects.filter(pk=0)[0].tasa7days
    deceased = Region.objects.filter(pk=0)[0].deceased
    recovered = Region.objects.filter(pk=0)[0].recovered

    regi1 = AcumulatedRegion.objects.order_by('-date')[0].aument
    regi2 = AcumulatedRegion.objects.order_by('-date')[1].aument

    percentageAument = abs(round((regi1 - regi2)/regi2,2))

    return render(request, 'dash_general_view.html', {
        'labels': etiquetas1,
        'labels2': etiquetas2,
        'dataAument': dataAument,
        'dataHospitalizedCounter': dataHospitalizedCounter,
        'dataICU': dataICU,
        'tasaInc14': incid14days,
        'tasaInc7': incid7days,
        'deceased': deceased,
        'recovered': recovered,
        'deceasedList': deceasedList,
        'recoveredList': recoveredList,
        'percentageAument':percentageAument
    })

def dash_province_view(request):
    provinces = Province.objects.order_by('name')
    etiquetas = []
    provincesIncidence = []
    ICU = []
    deceased = []
    recovered = []
    pcr14days = []
    pcr7days = []
    tasa14dias = []
    recovereList = []
    start = datetime.now() - timedelta(days=14)
    start_dt = start.date()
    end_dt = datetime.now().date()

    for province in provinces:
        registerAcum = AcumulatedProvinces.objects.order_by('-date').filter(province=province,date__range=(start_dt, end_dt))
        hospitalizedProv = []

        if (registerAcum.count()>0):
            etiquetas.append(province.name)
            deceasedToAdd = registerAcum.first().deceased - registerAcum[1].deceased
            recoveredToAdd = registerAcum.first().recovered - registerAcum[1].recovered
            pcr14days.append(registerAcum.first().pcr14days)
            pcr7days.append(registerAcum.first().pcr7days)
            ICU.append(registerAcum.first().ICU  - registerAcum[1].ICU)
            deceased.append(deceasedToAdd)
            recovered.append(recoveredToAdd)
            provincesIncidence.append(registerAcum.first().aument)
            tasa14dias.append(province.tasa14days)    
            recovereList.append(province.recovered)    
       
    return render(request, 'dash_province_view.html', {
        'labels': etiquetas,
        'provincesIncidence': provincesIncidence,
        'UCI':ICU,
        'pcr14days':pcr14days,
        'deceased': deceased,
        'recovered': recovered,
        'tasa14dias':tasa14dias,
        'recovereList':recovereList,
        'provinces':provinces,
        'pcr7days':pcr7days
    })

def dash_province_detail_view(request,pk):
    start = datetime.now() - timedelta(days=14)
    start_dt = start.date()
    end_dt = datetime.now().date()
    province = Province.objects.filter(pk=pk)[0]
    tships = Township.objects.all()
    districts = District.objects.filter(province=province)
    etiquetas = []
    provinceIncidence = []
    dataICU = []
    queryset = AcumulatedProvinces.objects.filter(province=province,date__range=(start_dt, end_dt))
    queryset2 = HistoricProvince.objects.filter(province=province,date__range=(start_dt, end_dt))
    townshipsProv = []
    townships500 = []
    townships1000 = []
    size = queryset.count()
    count = 0
    dataHospitalizedCounter = []
    dataAument = []
    deceasedList = []
    recoveredList = []

    for district in districts:
        for tship in tships:
            if (tship.distrit==district):
                townshipsProv.append(tship)

    for township in townshipsProv:
        if (township.tasa14days >= 500 and township.tasa14days < 1000 ):
           townships500.append(township.name) 
        if (township.tasa14days >= 1000 and township.name not in townships500):
                townships1000.append(township.name)    

    for register in queryset:
        etiquetas.append(str(register.date.day) + '/' + str(register.date.month))
        dataAument.append(register.aument)
        deceasedList.append(register.deceased)
        recoveredList.append(register.recovered)
 
    for register in queryset2:
        dataICU.append(register.ICU)
        dataHospitalizedCounter.append(register.Hospitalized)

    incid14days = province.tasa14days
    incid7days = province.tasa7days
    deceased = province.deceased
    recovered = province.recovered

    regi1 = AcumulatedProvinces.objects.order_by('date')[0]
    regi2 = AcumulatedProvinces.objects.order_by('date')[1]

    return render(request, 'dash_province_detail_view.html', {
        'labels': etiquetas,
        'districts':districts,
        'dataAument': dataAument,
        'dataHospitalizedCounter': dataHospitalizedCounter,
        'dataICU': dataICU,
        'tasaInc14': incid14days,
        'tasaInc7': incid7days,
        'deceased': deceased,
        'recovered': recovered,
        'tships': tships,
        'townships500': townships500,
        'townships1000':townships1000,
        'townships500list': ",".join(townships500),
        'townships1000list': ",".join(townships1000)
    })

def dash_township_detail_view(request,pk):
    start = datetime.now() - timedelta(days=14)
    start_dt = start.date()
    end_dt = datetime.now().date()
    tship = Township.objects.filter(pk=pk)[0]
    etiquetas = []
    queryset = HistoricTownship.objects.order_by('date').filter(township=tship,date__range=(start_dt, end_dt))
    confirmed14days = []
    confirmed14days100hab = []
    deceases = []
    rules = 0
    count = 0
    size = queryset.count()

    for register in queryset:
        if (count == 0):
            regComp = queryset[0]
        count += 1
        if (count < size):
            regComp = queryset[count]
            etiquetas.append(
                str(queryset[count].date.day) + '/' + str(queryset[count].date.month))
        confirmed14days.append(register.Confirmados_PCR_TA_14d)
        confirmed14days100hab.append(register.confirmed14100hab)

    tshipTot1 = queryset[0].totalConfirmed
    tshipTot2 = queryset[1].totalConfirmed

    tshipAument = tshipTot2 - tshipTot1
    tshipIncidence = tship.tasa14days
    confirmedPDIA = tship.confirmedPDIA
    tasa7days = tship.tasa7days
    deceased = queryset[0].deceases
    recovered = tship.deceased

    if (tshipIncidence>=500 and tshipIncidence<=10000):
        rules = 0
    elif (tshipIncidence>=1000):
        rules = 1    
    else:
        rules = 2

    return render(request, 'dash_township_detail_view.html', {
        'labels': etiquetas,
        'confirmed14days':confirmed14days,
        'tshipAument': tshipAument,
        'tshipIncidence':tshipIncidence,
        'confirmed14days100hab':confirmed14days100hab,
        'rules': rules,
        'confirmedPDIA':confirmedPDIA,
        'tasa7days':tasa7days,
        'deceased':deceased,
        'recovered':recovered
    })   

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def question_answers(request):
    return render(request, 'questions_answers.html', {})

def rest_api(request):
    return render(request, 'api.html', {})


# API VIEWS
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Lista de regiones': '/region-list/',
        'Lista de provincias': '/province-list/',
        'Lista de municipios': '/township-list/',
        'Lista de distritos': '/district-list/',
        'Histórico de una provincia': '/province-historic-detail/<str:name>/',
        'Histórico de un municipio': '/township-historic-detail/<str:name>/',
        'Histórico de Andalucía': '/region-historic-detail/',
        'Acumulados en la región': '/region-acumulated-all/',
        'Acumulados en las provincias': '/province-acumulated-all/',
        'Acumulados en los municipios': '/township-acumulated-all/'
    }
    return Response(api_urls)


@api_view(['GET'])
def regionList(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def provinceList(request):
    provinces = Province.objects.all()
    serializer = ProvinceSerializer(provinces, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def districtList(request):
    districts = District.objects.all()
    serializer = DistrictSerializer(districts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def townshipList(request):
    townships = Township.objects.all()
    serializer = TownshipSerializer(townships, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def townshipHistoricDetail(request, pk):
    tship = Township.objects.filter(pk=pk)[0]
    townshipHistorics = HistoricTownship.objects.filter(township=tship).order_by('-date',)
    serializer = TownshipHistoricDetailSerializer(townshipHistorics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def provinceHistoricDetail(request, pk):
    province = Province.objects.filter(pk=pk)[0]
    provinceHistorics = HistoricProvince.objects.filter(province=province).order_by('-date',)
    serializer = ProvinceHistoricDetailSerializer(provinceHistorics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def regionHistoricDetail(request,pk):
    region = Region.objects.filter(pk=pk)[0]
    regionHistorics = HistoricGeneral.objects.filter(cAutonoma=region).order_by('-date',)
    serializer = RegionHistoricDetailSerializer(regionHistorics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def regionAccumulatedAll(request):
    regionAcc = AcumulatedRegion.objects.all().order_by('-date',)
    serializer = RegionAccumulatedSerializer(regionAcc, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def provinceAccumulatedAll(request):
    provinceAcc = AcumulatedProvinces.objects.all().order_by('-date',)
    serializer = ProvincesAccumulatedSerializer(provinceAcc, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def regionAccumulatedDetail(request, pk):
    region = Region.objects.filter(pk=pk)[0]
    regionAcc = AcumulatedRegion.objects.filter(ccaa=region).order_by('-date',)
    serializer = RegionAccumulatedSerializer(regionAcc, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def provinceAccumulatedDetail(request, pk):
    prov = Province.objects.filter(pk=pk)[0]
    provAcc = AcumulatedProvinces.objects.filter(province=prov).order_by('-date',)
    serializer = ProvincesAccumulatedSerializer(prov, many=True)
    return Response(serializer.data)

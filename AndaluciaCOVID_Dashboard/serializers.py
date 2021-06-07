from rest_framework import serializers

from .models import *

class ProvinceSerializer(serializers.ModelSerializer):
    regionNombre = serializers.CharField(source='ccaa.name')
    regionId = serializers.IntegerField(source='ccaa.pk')
    nombreProvincia = serializers.CharField(source='name')
    poblacion = serializers.IntegerField(source='poblation')
    confirmadosTotales = serializers.IntegerField(source='totalConfirmed')
    confirmadosPDIA = serializers.IntegerField(source='confirmedPDIA')
    fallecidos = serializers.IntegerField(source='deceased')
    curados = serializers.IntegerField(source='recovered')
    incidencia14dias = serializers.IntegerField(source='tasa14days')
    incidencia7dias = serializers.IntegerField(source='tasa7days')   
    class Meta:
        model = Province
        fields = ('id', 'nombreProvincia', 'regionNombre','regionId','poblacion',
        'confirmadosPDIA','confirmadosTotales','incidencia14dias',
        'incidencia7dias','fallecidos','curados')      


class TownshipSerializer(serializers.ModelSerializer):
    nombreMunicipio = serializers.CharField(source='name')
    distritoNombre = serializers.CharField(source='distrit.name')
    distritoId = serializers.IntegerField(source='distrit.pk')
    confirmadosTotales = serializers.IntegerField(source='totalConfirmed')
    confirmadosPDIA = serializers.IntegerField(source='confirmedPDIA')
    fallecidos = serializers.IntegerField(source='deceased')
    curados = serializers.IntegerField(source='recovered')
    incidencia14dias = serializers.IntegerField(source='tasa14days')
    incidencia7dias = serializers.IntegerField(source='tasa7days')
    class Meta:
        model = Township
        fields = ('id', 'nombreMunicipio', 'distritoNombre','distritoId','confirmadosTotales',
        'confirmadosPDIA','incidencia14dias','incidencia7dias','fallecidos','curados')      

class DistrictSerializer(serializers.ModelSerializer):
    provinciaNombre = serializers.CharField(source = 'province.name')
    provinciaId = serializers.IntegerField(source = 'province.pk')
    nombreDistrito = serializers.CharField(source = 'name')
    class Meta:
        model = District
        fields = ('id', 'nombreDistrito', 'provinciaNombre','provinciaId')      

class RegionSerializer(serializers.ModelSerializer):
    nombreRegion = serializers.CharField(source='name')
    poblacion = serializers.IntegerField(source='poblation')
    confirmadosTotales = serializers.IntegerField(source='totalConfirmed')
    confirmadosPDIA = serializers.IntegerField(source='confirmedPDIA')
    fallecidos = serializers.IntegerField(source='deceased')
    curados = serializers.IntegerField(source='recovered')
    incidencia14dias = serializers.IntegerField(source='tasa14days')
    incidencia7dias = serializers.IntegerField(source='tasa7days')

    class Meta:
        model = District
        fields = ('id', 'nombreRegion', 'poblacion','confirmadosPDIA',
        'confirmadosTotales','incidencia14dias',
        'incidencia7dias','fallecidos','curados')                

class TownshipHistoricDetailSerializer(serializers.ModelSerializer):
    municipioNombre = serializers.CharField(source='township.name')
    municipioId = serializers.IntegerField(source='township.pk')
    timestamp = serializers.DateField(source='date')
    confirmadosPCR14dias = serializers.IntegerField(source='Confirmados_PCR_TA_14d')
    confirmadosTotales = serializers.IntegerField(source='totalConfirmed')
    fallecidos = serializers.IntegerField(source='deceases')

    class Meta:
        model = HistoricTownship
        fields = ('id','timestamp','municipioNombre','municipioId',
        'confirmadosPCR14dias','confirmadosTotales','fallecidos')           

class RegionHistoricDetailSerializer(serializers.ModelSerializer):
    regionNombre = serializers.CharField(source='cAutonoma.name')
    regionId = serializers.IntegerField(source='cAutonoma.pk')
    timestamp = serializers.DateField(source='date')
    confirmadosPDIA = serializers.IntegerField(source='confirmedPDIA')
    confirmadosTotales = serializers.IntegerField(source='totalConfirmed')
    Hospitalizados = serializers.IntegerField(source='Hospitalized')
    totalICU = serializers.IntegerField(source='ICU')
    fallecidos = serializers.IntegerField(source='deceased')

    class Meta:
        model = HistoricGeneral
        fields = ('id', 'timestamp', 'regionNombre', 'regionId',
        'confirmadosPDIA', 'confirmadosTotales', 
        'Hospitalizados','totalICU','fallecidos')          

class ProvinceHistoricDetailSerializer(serializers.ModelSerializer):
    provinciaNombre = serializers.CharField(source = 'province.name')
    provinciaId = serializers.IntegerField(source = 'province.pk')
    timestamp = serializers.DateField(source='date')
    confirmadosPDIA = serializers.IntegerField(source='confirmedPDIA')
    confirmadosTotales = serializers.IntegerField(source='totalConfirmed')
    Hospitalizados = serializers.IntegerField(source='Hospitalized')
    Fallecidos = serializers.IntegerField(source='deceased')
    totalUCI = serializers.IntegerField(source='ICU')

    class Meta:
        model = HistoricProvince
        fields = ('id', 'timestamp', 'provinciaNombre','provinciaId','confirmadosPDIA', 
        'confirmadosTotales', 'Hospitalizados','totalUCI','Fallecidos')          

class RegionAccumulatedSerializer(serializers.ModelSerializer):
    regionNombre = serializers.CharField(source='ccaa.name')
    regionId = serializers.IntegerField(source='ccaa.pk')
    confirmadosPDIA = serializers.IntegerField(source = 'confirmedPDIA')
    aumento = serializers.IntegerField(source = 'aument')
    pcrPositivas14dias = serializers.IntegerField(source = 'pcr14days')
    pcrPositivas7dias = serializers.IntegerField(source = 'pcr7days')
    confirmadosTotales = serializers.IntegerField(source = 'totalConfirmed')
    totalHospitalizados = serializers.IntegerField(source = 'Hospitalized')
    totalUCI = serializers.IntegerField(source = 'ICU')
    totalFallecidos = serializers.IntegerField(source = 'deceased')
    totalRecuperados = serializers.IntegerField(source = 'recovered')
    timestamp = serializers.DateField(source = 'date')
    class Meta:
        model = AcumulatedRegion
        fields = ('id', 'timestamp', 'regionNombre','regionId', 'confirmadosPDIA', 
        'aumento', 'pcrPositivas14dias','pcrPositivas7dias','confirmadosTotales',
        'totalHospitalizados','totalUCI','totalFallecidos','totalRecuperados')

class ProvincesAccumulatedSerializer(serializers.ModelSerializer):
    provinciaNombre = serializers.CharField(source = 'province.name')
    provinciaId = serializers.IntegerField(source = 'province.pk')
    confirmadosPDIA = serializers.IntegerField(source = 'confirmedPDIA')
    aumento = serializers.IntegerField(source = 'aument')
    pcrPositivas14dias = serializers.IntegerField(source = 'pcr14days')
    pcrPositivas7dias = serializers.IntegerField(source = 'pcr7days')
    totalConfirmados = serializers.IntegerField(source = 'totalConfirmed')
    totalHospitalizados = serializers.IntegerField(source = 'Hospitalized')
    totalUCI = serializers.IntegerField(source = 'ICU')
    totalFallecidos = serializers.IntegerField(source = 'deceased')
    totalRecuperados = serializers.IntegerField(source = 'recovered')
    timestamp = serializers.DateField(source = 'date')

    class Meta:
        model = AcumulatedProvinces
        fields = ('id', 'timestamp', 'provinciaNombre', 'provinciaId','confirmadosPDIA', 'aumento', 
        'pcrPositivas14dias','pcrPositivas7dias','totalConfirmados','totalHospitalizados',
        'totalUCI','totalFallecidos','totalRecuperados')          
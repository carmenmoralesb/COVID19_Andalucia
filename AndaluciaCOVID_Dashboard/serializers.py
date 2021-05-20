from rest_framework import serializers

from .models import *

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class TownshipSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='distrit.name')
    class Meta:
        model = Township
        fields = ('id', 'name', 'district_name')      

class DistrictSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(source='province.name')
    class Meta:
        model = District
        fields = ('id', 'name', 'province_name')          

class TownshipHistoricDetailSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='distr.name')
    class Meta:
        model = HistoricTownship
        fields = ('id', 'date', 'district_name', 'confirmedPDIA', 'totalConfirmed', 'Hospitalized','ICU','deceased')           

class RegionHistoricDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricGeneral
        fields = ('id', 'date', 'cAutonoma', 'confirmedPDIA', 'totalConfirmed', 'Hospitalized','ICU','deceased')          

class ProvinceHistoricDetailSerializer(serializers.ModelSerializer):
    province_name = serializers.CharField(source='province.name')
    class Meta:
        model = HistoricProvince
        fields = ('id', 'date', 'province_name', 'confirmedPDIA', 'totalConfirmed', 'Hospitalized','ICU','deceased')          

class RegionAccumulatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcumulatedRegion
        fields = ('id', 'date', 'ccaa', 'confirmedPDIA', 'aument', 'pcr14days','pcr7days','totalConfirmed','Hospitalized','ICU','deceased','recovered')

class ProvinceAccumulatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcumulatedProvinces
        fields = ('id', 'date', 'ccaa', 'confirmedPDIA', 'aument', 'pcr14days','pcr7days','totalConfirmed','Hospitalized','ICU','deceased','recovered')          
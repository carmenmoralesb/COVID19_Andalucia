from django.contrib import admin
from .models import *

@admin.register(Region)
class Region(admin.ModelAdmin):
    list_display = ("id", "name","confirmedPDIA","totalConfirmed","tasa14days","tasa7days","deceased")    

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("id", "name","confirmedPDIA","totalConfirmed","tasa14days","tasa7days","deceased")    
    

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name","get_province")
    list_filter = ("province__name", )
    def get_province(self, obj):
        return obj.province.name

@admin.register(Township)
class TownShiptAdmin(admin.ModelAdmin):
    list_display = ("id", "name","get_distrit","confirmedPDIA","totalConfirmed","tasa14days","tasa7days","deceased")    
    list_filter = ("distrit__name", )
    def get_distrit(self, obj):
        return obj.distrit.name

@admin.register(HistoricDistrit)
class HistoricDistrictAdmin(admin.ModelAdmin):
    list_display = ("date", "get_distr","Confirmados_PCR_TA","Confirmados_PCR_TA_14d","confirmed14100hab","totalConfirmed","deceases")
    list_filter = ("distr__name", )
    def get_distr(self, obj):
        return obj.distr.name

@admin.register(HistoricTownship)
class HistoricTownshipAdmin(admin.ModelAdmin):
    list_display = ("date", "get_township","Confirmados_PCR_TA","Confirmados_PCR_TA_14d","confirmed14100hab","totalConfirmed","deceases")
    list_filter = ("township__name", )
    def get_township(self, obj):
        return obj.township.name


@admin.register(HistoricProvince)
class HistoricProvinceAdmin(admin.ModelAdmin):
    list_display = ("date", "get_province","confirmedPDIA","totalConfirmed","Hospitalized","ICU","deceased")
    list_filter = ("province__name", )
    def get_province(self, obj):
        return obj.province.name

@admin.register(HistoricGeneral)
class HistoricGeneralAdmin(admin.ModelAdmin):
    list_display = ("date", "cAutonoma","confirmedPDIA","totalConfirmed","Hospitalized","ICU","deceased")

@admin.register(AcumulatedProvinces)
class AccumulatedProvincesAdmin(admin.ModelAdmin):
    list_display = ("date", "get_province","confirmedPDIA","totalConfirmed","Hospitalized","ICU","deceased","aument")
    list_filter = ("province__name", )
    def get_province(self, obj):
        return obj.province.name

@admin.register(AcumulatedRegion)
class AccumulatedRegionsAdmin(admin.ModelAdmin):
    list_display = ("date", "ccaa","confirmedPDIA","totalConfirmed","Hospitalized","ICU","deceased","recovered","aument","pcr7days","pcr14days")
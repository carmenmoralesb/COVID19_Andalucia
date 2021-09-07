from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import *
import pandas as pd
import numpy as np
from datetime import timedelta, date, datetime
from django.core.management.base import BaseCommand

class ModelsTestCase(TestCase):
    def test_hierarchy(self):
        """Foreign key is properly in save data"""
        region =   Region.objects.create(pk=0,name="Andalucía")
        province = Province.objects.create(pk=0,name="Cádiz",ccaa=region)
        district = District.objects.create(pk=0,name="Bahía de Cádiz-La Janda", province=province)
        township = Township.objects.create(pk=0,name="San Fernando", distrit=district)
        
        region.save()
        province.save()
        district.save()
        township.save()

        self.assertEqual(township.distrit, district)

    def test_scrapping(self):
        """Scrapping is properly done"""
        region = Region.objects.create(pk=0,name="Andalucía")
        province = Province.objects.create(pk=0,name="Cádiz",ccaa=region)

        region.save()
        province.save()

        directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/municipios.dia/Municipios_todos_datoshoy.csv'
        
        df = pd.read_csv(directory, delimiter=";")
        df.replace(np.NaN, 0, inplace=True)
        df = df.iloc[1:]

        listRegister = []

        for listaDatos in (df[df["Lugar de residencia"] == province.name].values):
            listData = listaDatos.tolist()
            listRegister.append(listData[2])
        if (listRegister[4]==0):
            valtasa14 = 0
        else:
            valtasa14 = int(listRegister[4].split(",")[0])
        if (listRegister[6]==0):
            valtasa7 = 0
        else:
            valtasa7 = int(listRegister[6].split(",")[0])  

        province.poblation = int(listRegister[0])   
        province.confirmedPDIA = int(listRegister[1])   
        province.tasa14days = valtasa14
        province.tasa7days = valtasa7
        province.totalConfirmed = int(listRegister[7])
        province.deceased = int(listRegister[10])
        province.recovered = int(listRegister[9])
        province.save()    

        self.assertEqual(province.tasa7days, valtasa7)

    def cannot_have_two_register_with_same_id(self):
        """Cannot save register with same id"""
        with self.assertRaises(TypeError):
            township1 = Township.objects.create(pk=0,name="San Fernando", distrit=district)
            township2 = Township.objects.create(pk=0,name="Puerto Real", distrit=district)
            township1.save()    
            township2.save()

    def cannot_violate_constraint_unique(self):
        """Cannot violate unique constraints"""
        with self.assertRaises(TypeError):
            date =  datetime.now() 
            dateDF = date.strftime('%d/%m/%Y')

            newRegisterAccumulated1 = AcumulatedProvinces(
                province='Cádiz',
                date=date,
                confirmedPDIA=0,
                aument=0,
                pcr14days=0,
                pcr7days=0,
                totalConfirmed=0,
                Hospitalized=0,
                ICU=0,
                deceased=0,
                recovered=0)        
            
            newRegisterAccumulated2 = AcumulatedProvinces(
                province='Cádiz',
                date=date,
                confirmedPDIA=0,
                aument=0,
                pcr14days=0,
                pcr7days=0,
                totalConfirmed=0,
                Hospitalized=0,
                ICU=0,
                deceased=0,
                recovered=0) 

            newRegisterAccumulated1.save()
            newRegisterAccumulated2.save()

    def cannot_violate_constraint_unique_reg(self):
         """Cannot violate unique constraint in accumulated"""       
        region = Region.objects.create(pk=0,name="Andalucía")
        region.save()

        with self.assertRaises(TypeError):
            date =  datetime.now() 
            dateDF = date.strftime('%d/%m/%Y')

            newRegisterAccumulated1 = AcumulatedRegion(
                ccaa=region,
                date=date,
                confirmedPDIA=0,
                aument=0,
                pcr14days=0,
                pcr7days=0,
                totalConfirmed=0,
                Hospitalized=0,
                ICU=0,
                deceased=0,
                recovered=0)

            newRegisterAccumulated2 = AcumulatedRegion(
                ccaa=region,
                date=date,
                confirmedPDIA=0,
                aument=0,
                pcr14days=0,
                pcr7days=0,
                totalConfirmed=0,
                Hospitalized=0,
                ICU=0,
                deceased=0,
                recovered=0)

            newRegisterAccumulated1.save()
            newRegisterAccumulated2.save()

class ViewsTestCase(TestCase):
    def api_loads_properly_town(self):
        """The API page loads properly in list township"""
        response = self.client.get('http://localhost:1337/api/municipio-lista?format=json')
        self.assertEqual(response.status_code, 200)  

    def api_loads_properly_prov(self):
        """The API page loads properly with province list"""
        response = self.client.get('http://localhost:1337/api/provincia-lista?format=json')
        self.assertEqual(response.status_code, 200)                       
    
    def api_loads_properly_detail(self):
        """The API page loads properly with acumulated detail"""
        response = self.client.get('http://localhost:1337/api/region-acumulado-detalle/1?format=json')
        self.assertEqual(response.status_code, 200)                 

    def api_loads_properly_detail(self):
        """The API page loads properly with an error"""
        response = self.client.get('http://localhost:1337/api/region-acumulado-detalle/35256363?format=json')
        self.assertEqual(response.status_code, 500)           
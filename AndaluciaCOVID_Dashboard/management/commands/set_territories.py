import pandas as pd
import numpy as np
import datetime
from django.core.management.base import BaseCommand

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'COVID19_Andalucia.settings')
django.setup()
from AndaluciaCOVID_Dashboard.models import *

class Command(BaseCommand):
    help = 'Use this command to populate de DB automatically'

    def setRegions(self):
        directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/municipios.dia/Municipios_todos_datoshoy.csv'
        df = pd.read_csv(directory, delimiter=";")
        df.replace(np.NaN, 0, inplace=True)
        listRegister = []
        try:
            for listaDatos in (df[df["Lugar de residencia"] == "Andalucía"].values):
                listData = listaDatos.tolist()
                listRegister.append(listData[2])
            print(listRegister)
            if (listRegister[4]==0):
                valtasa14 = 0
            else:
                valtasa14 = int(listRegister[4].split(",")[0])
            if (listRegister[6]==0):
                valtasa7 = 0
            else:
                valtasa7 = int(listRegister[6].split(",")[0])  

            if (Region.objects.all().filter(id=0).count()==0):            
                region = Region(
                    id=0,
                    name="Andalucía",
                    poblation = int(listRegister[0]), 
                    confirmedPDIA = int(listRegister[1]),
                    tasa14days = valtasa14,
                    tasa7days = valtasa7,
                    totalConfirmed = int(listRegister[7]),
                    deceased = int(listRegister[10]),
                    recovered = int(listRegister[9]))
                region.save() 
            else:
               regionUpdating = Region.objects.all().filter(id=0)[0]  
               regionUpdating.confirmedPDIA = int(listRegister[1])
               regionUpdating.tasa14days = valtasa14
               regionUpdating.tasa7days = valtasa7
               regionUpdating.totalConfirmed = int(listRegister[7])
               regionUpdating.deceased = int(listRegister[10])
               regionUpdating.recovered = int(listRegister[9])
               regionUpdating.save() 
        except IndexError as e:
            print(e)


    def getProvinces(self):
        """ 
        Migrar a la base de datos las provincias,municipios y distritos de Andalucía
        """
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/muni_prov_dist.csv'
            df = pd.read_csv(directory, delimiter=",", names=[
                'province', 'distrit', 'township'])
            df.drop(df.index[[0, 2]])
            for prov in df.province:
                print(prov)
                if (Province.objects.filter(name=prov).exists() == False):
                    region = Region.objects.all()[0]
                    province = Province(name=prov,ccaa=Region(id=0,name="Andalucía"))
                    province.save()
        except IndexError as e:
            print(e)

    def getDistrFromProv(self):
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/muni_prov_dist.csv'
            df = pd.read_csv(directory, delimiter=",", names=[
                'province', 'distrit', 'township'])
            provinces = Province.objects.all()
            for province in provinces:
                for distr in df[df.province == province.name].distrit:
                    if (District.objects.filter(name=distr).exists() == False):
                        distr = District(name=distr, province=province)
                        distr.save()

        except IndexError as e:
            print(e)

    def getTownShipFromDistr(self):
        try:            
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/muni_prov_dist.csv'
            df = pd.read_csv(directory, delimiter=",", names=[
                'province', 'distrit', 'township'])
            df.drop(df.index[[0, 2]])
            districts = District.objects.all()
            for district in districts:
                for ts in df[df.distrit == district.name].township:
                    if (Township.objects.filter(name=ts).exists() == False):
                        township = Township(name=ts, distrit=district)
                        township.save()
        except IndexError as e:
            print(e)

    def getTshipData(self, munName):
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/municipios.dia/Municipios_todos_datoshoy.csv'
            df = pd.read_csv(directory, delimiter=";")
            df.replace(np.NaN, 0, inplace=True)
            df = df.iloc[1:]
            tship = Township.objects.filter(name=munName)[0]
            listRegister = []

            for listaDatos in (df[df["Lugar de residencia"] == tship.name].values):
                listData = listaDatos.tolist()
                listRegister.append(listData[2])
            print(listRegister)
            if (listRegister[4]==0):
                valtasa14 = 0
            else:
                valtasa14 = int(listRegister[4].split(",")[0])
            if (listRegister[5]==0):
                valtasa7 = 0
            else:
                valtasa7 = int(listRegister[5].split(",")[0])  

            tship.poblation = int(listRegister[0])   
            tship.confirmedPDIA = int(listRegister[1])   
            tship.tasa14days = valtasa14
            tship.tasa7days = valtasa7
            tship.totalConfirmed = int(listRegister[7])
            tship.deceased = int(listRegister[9])
            tship.recovered = int(listRegister[10])
            tship.save()                    
        except IndexError as e:
            print(e)    

    def getProvinceData(self, provName):
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/municipios.dia/Municipios_todos_datoshoy.csv'
            df = pd.read_csv(directory, delimiter=";")
            df.replace(np.NaN, 0, inplace=True)
            df = df.iloc[1:]
            province = Province.objects.filter(name=provName)[0]
            listRegister = []

            for listaDatos in (df[df["Lugar de residencia"] == province.name].values):
                listData = listaDatos.tolist()
                listRegister.append(listData[2])
            print(listRegister)
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
        except IndexError as e:
            print(e)     

    def handle(self, *args, **options):
        print('Adding region...')
        self.setRegions()
        print('Adding provinces...')
        self.getProvinces()
        print('Adding distrits...')
        self.getDistrFromProv()
        print('Adding townships...')
        self.getTownShipFromDistr()

        townships = Township.objects.all()
        provinces = Province.objects.all()
      
        for township in townships:
            self.getTshipData(township.name)   
        for prov in provinces:
            self.getProvinceData(prov.name)               
        print('...MIGRATION SUCCESFUL!')

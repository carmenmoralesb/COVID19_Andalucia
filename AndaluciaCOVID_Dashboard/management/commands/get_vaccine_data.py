from django.core.management.base import BaseCommand
from AndaluciaCOVID_Dashboard.models import *
import pandas as pd
import numpy as np
import datetime
import requests
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'COVID19_Andalucia.settings')
django.setup()


class Command(BaseCommand):
    help = 'Use this command to populate de DB automatically'

    def getVaccineData(self):
        downloadCSV()
        directory = 'datos/vacunacion/vacuna.csv'
        df = pd.read_csv(directory, delimiter=";")
        df.replace(np.NaN, 0, inplace=True)
        listRegister = []
        try:
            for listaDatos in (df[df["Lugar de residencia"] == "Andalucía"].values):
                listData = listaDatos.tolist()
                listRegister.append(listData[2])
            print(listRegister)
            if (listRegister[4] == 0):
                valtasa14 = 0
            else:
                valtasa14 = int(listRegister[4].split(",")[0])
            if (listRegister[6] == 0):
                valtasa7 = 0
            else:
                valtasa7 = int(listRegister[6].split(",")[0])

            if (Region.objects.all().filter(id=0).count() == 0):
                region = Region(
                    id=0,
                    name="Andalucía",
                    poblation=int(listRegister[0]),
                    confirmedPDIA=int(listRegister[1]),
                    tasa14days=valtasa14,
                    tasa7days=valtasa7,
                    totalConfirmed=int(listRegister[7]),
                    deceased=int(listRegister[10]),
                    recovered=int(listRegister[9]))
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

    def downloadCSV(self):
        """ 
        Descargar el CSV del reporte diario de vacunación
        """
        try:
            csv_url = 'https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/stpivot/stpivot/Print?cube=357f49a7-3ec6-4b8e-92a6-7de39bcfb237&type=3&foto=si&ejecutaDesde=&codConsulta=53530&consTipoVisua=JP'
            req = requests.get(csv_url)
            csv_file = open('datos/vacunacion/vacunaTipos.csv', 'wb')
            csv_file.close()

            csv_url = 'https://www.juntadeandalucia.es/institutodeestadisticaycartografia/badea/stpivot/stpivot/Print?cube=357f49a7-3ec6-4b8e-92a6-7de39bcfb237&type=3&foto=si&ejecutaDesde=&codConsulta=53530&consTipoVisua=JP'
            req = requests.get(csv_url)
            csv_file = open('datos/vacunacion/vacunaTipos.csv', 'wb')
            csv_file.close()
        except IndexError as e:
            print(e)

    def handle(self, *args, **options):
        print('Obteniendo datos de vacunación...')
        self.getVaccineData()
        print('...MIGRATION SUCCESFUL!')

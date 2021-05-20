import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'COVID19_Andalucia.settings')
django.setup()
from AndaluciaCOVID_Dashboard.models import *

class Command(BaseCommand):
    help = 'Use this command to retrieve up-to-date data of COVID19 from IECA'

    def updateHistoricProvince(self):
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/datos_provincias_clean.csv'
            df = pd.read_csv(directory, delimiter=",", names=[
                'fdiag', 'prov', 'pcrConfirmed','totalConfirmed','hospitalized','ICU','deceased'])
            df.drop(df.index[[0, 1]])
            provinces = Province.objects.all()

            for prov in provinces:
                for row in (df[df["prov"] == prov.name].values):
                    province = Province.objects.filter(name=row[1])
                    ifExists = HistoricProvince.objects.filter(date=row[0],province=province[0])
                    if (ifExists.count()==0):
                        newHistoric = HistoricProvince(date=row[0],
                        province=province[0],
                        confirmedPDIA=int(row[2]),
                        totalConfirmed=int(row[3]),
                        Hospitalized=int(row[4]),
                        ICU=int(row[5]),
                        deceased=int(row[6])
                    )
                        newHistoric.save()
            for row in (df[df["prov"] == 'Andalucía'].values):
                ifExists = HistoricGeneral.objects.filter(date=row[0],cAutonoma=Region.objects.all()[0])
                if (ifExists.count()==0):
                    newHistoricGeneral = HistoricGeneral(date=row[0],
                    cAutonoma=row[1],
                    confirmedPDIA=int(row[2]),
                    totalConfirmed=int(row[3]),
                    Hospitalized=int(row[4]),
                    ICU=int(row[5]),
                    deceased=int(row[6])
                    )
                    newHistoricGeneral.save()

        except IndexError as e:
            print(e)

    def updateHistoricDistrict(self):
        """ 
        Migrar todos los históricos de datos de municipios y distritos a la base de datos
        desde el inicio de la pandemia. Hacerlo SOLO en la primera migración
        """
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/municipios.csv'
            df = pd.read_csv(directory, dtype='unicode', delimiter=",",
                             names=[
                                 'fdiag',
                                 'prov',
                                 'distr',
                                 'township',
                                 'Confirmados_PCR_TA',
                                 'Confirmados_PCR_TA_14d',
                                 'Confirmed14100hab',
                                 'ConfirmadosTotal',
                                 'deceases'])
            df = df.iloc[1:]
            df.replace(np.NaN, 0, inplace=True)
            covid_data = datetime.now() - timedelta(days=14)
            covid_data_df = str(covid_data.date())
            districtList = District.objects.all()
            townshipList = Township.objects.all()

            for distr in districtList:
                for row in (df[df["distr"] == distr.name].values):
                    if (row[0]>=covid_data_df):
                        district = District.objects.filter(name=row[2])
                        ifExists = HistoricDistrit.objects.filter(date=row[0],distr=district[0])
                        if (ifExists.count()==0):
                            print(row)       
                            newHistoricDistrict = HistoricDistrit(date=row[0],
                                                distr=district[0],
                                                Confirmados_PCR_TA=int(row[4]),
                                                Confirmados_PCR_TA_14d=int(row[5]),
                                                confirmed14100hab=int(str(row[6]).split(".")[0]),
                                                totalConfirmed=int(row[7]),
                                                deceases=int(row[8]))
                            newHistoricDistrict.save()
        except IndexError as e:
            print(e)
    
    def setHistoricTownships(self):
        try:
            directory = 'https://raw.githubusercontent.com/Pakillo/COVID19-Andalucia/master/datos/municipios.csv'
            df = pd.read_csv(directory, dtype='unicode', delimiter=",",
                             names=[
                                 'fdiag',
                                 'prov',
                                 'distr',
                                 'township',
                                 'Confirmados_PCR_TA',
                                 'Confirmados_PCR_TA_14d',
                                 'Confirmed14100hab',
                                 'ConfirmadosTotal',
                                 'deceases'])
            df = df.iloc[1:]
            df.replace(np.NaN, 0, inplace=True)
            covid_data = datetime.now() - timedelta(days=14)
            covid_data_df = str(covid_data.date())
            districtList = District.objects.all()
            townshipList = Township.objects.all()         
            for tship in townshipList:
                for row in (df[df["township"] == tship.name].values):
                    if (row[0]>covid_data_df):
                        print(row[0])
                        tshipsel = Township.objects.filter(name=row[3])
                        ifExists = HistoricTownship.objects.filter(date=row[0],township=tshipsel[0])
                        if (ifExists.count()==0):
                            print(row)       
                            newHistoricTownship = HistoricTownship(date=row[0],
                            township=tshipsel[0],
                            Confirmados_PCR_TA=int(row[4]),
                            Confirmados_PCR_TA_14d=int(row[5]),
                            confirmed14100hab=int(str(row[6]).split(".")[0]),
                            totalConfirmed=int(row[7]),
                            deceases=int(row[8]))
                            newHistoricTownship.save()
        except IndexError as e:
            print(e)
  
    def handle(self, *args, **options):
        print('Updating...')
        self.updateHistoricProvince()
        self.updateHistoricDistrict()
        self.setHistoricTownships()
        print('...MIGRATION SUCCESFUL!')

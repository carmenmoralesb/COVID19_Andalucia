from AndaluciaCOVID_Dashboard.models import *
import pandas as pd
import numpy as np
from datetime import timedelta, date, datetime
from django.core.management.base import BaseCommand

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'COVID19_Andalucia.settings')
django.setup()

class Command(BaseCommand):
    help = 'Usa este comando para borrar registros antiguos'

    def deleteOldData(self,date):
        date = date.strftime('%d/%m/%Y')
        try:
            AcumulatedProvinces.objects.filter(date<date).delete()
            AcumulatedRegion.objects.filter(date<date).delete()
            HistoricDistrit.objects.filter(date<date).delete()
            HistoricGeneral.filter(date<date).delete()
            HistoricTownship.filter(date<date).delete()
            HistoricProvince.filter(date<date).delete()
        except IndexError as e:
            print(e)

    def handle(self, *args, **options):
        print('Borrando registros antiguos...')

        start = datetime.now() - timedelta(days=14)
        start_dt = start.date()
        self.deleteOldData(dt)
        print('...Borrado realizado!')

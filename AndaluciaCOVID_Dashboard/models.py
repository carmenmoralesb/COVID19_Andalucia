from django.db import models
# Create your models here.

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="Nombre")
    poblation = models.IntegerField(null=False,verbose_name="Población",default=0)
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    tasa14days = models.IntegerField(null=False,verbose_name="Tasa a 14 días",default=0)
    tasa7days = models.IntegerField(null=False,verbose_name="Tasa a 7 dias",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)
    recovered = models.IntegerField(null=False,verbose_name="Curados",default=0)

    def __unicode__(self):
        return self.name
    class Meta: 
        verbose_name = 'Comunidad Autónoma'

class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="Nombre")
    ccaa = models.ForeignKey(Region, on_delete=models.CASCADE,blank=True, null=True, default=0,verbose_name="CCAA")
    poblation = models.IntegerField(null=False,verbose_name="Población",default=0)
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    tasa14days = models.IntegerField(null=False,verbose_name="Tasa a 14 días",default=0)
    tasa7days = models.IntegerField(null=False,verbose_name="Tasa a 7 dias",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)
    recovered = models.IntegerField(null=False,verbose_name="Curados",default=0)
    def __unicode__(self):
        return self.name
    class Meta: 
        verbose_name = 'Provincia'


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="Nombre")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="Provincia")


    def __unicode__(self):
        return self.name
    class Meta: 
        verbose_name = 'Distrito'

class Township(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name="Nombre",unique=True)
    distrit = models.ForeignKey(District, on_delete=models.CASCADE,verbose_name="Distrito")
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    tasa14days = models.IntegerField(null=False,verbose_name="Tasa a 14 días",default=0)
    tasa7days = models.IntegerField(null=False,verbose_name="Tasa a 7 dias",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)
    recovered = models.IntegerField(null=False,verbose_name="Curados",default=0)
    def __unicode__(self):
        return self.name
    class Meta: 
        verbose_name = 'Municipio'

class HistoricProvince(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100, default="", verbose_name='Fecha de diagnóstico')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name = "Provincia")
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    Hospitalized = models.IntegerField(null=False, verbose_name="Hospitalizados",default=0)
    ICU = models.IntegerField(null=False,verbose_name="UCIS",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'province'], name='CONSTR_NO_REPEAT_REGISTRPROV')
        ]
        verbose_name = 'Histórico de datos por Provincia'


class HistoricDistrit(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100, default="", verbose_name='Fecha de diagnóstico')    
    distr = models.ForeignKey(District, on_delete=models.CASCADE,null=True, verbose_name="Distrito")
    Confirmados_PCR_TA = models.IntegerField(null=False, verbose_name='Confirmados por PCR TOTAL',default=0)
    Confirmados_PCR_TA_14d = models.IntegerField(null=False, verbose_name='Confirmados PCR 14 días',default=0)
    confirmed14100hab =  models.IntegerField(null=False,verbose_name='Confirmados 14 días x 100.000 hab',default=0)
    totalConfirmed = models.IntegerField(null=False, verbose_name='Confirmados totales',default=0)
    deceases = models.IntegerField(null=False, verbose_name='Fallecidos',default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'distr'], name='CONSTR_NO_REPEAT_REGISTRDISTR')
        ]
        verbose_name = 'Histórico de datos por distrito sanitario'

class HistoricTownship(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100, default="", verbose_name='Fecha de diagnóstico')
    township = models.ForeignKey(Township, on_delete=models.CASCADE,null=True, verbose_name='Municipio',default=0)
    Confirmados_PCR_TA = models.IntegerField(null=False, verbose_name='Confirmados por PCR TOTAL',default=0)
    Confirmados_PCR_TA_14d = models.IntegerField(null=False, verbose_name='Confirmados PCR 14 días',default=0)
    confirmed14100hab =  models.IntegerField(null=False,verbose_name='Confirmados 14 días x 100.000 hab',default=0)
    totalConfirmed = models.IntegerField(null=False, verbose_name='Confirmados totales',default=0)
    deceases = models.IntegerField(null=False, verbose_name='Fallecidos',default=0)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'township'], name='CONSTR_NO_REPEAT_REGISTRTOWN')
        ]
        verbose_name = 'Histórico de datos por municipio'

class HistoricGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100)
    cAutonoma = models.CharField(max_length=50,verbose_name="Nombre",default=0)
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    Hospitalized = models.IntegerField(null=False, verbose_name="Hospitalizados",default=0)
    ICU = models.IntegerField(null=False,verbose_name="UCIS",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)
    
    constraints = [
            models.UniqueConstraint(fields=['date', 'cAutonoma'], name='CONSTR_NO_REPEAT_REGISTRCCAA')
        ]
    class Meta:
        verbose_name = 'Histórico de datos en toda la región de Andalucía'

class AcumulatedProvinces(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name = "Provincia")
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    aument = models.IntegerField(null=False,verbose_name="Aumento con el día anterior",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    Hospitalized = models.IntegerField(null=False, verbose_name="Hospitalizados",default=0)
    pcr14days = models.IntegerField(null=False,verbose_name="Confirmados PCR 14 días",default=0)
    pcr7days = models.IntegerField(null=False,verbose_name="Confirmados PCR 7 días",default=0)
    ICU = models.IntegerField(null=False,verbose_name="UCIS",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)
    recovered = models.IntegerField(null=False,verbose_name="Curados",default=0)
    
    constraints = [
            models.UniqueConstraint(fields=['date', 'province'], name='CONSTR_NO_REPEAT_ACUMPROV')
        ]
    class Meta:
        verbose_name = 'Datos acumulados en las provincias de Andalucia'

class AcumulatedRegion(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=100)
    ccaa = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name = "Region")
    confirmedPDIA = models.IntegerField(null=False,verbose_name="Confirmados PDIA",default=0)
    aument = models.IntegerField(null=False,verbose_name="Aumento con el día anterior",default=0)
    totalConfirmed = models.IntegerField(null=False,verbose_name="Total Confirmados",default=0)
    Hospitalized = models.IntegerField(null=False, verbose_name="Hospitalizados",default=0)
    pcr14days = models.IntegerField(null=False,verbose_name="Confirmados PCR 14 días",default=0)
    pcr7days = models.IntegerField(null=False,verbose_name="Confirmados PCR 7 días",default=0)
    ICU = models.IntegerField(null=False,verbose_name="UCIS",default=0)
    deceased = models.IntegerField(null=False,verbose_name="Fallecidos",default=0)
    recovered = models.IntegerField(null=False,verbose_name="Curados",default=0)
    
    constraints = [
            models.UniqueConstraint(fields=['date', 'ccaa'], name='CONSTR_NO_REPEAT_ACUMREG')
        ]
    class Meta:
        verbose_name = 'Datos acumulados en Andalucía'
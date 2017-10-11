from django.db import models

#model field name should be same as form field name
from Hospital_data import settings


class Pdata(models.Model):
    #new field addes
    patientid=models.IntegerField()
    Name = models.CharField(max_length=200)
    DateofBirth = models.DateField(max_length=8)
    Email = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.Name +"  "+self.Address


class Labdata(models.Model):
    patientid = models.ForeignKey(Pdata, on_delete=models.CASCADE)
    BloodGlucoseRange = models.IntegerField(default=0)
    BloodPressure = models.IntegerField(default=0)
    HeartRates = models.IntegerField(default=0)
    SkinThikness=models.FloatField(default=0)
    PragnencyParYear=models.IntegerField(default=0)
    Diabetes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.patientid)+"  "+str(self.Diabetes)
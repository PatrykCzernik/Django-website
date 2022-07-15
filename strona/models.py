from django.db import models

class sqlserverconn(models.Model):
    
    ID_Chorego = models.IntegerField(db_column='ID_Chorego',primary_key=True)
    Płeć = models.CharField(max_length=100)
    Wiek = models.IntegerField()
    BMI = models.IntegerField()
    Typ = models.CharField(max_length=100)
    Srodowisko = models.CharField(max_length=100)



class insertdata(models.Model):
    id =models.IntegerField(db_column='ID_Chorego',primary_key=True)
    plec= models.CharField(max_length=100)
    wiek = models.IntegerField()
    typ_nowotworu = models.CharField(max_length=100)
    id_srodowiska = models.IntegerField()
    bmi = models.IntegerField()
    id_promieniowania = models.IntegerField()
    id_nowotworu = models.IntegerField()

class EmpModel(models.Model):
    ID_Chorego =models.IntegerField(db_column='ID_Chorego',primary_key=True)
    plec= models.CharField(max_length=100)
    wiek = models.IntegerField()
    typ_nowotworu = models.CharField(max_length=100)
    id_srodowiska = models.IntegerField()
    bmi = models.IntegerField()
    id_promieniowania = models.IntegerField()
    Typ_Nowotworu= models.CharField(max_length=100)
   

    class Meta:
      db_table="baza"
    
   



   
    
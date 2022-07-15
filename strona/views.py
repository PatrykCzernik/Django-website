from django.shortcuts import render 
from strona.models import sqlserverconn
from strona.models import insertdata
from strona.models import EmpModel
import pyodbc
from django.db.models import Sum
from django.http import JsonResponse
import mysql.connector
import pymysql

def connsql(request):

    serv= sqlserverconn.objects.raw('SELECT Chorzy.ID_Chorego, Chorzy.Plec,Chorzy.Wiek, Chorzy.BMI, Chorzy.Typ_Nowotworu, Promieniowanie.Dawka, Srodowisko.Nazwa  FROM baza.Chorzy INNER JOIN baza.Promieniowanie ON Chorzy.ID_Promieniowania = Promieniowanie.ID_Promieniowania INNER JOIN baza.Srodowisko  ON Chorzy.ID_Srodowiska = Srodowisko.ID_Srodowiska')

    return render(request,'index.html',{'sqlserverconn':serv})
  
    

def saverecords(request):

    conn22 = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database='baza'
    )
    
    if request.method=="POST":
        if request.POST.get('plec') and request.POST.get('wiek') and request.POST.get('typ_nowotworu') and request.POST.get('id_srodowiska') and request.POST.get('bmi') and request.POST.get('id_promieniowania'):
            insertvalues= insertdata()
            insertvalues.id=request.POST.get('id')
            insertvalues.plec=request.POST.get('plec')
            insertvalues.wiek=request.POST.get('wiek')
            insertvalues.typ_nowotworu=request.POST.get('typ_nowotworu')
            insertvalues.id_srodowiska=request.POST.get('id_srodowiska')
            insertvalues.bmi=request.POST.get('bmi')
            insertvalues.id_promieniowania=request.POST.get('id_promieniowania')
            insertvalues.id_nowotworu=request.POST.get('id_nowotworu')
            cursor5=conn22.cursor()
            cursor5.execute("insert into Chorzy values ('""','"+insertvalues.plec+"','"+insertvalues.wiek+"','"+insertvalues.typ_nowotworu+"','"+insertvalues.id_srodowiska+"','"+insertvalues.bmi+"','"+insertvalues.id_promieniowania+"','"+insertvalues.id_nowotworu+"')")
            #cursor5.execute("insert into Chorzy values ('"+insertvalues.plec+"','"+insertvalues.wiek+"','"+insertvalues.typ_nowotworu+"','"+insertvalues.id_srodowiska+"','"+insertvalues.bmi+"','"+insertvalues.id_promieniowania+"','"+insertvalues.id_nowotworu+"')")

            conn22.commit()
        return render(request,'insert.html')
    else:
        return render(request,'insert.html')

def Multiplesearchemp(request):
    # conn = pyodbc.connect('Driver={sql server};'
    #                       'Server=DESKTOP-O8UBSV2;'
    #                       'Database=baza;'
                          
    #                       'Trusted_Connections=yes;')
    if request.method=="POST":
    
    
        ID_Chorego=request.POST.get('ID_Chorego')
        plec=request.POST.get('plec')
        wiek =request.POST.get('wiek')
        typ_nowotworu=request.POST.get('typ_nowotworu')
        id_srodowiska=request.POST.get('id_srodowiska')
        bmi=request.POST.get('bmi')
        id_promieniowania=request.POST.get('id_promieniowania')
        
        empsearchobj=EmpModel.objects.raw('SELECT Chorzy.ID_Chorego, Chorzy.Plec,Chorzy.Wiek, Chorzy.BMI, Chorzy.Typ_Nowotworu, Chorzy.ID_Nowotworu, Promieniowanie.Dawka, Srodowisko.Nazwa,  Chorzy.ID_Chorego, Chorzy.Plec,Chorzy.Wiek, Chorzy.BMI, Chorzy.Typ_Nowotworu, Chorzy.ID_Nowotworu, Promieniowanie.Dawka, Srodowisko.Nazwa, nowotwor.Objaw  FROM baza.Chorzy INNER JOIN baza.Promieniowanie ON Chorzy.ID_Promieniowania = Promieniowanie.ID_Promieniowania INNER JOIN baza.Srodowisko  ON Chorzy.ID_Srodowiska = Srodowisko.ID_Srodowiska INNER JOIN baza.nowotwor ON Chorzy.ID_Nowotworu = nowotwor.ID_Nowotworu where  Chorzy.Typ_Nowotworu="'+typ_nowotworu+'"')  
        
  
        return render(request,'search.html',{"sqlserverconn":empsearchobj})
  
        
    else:

        empobj= EmpModel.objects.raw('SELECT * from baza.Chorzy')
     
        return render(request,'search.html',{"EmpModel":empobj})
       
        




            








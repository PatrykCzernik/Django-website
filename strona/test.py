
import mysql.connector
db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database='baza'
    )
cursor=db.cursor()
    #cursor=conn.cursor()
    
    #cursor=conn.cursor()
  
cursor.execute("SELECT Chorzy.ID_Chorego, Chorzy.Plec,Chorzy.Wiek, Chorzy.BMI, Chorzy.Typ_Nowotworu, Promieniowanie.Dawka, Srodowisko.Nazwa  FROM Chorzy INNER JOIN Promieniowanie ON Chorzy.ID_Promieniowania = Promieniowanie.ID_Promieniowania INNER JOIN Srodowisko  ON Chorzy.ID_Srodowiska = Srodowisko.ID_Srodowiska")
result=[]
for i in cursor:
    result.append(i)
    print(i)
s
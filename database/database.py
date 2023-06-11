# Gerekli Kütüphaneler
import pymysql as sql
from datetime import datetime
from os import name, system
import os
import cv2 
import numpy
from time import sleep

# Konsolu Sildirme
system("cls")

# Veri Tabanı Bağlantısı Sağlama
try:
    db = sql.connect(
        host="localhost",
        user="root",
        database="kuara",
        password="8139")
    print("Veri Tabanına Başarıyla Bağlantı Sağlandı!")
    sleep(1)
    
except:
     print("Veri Tabanı Bağlantısı Sağlanamadı!")
     sleep(1)

# İmleç Oluşturma
im = db.cursor() 

# Kodun Bulunduğu Dosya Yolu  
codePath = os.getcwd()

# Panel Resimlerinin Dosya Yolu
imagePath = codePath + "\\image" 

# Kodun Bulunduğu Dosya Yoluna Gitme
if os.path.exists(codePath) == 0:
        os.mkdir(codePath)

# Veri Tabanına TXT Dosyasındaki Verileri Ekleyen Fonksiyon
def AddPanel():
    durum = ""
    konumx=""
    konumy=""
    konumz=""
    resimanayol="C:/Users/Süleyman Samet Kaya/Desktop/Database-main/image/"
    resim=""  
    log = ""
    with open("solar.txt", "r") as txt:
        for info in txt:
            solarInfo = info.strip().split(", ")
            durum = solarInfo[0]
            konumx = solarInfo[1]
            konumy = solarInfo[2]
            konumz = solarInfo[3]
            resimyolu = resimanayol + solarInfo[4]
            log = datetime.now().strftime("%d/%m/%Y")
            data1 = (durum,konumx,konumy,konumz,log)
            data2 = "INSERT INTO panel (ID,DURUM,X,Y,Z,LOG) VALUES (NULL,'{}','{}','{}','{}','{}')"
            data2 = data2.format(*data1)
            im.execute(data2)
            db.commit()
            idcek = "SELECT MAX(ID) FROM panel"
            im.execute(idcek)
            datas = im.fetchone()
            with open(resimyolu, "rb") as binary_file:
                resim = binary_file.read()
            data3 = "UPDATE panel SET RESİM=%s WHERE ID=%s"
            im.execute(data3, (resim, datas[0]))
            db.commit()

# Veri Tabanına Veri Ekleme Fonksiyonunu Çalıştırma
try:
    sleep(1)
    system("cls")
    print("Veri Tabanına Veriler Ekleniyor...\n")
    sleep(1)
    AddPanel()
    print("İşlem Tamamlandı!")
    sleep(1)

except:
     print("Veri Tabanına Veriler Eklenemedi!")
     sleep(1)

from datetime import datetime, timedelta

def ekrana_tarih_yazdir():
    print("Tarih:", datetime.now().strftime("%d/%m/%Y"))

def ekrana_saat_ve_tarih_yazdir():
    print("Saat ve Tarih:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def ekrana_sadece_saat_yazdir():
    print("Saat:", datetime.now().strftime("%H:%M:%S"))

def saat_degisken():
    while True:
        print("Saat değişiyor:", datetime.now().strftime("%H:%M:%S"), end="\r")

def kacinci_ay():
    print("Kaçıncı ayda olduğumuz:", datetime.now().month)

def hangi_gunde():
    print("Hangi günde olduğumuz:", datetime.now().strftime("%A"))

def dogum_tarihi_yas():
    dogum_tarihi = input("Doğum tarihini gir (GG/AA/YYYY): ")
    dogum_datetime = datetime.strptime(dogum_tarihi, "%d/%m/%Y")
    yas = datetime.now().year - dogum_datetime.year - ((datetime.now().month, datetime.now().day) < (dogum_datetime.month, dogum_datetime.day))
    print("Yaşın:", yas)
    
def kac_ay_kac_gun_yas():
    dogum_tarihi = input("Doğum tarihini gir (GG/AA/YYYY): ")
    dogum_datetime = datetime.strptime(dogum_tarihi, "%d/%m/%Y")
    
    bugun = datetime.now()
    yas = bugun.year - dogum_datetime.year - ((bugun.month, bugun.day) < (dogum_datetime.month, dogum_datetime.day))
    toplam_ay = (bugun.year - dogum_datetime.year) * 12 + bugun.month - dogum_datetime.month
    toplam_gun = (bugun - dogum_datetime).days
    print("Toplam kaç ay yaşadın:", toplam_ay)
    print("Toplam kaç gün yaşadın:", toplam_gun)


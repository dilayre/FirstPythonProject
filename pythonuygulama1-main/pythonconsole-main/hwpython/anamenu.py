# bu dosyanın içeriğini de main.py dosyasına taşıdık. istersen sil, istersen dursun.

import selamlama

def anaMenu():
  print("\033[1;32;40m")
  print("╔" + "═" * 25 + "╗")
  print("║       Ana Menü          ║")
  print("║                         ║")
  print("║ 1-Hesaplamalar          ║")
  print("║ 2-Çizimler              ║")
  print("║ 3-Oyunlar               ║")
  print("║ 4- Çıkış(e)             ║")
  print("║                         ║")
  print("║                         ║")
  print("║ Seçiminiz nedir?        ║")
  print("╚" + "═" * 25 + "╝")
  secim = input()


  print("Seçiminiz:", secim)
  if secim == "1":
    import hesaplamalar.hesapm
    hesaplamalar.hesapm.menuhesap()
  if secim == "2":
    import cizimler.cizimlerm # buradaki birinci kısım klasr adı. ikinci kısım klasör içindeki cizimlerm.py dosyasını anlatıyor. Bundan sonra cizimlerm dosyasının içindeki fonksiyonları kullanabilirsin.
    cizimler.cizimlerm.cizimmenu() # birincisi klasör, ikincisi dosya, sonuncusu ise cizimlerm.py dosyası içindeki cizimmenu adlı fonksiyon.
    anaMenu() # yukarıdaki iki satırın işi bitince tekrar bu dosyadaki anaMenu fonksiyonu çalışsın dedik.
  if secim == "3": 
    import oyunlar
  if secim == "4" : 
    print("Programdan çıkılıyor")
    selamlama.iyiAksamlar()
    exit()

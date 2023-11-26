def tarihm():

    print ("  ==== HESAPLAMALAR =====  ")
    print ("                           ")
    print ("= 1-Tarih Yazdırma        =")
    print ("= 2-Saat ve Tarih Yazdırma=")
    print ("= 3-Saat                  =")
    print ("= 4-Anlık Saat            =")
    print ("= 5-Hangi Aydasın?        =")
    print ("= 6-Hangi Gündesin?       =")
    print ("= 7-Yaşını Hesapla        =")
    print ("= 8-Ne Kadar Yaşadın?     =")
    print ("= 9-Çıkış                 =")
    print ("=                         =")
    print ("===========================")
    print ("Seçiminiz nedir?")
    secim = input()
    if secim == "1":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.ekrana_tarih_yazdir()

    if secim == "2":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.ekrana_saat_ve_tarih_yazdir()

    if secim == "3":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.ekrana_sadece_saat_yazdir() 

    if secim == "4":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.saat_degisken()

    if secim == "5":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.kacinci_ay()

    if secim == "6":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.hangi_gunde()

    if secim == "7":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.dogum_tarihi_yas()

    if secim == "8":
        import hesaplamalar.yiltahmin
        hesaplamalar.yiltahmin.kac_ay_kac_gun_yas()

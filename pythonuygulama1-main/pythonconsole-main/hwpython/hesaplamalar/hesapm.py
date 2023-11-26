def menuhesap():

    print ("=== HESAPLAMALAR ===")
    print ("                    ")
    print ("= 1-Hesap Makinesi =")
    print ("= 2-Not Hesabı     =")
    print ("= 3-Yıl Tahmin     =")
    print ("= 9-Çıkış          =")
    print ("                    ")
    print ("====================")
    print ("Seçiminiz nedir?")
    secim = input()
    if secim == "1":
        import hesaplamalar.hesapmakinesi
        hesaplamalar.hesapmakinesi
    if secim == "2":
        import hesaplamalar.nothesabı
        hesaplamalar.nothesabı.gectikaldi()
    if secim == "3":
        import hesaplamalar.yilmenu
        hesaplamalar.yilmenu.tarihm()

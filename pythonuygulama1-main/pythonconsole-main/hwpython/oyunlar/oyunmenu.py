def oyunmenu():
    print ("===   OYUNLAR        ===")
    print ("= 1-ADAM ASMACA        =")
    print ("= 2-SAYI TAHMİN OYUNU  =")
    print ("= 3-ZAR OYUNU          =")
    print ("= 4-TAŞ KAĞIT MAKAS    =")
    print ("========================")
    print ("Seçiminiz nedir?")
    secim = input()
    if secim == "1":
        import oyunlar.adamasmaca
        oyunlar.adamasmaca.adamasmaca()
    if secim == "2":
        import oyunlar.sayitahmin
        oyunlar.sayitahmin.sayi_tahmin_oyunu()
    if secim == "3":
        import oyunlar.zaroyunu
        oyunlar.zaroyunu.zar()
    if secim == "4":
        import oyunlar.taskagitmakas
        oyunlar.taskagitmakas.bilgisayar_hamle()
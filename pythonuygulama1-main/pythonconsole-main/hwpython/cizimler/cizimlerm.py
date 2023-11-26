def cizimmenu():
    print ("===  WOREX-ÇİZİM ===")
    print ("= 1-YingYang       =")
    print ("= 2-Kelebek        =")
    print ("= 3-Among Us       =")
    print ("= 4-Iron Man       =")
    print ("= 9-Çıkış          =")
    print ("==================")
    print ("Seçiminiz nedir?")
    secim = input()
    if secim == "1":
        import cizimler.yingyang
        cizimler.yingyang.ciz1()
    if secim == "2":
        import cizimler.kelebek
        cizimler.kelebek.ciz2()
    if secim == "3":
        import cizimler.amongus
        cizimler.amongus.amongus()
    if secim == "4":
        import cizimler.ironman
        cizimler.ironman.iron()
import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")

    while True:
        # Rastgele bir sayı seçelim (1 ile 100 arasında)
        sayi = random.randint(1, 100)
        tahmin_hakki = 7

        while True:
            tahmin = int(input("Bir sayı tahmin edin (1-100 arasında): "))

            if tahmin < sayi:
                print("Daha büyük bir sayı girin.")
            elif tahmin > sayi:
                print("Daha küçük bir sayı girin.")
            else:
                print(f"Tebrikler! {sayi} sayısını doğru tahmin ettiniz.")
                break

            tahmin_hakki -= 1

            if tahmin_hakki == 0:
                print(f"Üzgünüm, tahmin hakkınız kalmadı. Doğru sayı: {sayi}")
                break

        devam = input("Tekrar oynamak ister misiniz? (E/H): ").lower()
        if devam != 'e':
            break


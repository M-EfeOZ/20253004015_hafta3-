import time

def hamle_sayaci():
    sayac = 0
    def artir():
        # nonlocal: İç içe fonksiyonlarda (closure), içteki fonksiyonun bir üstteki 
        # (dıştaki) fonksiyonun değişkenini okuyup değiştirebilmesini sağlar.
        # Eğer bu kelimeyi yazmazsak, Python içeride yeni bir 'sayac' oluşturmaya çalışır ve hata verir.
        nonlocal sayac
        sayac += 1
        return sayac
    return artir

def en_bagli_gezegenler(galaksi):
    gezegenler = galaksi["gezegenler"]
    baglantilar = galaksi["baglantilar"]
    
    # sorted: Bir listeyi belirli kurallara göre sıralayıp yeni bir liste oluşturur.
    # lambda: Tek satırlık isimsiz (anonim) küçük fonksiyonlar oluşturmak için kullanılır.
    # Burada key=lambda g: ... ile sıralamanın kuralını belirliyoruz.
    # (-len(...) ile önce bağlantı sayısına göre çoktan aza, eşitlik varsa 'g' ile alfabetik sıralar).
    return sorted(gezegenler, key=lambda g: (-len(baglantilar[g]), g))

def sure_olc(fonksiyon):
    def sarmalayici(*args, **kwargs):
        # time.time(): O anki zamanı saniye cinsinden (ondalıklı bir sayı olarak) verir.
        # İşlemden önceki zamanı ve sonraki zamanı alıp birbirinden çıkararak süreyi buluruz.
        baslangic = time.time()
        
        # Dışarıdan gelen fonksiyonu, ona gönderilen tüm parametrelerle (*args, **kwargs) çalıştırır.
        sonuc = fonksiyon(*args, **kwargs)
        
        bitis = time.time()
        # :.6f ifadesi, ondalıklı sayının virgülden sonraki sadece 6 basamağını göstermeye yarar.
        print(f"Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
    return sarmalayici
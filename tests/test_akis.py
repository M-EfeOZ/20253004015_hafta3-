import pytest
import typing

def yakit_gostergesi(yakit: int, tuketim: int) -> typing.Iterator[int]:
    """Her çağrıda yakıtı tüketim kadar azaltır ve kalan yakıtı üretir, 0'da durur."""
    while yakit > 0:
        yakit = yakit - tuketim
        if yakit < 0:
            yakit = 0
        yield yakit

def test_yakit_gostergesi():
    """Göstergenin doğru değerleri verdiğini ve bitince StopIteration fırlattığını test eder."""
    sonuc = list(yakit_gostergesi(100, 30))
    assert sonuc == [70, 40, 10, 0]
    
    gosterge = yakit_gostergesi(50, 30)
    next(gosterge)
    next(gosterge)
    
    with pytest.raises(StopIteration):
        next(gosterge)

print(list(yakit_gostergesi(100, 30)))

#3 test

from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar

def test_seyir_defteri_boru_hatti():
    """Boru hattının doğru toplamı ve filtrelemeyi yaptığını test eder."""
    # Toplam yakıtın 88 olduğunu test etme
    okunan_satirlar = satirlari_oku("veri/seyir.txt")
    kayitlar = ayristir(okunan_satirlar)
    
    toplam_yakit = 0
    for kaynak, hedef, yakit in kayitlar:
        toplam_yakit += yakit
        
    assert toplam_yakit == 88

    # 10'dan büyük yakıtı olan hedefleri test etme
    yeni_satirlar = satirlari_oku("veri/seyir.txt")
    yeni_kayitlar = ayristir(yeni_satirlar)
    uzunlar = uzun_yolculuklar(yeni_kayitlar, 10)
    
    hedefler = []
    for kaynak, hedef, yakit in uzunlar:
        hedefler.append(hedef)
        
    assert hedefler == ['sirius', 'centauri', 'orion', 'kara_delik']

#4 test

from uzay_oyunu.akis import rota_sayaci

def test_rota_sayaci():
    """Rota sayacının önbellekli şekilde doğru hesaplama yaptığını test eder."""
    ornek_baglantilar = {
        "dünya": ["sirius", "mars"],
        "sirius": ["orion", "dünya"],
        "mars": ["dünya"],
        "orion": ["sirius"]
    }
    
    say = rota_sayaci(ornek_baglantilar)
    
    assert say("dünya", 0) == 1
    assert say("dünya", 1) == 2
    assert say("dünya", 2) == 3

import time
# (Diğer importların burada duracak)

def test_zaman_olcum():
    ornek_baglantilar = {
        "dünya": ["sirius", "mars"],
        "sirius": ["orion", "dünya"],
        "mars": ["dünya"],
        "orion": ["sirius"]
    }
    
    # "say" değişkenini ölçüm yapmadan hemen önce burada oluşturuyoruz
    say = rota_sayaci(ornek_baglantilar)
    
    basla = time.perf_counter()
    say("dünya", 20)
    bitis = time.perf_counter()
    
    print("\nGeçen süre:", bitis - basla)
    print("Önbellek durumu:", say.cache_info())
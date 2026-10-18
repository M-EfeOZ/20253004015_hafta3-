from uzay_oyunu.istatistik import (
    buyuk_harfli_map, buyuk_harfli_liste_ureteci,
    cok_baglantili_filter, cok_baglantili_liste_ureteci,
    toplam_baglanti_reduce, toplam_baglanti_sum,
    hizli_yolculuk
)

def test_istatistik_fonksiyonlari():
    ornek_baglantilar = {
        "dünya": ["sirius"],
        "sirius": ["orion", "dünya"],
        "orion": ["sirius", "centauri", "mars"]
    }
    
    # 1. Soru Testleri
    beklenen_buyukler = ["DÜNYA", "SIRIUS", "ORION"]
    assert buyuk_harfli_map(ornek_baglantilar) == beklenen_buyukler
    assert buyuk_harfli_liste_ureteci(ornek_baglantilar) == beklenen_buyukler
    
    # 2. Soru Testleri
    beklenen_cok_baglantililar = ["sirius", "orion"]
    assert cok_baglantili_filter(ornek_baglantilar) == beklenen_cok_baglantililar
    assert cok_baglantili_liste_ureteci(ornek_baglantilar) == beklenen_cok_baglantililar
    
    # 3. Soru Testleri
    assert toplam_baglanti_reduce(ornek_baglantilar) == 6
    assert toplam_baglanti_sum(ornek_baglantilar) == 6
    
    # Partial Testi
    assert hizli_yolculuk("dünya", "mars") == "dünya -> mars yolculugu 3 hiziyla yapiliyor"
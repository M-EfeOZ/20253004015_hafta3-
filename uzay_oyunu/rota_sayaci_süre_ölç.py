import time
import functools

# 1. Süre Ölçen Dekoratör
def sure_olc(func):
    """Fonksiyonun çalışma süresini ölçer ve yazdırır."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        basla = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{func.__name__}: {bitis - basla:.4f} sn")
        return sonuc
    return wrapper

# 2. Önbelleksiz Rota Sayacı (Hafta 4 - Görev 4'ün önbelleksiz hali)
def rota_sayaci(baglantilar: dict):
    # Bilerek @lru_cache eklemiyoruz ki önbelleksiz süreyi görelim
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        toplam = 0
        if gezegen in baglantilar:
            for komsu in baglantilar[gezegen]:
                toplam += rota_sayisi(komsu, adim - 1)
        return toplam
    return rota_sayisi

# 3. 20 Adımı Çalıştıran ve Ölçen Fonksiyon
@sure_olc
def yirmi_adim_testi(baglantilar: dict, baslangic: str = "dünya", adim: int = 20) -> int:
    say = rota_sayaci(baglantilar)
    return say(baslangic, adim)

# --- Test ve Çalıştırma ---
if __name__ == "__main__":
    ornek_baglantilar = {
        "dünya": ["sirius", "mars"],
        "sirius": ["orion", "dünya"],
        "mars": ["dünya"],
        "orion": ["sirius"]
    }

    print("Önbelleksiz 20 adım hesaplanıyor (Bu birkaç saniye sürebilir)...")
    toplam_rota = yirmi_adim_testi(ornek_baglantilar, "dünya", 20)
    print(f"Toplam Rota Sayısı: {toplam_rota}")
import pytest

KOMUTLAR = {}

def komut(ad: str, aciklama: str = ""):
    """Fonksiyonu değiştirmeden KOMUTLAR sözlüğüne kaydeden dekoratör."""
    def decorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı.")
        KOMUTLAR[ad] = (func, aciklama)
        return func
    return decorator

@komut("yardim", "komutları listeler")
def yardim(durum: dict) -> str:
    """Kayıtlı tüm komutları ve açıklamalarını döndürür."""
    satirlar = [f"{ad} {aciklama}" for ad, (f, aciklama) in sorted(KOMUTLAR.items())]
    return "\n".join(satirlar)

@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict) -> str:
    """Oyuncunun envanter bilgilerini döndürür."""
    return f"Kredi: {durum.get('credits', 0)}, Motor: {durum.get('engines', 0)}, Yardımcı Pilot: {durum.get('copilot', 'Yok')}"

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict) -> str:
    """Mevcut konumdan gidilebilecek gezegenleri döndürür."""
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    hedefler = baglantilar.get(konum, [])
    return ", ".join(hedefler)

def test_komut_sistemi():
    ornek_durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["orion", "sirius", "kara_delik"]},
        "credits": 100,
        "engines": 2,
        "copilot": "Ateş"
    }

    assert "yardim" in KOMUTLAR
    assert "envanter" in KOMUTLAR
    assert "harita" in KOMUTLAR

    yardim_cikti = yardim(ornek_durum)
    assert "envanter eşyalarını gösterir" in yardim_cikti
    assert "harita gidebileceğin gezegenleri gösterir" in yardim_cikti
    assert "yardim komutları listeler" in yardim_cikti

    assert harita(ornek_durum) == "orion, sirius, kara_delik"
    assert "100" in envanter(ornek_durum)

    with pytest.raises(ValueError):
        @komut("harita", "tekrar kayıt denemesi")
        def sahte_harita(durum):
            pass

# görev 4

import pytest


def test_yardim_komutu():
    durum = {}
    cikti = yardim(durum)
    assert "envanter eşyalarını gösterir" in cikti
    assert "harita gidebileceğin gezegenleri gösterir" in cikti
    assert "yardim komutları listeler" in cikti

def test_envanter_komutu():
    durum = {"credits": 100, "engines": 2, "copilot": "Ateş"}
    cikti = envanter(durum)
    assert "100" in cikti
    assert "2" in cikti
    assert "Ateş" in cikti

def test_harita_komutu():
    durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["orion", "sirius", "kara_delik"]}
    }
    assert harita(durum) == "orion, sirius, kara_delik"

def test_ayni_isimle_komut_kaydi_hata_verir():
    with pytest.raises(ValueError):
        @komut("harita", "tekrar kayıt denemesi")
        def sahte_harita(durum):
            pass

#5

import functools
import pytest

def sinirla(alt: int, ust: int):
    """Fonksiyonun ilk argümanının [alt, ust] aralığında olmasını zorunlu kılar."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # İlk argümanı yakala (konumsal veya adlı olarak gelebilir)
            if args:
                deger = args[0]
            else:
                deger = next(iter(kwargs.values()))
                
            if not (alt <= deger <= ust):
                raise ValueError(f"{func.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
                
            return func(*args, **kwargs)
        return wrapper
    return decorator

@sinirla(0, 100)
def yakit_harca(miktar: int) -> int:
    """100 birimlik başlangıç yakıtından harcanan miktarı düşer."""
    return 100 - miktar


def test_sinirla_normal_ve_sinir_degerler():
    # Normal değer testi
    assert yakit_harca(30) == 70
    
    # Sınır değerleri (0 ve 100) ayrı ayrı test
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0

def test_sinirla_ust_sinir_disi():
    with pytest.raises(ValueError) as exc_info:
        yakit_harca(150)
    assert str(exc_info.value) == "yakit_harca: 150 değeri 0-100 aralığında değil"

def test_sinirla_alt_sinir_disi():
    with pytest.raises(ValueError) as exc_info:
        yakit_harca(-10)
    assert str(exc_info.value) == "yakit_harca: -10 değeri 0-100 aralığında değil"

def test_sinirla_meta_veri_koruma():
    assert yakit_harca.__name__ == "yakit_harca"
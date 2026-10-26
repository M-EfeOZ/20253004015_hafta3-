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

#hafta 4 görev 2

import functools

def say(func):
    """Fonksiyonun kaç kez çağrıldığını sayar."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        mevcut = getattr(wrapper, "cagri", 0)
        setattr(wrapper, "cagri", mevcut + 1)
        return func(*args, **kwargs)
    
    setattr(wrapper, "cagri", 0)
    return wrapper

def test_fib_sadece_say():
    @say
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    fib(20)
    assert getattr(fib, "cagri") == 21891

def test_fib_say_ustte_lru_altta():
    @say
    @functools.lru_cache(maxsize=None)
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    fib(20)
    assert getattr(fib, "cagri") == 39

def test_fib_lru_ustte_say_altta():
    @functools.lru_cache(maxsize=None)
    @say
    def fib(n):
        if n < 2: return n
        return fib(n-1) + fib(n-2)
    
    fib(20)
    alt_fonksiyon = getattr(fib, "__wrapped__")
    assert getattr(alt_fonksiyon, "cagri") == 21

# log cağrı

import functools

def log_cagri(func):
    """Fonksiyon çağrılmadan önce argümanları, sonra dönüş değerini yazdırır."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_listesi = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        arg_metni = ", ".join(arg_listesi)
        print(f"-> {func.__name__}({arg_metni})")
        
        sonuc = func(*args, **kwargs)
        
        print(f"<- {func.__name__} {sonuc!r}")
        return sonuc
    return wrapper

@log_cagri
def galaksi_kur():
    """Galaksi verisini oluşturur."""
    return {"dünya": ["sirius", "orion"]}

@log_cagri
def hedef_menusu(gezegenler):
    """Hedef gezegenlerin menüsünü döndürür."""
    return [f"[{i+1}] {g}" for i, g in enumerate(gezegenler)]


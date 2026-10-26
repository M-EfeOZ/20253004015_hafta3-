import time
import functools

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


def test_sure_olc():
    @sure_olc
    def topla(a, b=0):
        """İki sayıyı toplar."""
        return a + b

    # 1. Sonuç değişmeden dönüyor mu?
    assert topla(5, 3) == 8

    # 2. Adlı (keyword) argümanlarla çağrı çalışıyor mu?
    assert topla(5, b=10) == 15

    # 3. __name__ ve __doc__ korunuyor mu?
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "İki sayıyı toplar."

###

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

#log çağrı

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

def test_log_cagri(capsys):
    @log_cagri
    def yolculuk(hedef, hiz=1):
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    cikti = capsys.readouterr().out
    assert "-> yolculuk('orion', hiz=3)" in cikti
    assert "<- yolculuk 'orion hiz=3'" in cikti

    galaksi = galaksi_kur()
    assert "dünya" in galaksi
    assert hedef_menusu(galaksi["dünya"]) == ["[1] sirius", "[2] orion"]
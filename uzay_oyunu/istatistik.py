import functools

# 1. Gezegen adlarının büyük harfli listesi
def buyuk_harfli_map(baglantilar: dict) -> list:
    return list(map(str.upper, baglantilar.keys()))

def buyuk_harfli_liste_ureteci(baglantilar: dict) -> list:
    return [gezegen.upper() for gezegen in baglantilar.keys()]

# 2. En az iki bağlantısı olan gezegenler
def cok_baglantili_filter(baglantilar: dict) -> list:
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar.keys()))

def cok_baglantili_liste_ureteci(baglantilar: dict) -> list:
    return [gezegen for gezegen, komsular in baglantilar.items() if len(komsular) >= 2]

# 3. Toplam bağlantı sayısı
def toplam_baglanti_reduce(baglantilar: dict) -> int:
    return functools.reduce(lambda acc, komsular: acc + len(komsular), baglantilar.values(), 0)

def toplam_baglanti_sum(baglantilar: dict) -> int:
    return sum(len(komsular) for komsular in baglantilar.values())

# --- functools.partial kullanımı ---
def yolculuk(kaynak: str, hedef: str, hiz: int) -> str:
    return f"{kaynak} -> {hedef} yolculugu {hiz} hiziyla yapiliyor"

hizli_yolculuk = functools.partial(yolculuk, hiz=3)

#bence direkt olarak list comprehension ve sum ile yaptığımız kodlama daha okunaklı ve anlaşılır.
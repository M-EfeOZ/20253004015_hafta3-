def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
from itertools import islice,takewhile
print(list(islice(fibonacci(),12)))
print(list(takewhile(lambda x: x<100,fibonacci())))

g = fibonacci()
assert next(g) == 0
assert next(g) == 1
assert next(g) == 1

print(g)

#3
import typing

def satirlari_oku(yol: str) -> typing.Iterator[str]:
    """Dosyadan boş olmayan ve # ile başlamayan satırları tek tek okur."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz_satir = satir.strip()
            if temiz_satir != "" and not temiz_satir.startswith("#"):
                yield temiz_satir

def ayristir(satirlar: typing.Iterator[str]) -> typing.Iterator[tuple]:
    """Satırları kaynak, hedef ve yakıt olarak ayırır."""
    for satir in satirlar:
        parcalar = satir.split()
        kaynak = parcalar[0]
        hedef = parcalar[2]
        yakit = int(parcalar[3])
        yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar: typing.Iterator[tuple], esik: int) -> typing.Iterator[tuple]:
    """Yakıt tüketimi eşik değerinden büyük olan yolculukları filtreler."""
    for kayit in kayitlar:
        yakit = kayit[2]
        if yakit > esik:
            yield kayit

#4

import functools
import typing

def rota_sayaci(baglantilar: dict) -> typing.Callable:
   
    
    @functools.lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        
        toplam = 0
        if gezegen in baglantilar:
            for komsu in baglantilar[gezegen]:
                toplam += rota_sayisi(komsu, adim - 1)
        
        return toplam
        
    return rota_sayisi
    
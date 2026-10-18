from typing import Iterator

def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her çağrıda yakıtı tüketim kadar azaltır ve kalan yakıtı üretir, 0'da durur."""
    while yakit > 0:
        yakit = yakit - tuketim
        if yakit < 0:
            yakit = 0
        yield yakit

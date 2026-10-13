import json

def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    if baslangic not in gezegenler:
        # raise: Kasıtlı olarak bir hata (exception) fırlatıp programın çalışmasını durdurur.
        # ValueError: Gönderilen değerin (baslangic) türü doğru olsa bile, içeriğinin 
        # veya mantığının (listede olmaması) yanlış olduğunu belirtir.
        raise ValueError("Başlangıç gezegeni listede yok.")
        
    # get(): Sözlükten (dictionary) bir değeri güvenli şekilde okumayı sağlar.
    # Eğer "yakit" anahtarı kwargs içinde yoksa program çökmez, virgülden sonraki 
    # varsayılan değeri (burada 50) değişkene atar.
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

if __name__ == "__main__":
    # with open(...): Dosya açma işlemidir. 'with' kelimesi, içerideki işlemler bitince 
    # veya bir hata çıkarsa dosyanın otomatik olarak kapatılmasını (close) sağlar.
    # "r": Dosyanın sadece okuma (read) modunda açılacağını belirtir.
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
        # json.load(): Açılmış bir JSON dosyasının içindeki metin formatındaki veriyi okuyup, 
        # Python'ın kullanabileceği bir sözlüğe (dictionary) dönüştürür.
        veri = json.load(dosya)
        
    g = galaksi_kur(**veri)
    print(g["konum"], g["yakit"])
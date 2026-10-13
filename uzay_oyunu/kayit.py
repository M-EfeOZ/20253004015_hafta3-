# *adimlar (*args): Fonksiyona istediğimiz sayıda fazladan parametre göndermemizi sağlar.
# Gelen bu değerleri bir tuple (demet) içinde toplar.
# **ekler (**kwargs): İsimlendirilerek gönderilen fazladan parametreleri (örneğin pilot="Ali" gibi) 
# bir sözlük (dictionary) yapısında toplar.
def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    # upper(): Bir metnin (string) içindeki tüm harfleri BÜYÜK harfe dönüştürür.
    print(f"[{oncelik.upper()}] {baslik}")
    
    for i, adim in enumerate(adimlar, 1):
        print(f"{i}. {adim}")
        
    # items(): Bir sözlüğün (dictionary) içindeki anahtar (key) ve değer (value) çiftlerini 
    # parçalayarak döngü içinde aynı anda kullanmamızı sağlar.
    for anahtar, deger in ekler.items():
        print(f"{anahtar}: {deger}")

if __name__ == "__main__":
    yapilacaklar = ["Kredi kazan", "Pilot bul", "Uçak al"]
    detaylar = {"sorumlu": "Mert"}
    
    # *yapilacaklar (Unpacking): Listenin içindeki elemanları paketinden çıkarıp 
    # fonksiyona tek tek virgülle ayrılmış parametreler gibi gönderir.
    # **detaylar (Unpacking): Sözlüğün içindeki eşleşmeleri paketinden çıkarıp 
    # fonksiyona doğrudan sorumlu="Mert" şeklinde isimlendirilmiş parametre olarak gönderir.
    gorev_kaydi("Kara deliğe atla", *yapilacaklar, oncelik="yüksek", **detaylar)
    
    print()
    
    gorev_kaydi("Dünyaya dön", "Motoru çalıştır", "Rotayı çiz", oncelik="normal", pilot="Ali", yakit="Tam")
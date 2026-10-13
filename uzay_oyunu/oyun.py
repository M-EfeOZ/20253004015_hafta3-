def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    esyalar = []
    if credits:
        # append: Listeye yeni bir eleman eklemeye yarar. 
        # Eşyayı alır ve mevcut 'esyalar' listesinin en sonuna yerleştirir.
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hiper sürücü")
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    if not esyalar:
        return ""
        
    # join: Bir liste içindeki tüm elemanları, belirttiğimiz karakterle (burada ", ")
    # birbirine yapıştırarak tek parça bir metin (string) haline getirir.
    # Örnek: ["kredi", "pilot"] listesini "kredi, pilot" metnine dönüştürür.
    return "Sende: " + ", ".join(esyalar)

def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    
    # enumerate: Bir liste içinde dönerken, elemanlara otomatik olarak numara (index) atar.
    # Yanındaki '1' değeri, saymaya 0'dan değil 1'den başlamasını söyler.
    # Böylece i değişkeni numarayı (1, 2, 3...), hedef değişkeni ise gezegen adını tutar.
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
        
    return "\n".join(satirlar)
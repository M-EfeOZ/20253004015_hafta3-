# depo=None: Parametreye varsayılan olarak boş liste ([]) vermek yerine None veriyoruz.
# Çünkü Python'da varsayılan listeler sadece bir kez oluşturulur ve her fonksiyon çağrısında 
# aynı liste hafızada tutularak paylaşılır. None kullanarak listelerin birbirine karışmasını önlüyoruz.
def yakit_ekle(miktar, depo=None):
    # is None: Bir değişkenin gerçekten "None" (hiçlik) objesi olup olmadığını kontrol eder.
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle():
    benim_gemi = yakit_ekle(50)
    senin_gemi = yakit_ekle(30)
    
    # assert: Test yazarken kullanılır. "İddia ediyorum ki burası Doğru (True) çıkacak" demektir.
    # Eğer benim_gemi gerçekten [50]'ye eşitse kod sessizce çalışmaya devam eder,
    # eşit değilse 'AssertionError' hatası fırlatıp testin başarısız olduğunu bildirir.
    assert benim_gemi == [50]
    assert senin_gemi == [30]

    #none ile düzeltilmiş hali
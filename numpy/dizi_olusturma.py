import numpy as np  # NumPy kütüphanesini programa dahil ederiz

# 1. Dizi oluşturma
dizi1 = np.array([10, 20, 30, 40, 50])  # Sayılardan oluşan bir dizi oluştururuz
print("Dizi 1:", dizi1)  # Diziyi ekrana yazdırırız

# 2. İkinci bir dizi oluşturma
dizi2 = np.array([1, 2, 3, 4, 5])  # İkinci diziyi oluştururuz
print("Dizi 2:", dizi2)  # İkinci diziyi ekrana yazdırırız

# 3. İki diziyi toplama
toplam = dizi1 + dizi2  # Aynı konumdaki elemanları toplarız
print("Dizilerin toplamı:", toplam)  # Toplam dizisini ekrana yazdırırız

# 4. İki diziyi çıkarma
fark = dizi1 - dizi2  # Aynı konumdaki elemanları birbirinden çıkarırız
print("Dizilerin farkı:", fark)  # Fark dizisini ekrana yazdırırız

# 5. İki diziyi çarpma
carpim = dizi1 * dizi2  # Aynı konumdaki elemanları çarparız
print("Dizilerin çarpımı:", carpim)  # Çarpım dizisini ekrana yazdırırız

# 6. İki diziyi bölme
bolum = dizi1 / dizi2  # Aynı konumdaki elemanları birbirine böleriz
print("Dizilerin bölümü:", bolum)  # Bölüm dizisini ekrana yazdırırız

# 7. Dizideki en büyük değeri bulma
maksimum = np.max(dizi1)  # Dizideki en büyük sayıyı buluruz
print("En büyük değer:", maksimum)  # En büyük değeri ekrana yazdırırız

# 8. Dizideki en küçük değeri bulma
minimum = np.min(dizi1)  # Dizideki en küçük sayıyı buluruz
print("En küçük değer:", minimum)  # En küçük değeri ekrana yazdırırız

# 9. Dizinin ortalamasını bulma
ortalama = np.mean(dizi1)  # Dizideki sayıların ortalamasını hesaplarız
print("Ortalama:", ortalama)  # Ortalamayı ekrana yazdırırız

# 10. Dizideki elemanların toplamını bulma
genel_toplam = np.sum(dizi1)  # Dizideki bütün sayıları toplarız
print("Elemanların toplamı:", genel_toplam)  # Sonucu ekrana yazdırırız

# 11. Dizinin eleman sayısını bulma
eleman_sayisi = len(dizi1)  # Dizide kaç eleman olduğunu buluruz
print("Eleman sayısı:", eleman_sayisi)  # Eleman sayısını ekrana yazdırırız

# 12. Dizinin belirli bir elemanını bulma
print("İlk eleman:", dizi1[0])  # İlk elemanı ekrana yazdırırız
print("Üçüncü eleman:", dizi1[2])  # Üçüncü elemanı ekrana yazdırırız

# 13. Belirli aralıkta sayılar oluşturma
sayilar = np.arange(0, 11, 2)  # 0'dan 10'a kadar ikişer artan sayılar oluştururuz
print("Sayı örüntüsü:", sayilar)  # Oluşan diziyi ekrana yazdırırız

# 14. Dizideki elemanları sıralama
karisik = np.array([30, 10, 50, 20, 40])  # Sıralanmamış bir dizi oluştururuz
sirali = np.sort(karisik)  # Elemanları küçükten büyüğe sıralarız
print("Sıralı dizi:", sirali)  # Sıralı diziyi ekrana yazdırırız

# 15. Belirli bir koşulu sağlayan elemanları bulma
buyuk_sayilar = dizi1[dizi1 > 25]  # 25'ten büyük elemanları seçeriz
print("25'ten büyük sayılar:", buyuk_sayilar)  # Seçilen sayıları ekrana yazdırırız



import numpy as np

# Sıfırlardan oluşan dizi
print("zeros:\n", np.zeros((2, 3)))

# Birlerden oluşan dizi
print("ones:\n", np.ones((2, 3)))

# Belirli aralıkta, belirli adımla dizi (bitiş dahil değil)
print("arange:\n", np.arange(0, 10, 2))




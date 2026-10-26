import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot bölümünü içe aktarır ve plt olarak adlandırır

aylar = ["Ocak", "Şubat", "Mart", "Nisan"]  # Grafikte gösterilecek ayların isimlerini bir liste içinde tutar
urun_a = [10, 20, 15, 30]  # Ürün A'nın aylara göre satış miktarlarını tutar
urun_b = [15, 18, 25, 28]  # Ürün B'nin aylara göre satış miktarlarını tutar

plt.plot(aylar, urun_a, label="Ürün A")  # Ürün A'nın satışlarını çizgi grafiğinde gösterir ve çizgiyi Ürün A olarak adlandırır
plt.plot(aylar, urun_b, label="Ürün B")  # Ürün B'nin satışlarını aynı grafikte gösterir ve çizgiyi Ürün B olarak adlandırır

plt.title("Ürün Satış Karşılaştırması")  # Grafiğin başlığını belirler
plt.xlabel("Aylar")  # Yatay eksenin adını belirler
plt.ylabel("Satış")  # Dikey eksenin adını belirler
plt.legend()  # Hangi çizginin hangi ürüne ait olduğunu gösteren açıklama kutusunu ekler
plt.grid(True)  # Grafiğin arka planına ızgara çizgileri ekler

plt.show()  # Oluşturulan grafiği ekranda gösterir
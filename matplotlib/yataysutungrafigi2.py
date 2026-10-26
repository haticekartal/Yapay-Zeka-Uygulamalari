import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot bölümünü içe aktarır ve plt olarak adlandırır

urunler = ["Kalem", "Defter", "Silgi", "Kitap"]  # Ürün isimlerini bir liste içinde tutar
satislar = [20, 35, 15, 40]  # Her ürünün satış miktarını bir liste içinde tutar

plt.barh(urunler, satislar)  # Ürünleri yatay sütunlar şeklinde gösteren bir grafik oluşturur

plt.title("Ürün Satışları")  # Grafiğin başlığını belirler
plt.xlabel("Satış Miktarı")  # Yatay eksenin adını belirler
plt.ylabel("Ürünler")  # Dikey eksenin adını belirler

plt.show()  # Oluşturulan grafiği ekranda gösterir
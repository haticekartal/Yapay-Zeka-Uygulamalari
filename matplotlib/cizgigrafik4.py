import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot bölümünü içe aktarır ve plt olarak adlandırır

gunler = [1, 2, 3, 4, 5]  # Günleri temsil eden sayıları bir liste içinde tutar
satislar = [10, 15, 8, 20, 25]  # Her güne ait satış miktarlarını bir liste içinde tutar

plt.plot(gunler, satislar, marker="o", linestyle="--")  # Günlük satışları çizgi grafiğinde gösterir, noktalara daire işareti ve çizgiye kesikli stil verir

plt.title("Günlük Satışlar")  # Grafiğin başlığını belirler
plt.xlabel("Gün")  # Yatay eksenin adını belirler
plt.ylabel("Satış")  # Dikey eksenin adını belirler
plt.grid(True)  # Grafiğin arka planına ızgara çizgileri ekler

plt.show()  # Oluşturulan grafiği ekranda gösterir
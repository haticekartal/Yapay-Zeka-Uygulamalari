import matplotlib.pyplot as plt  # Grafik çizmek için Matplotlib kütüphanesini ekleriz

# 1. Basit çizgi grafiği oluşturma
gunler = [1, 2, 3, 4, 5]  # Günleri belirleriz
sicaklik = [18, 21, 19, 24, 22]  # Günlere ait sıcaklıkları belirleriz
plt.plot(gunler, sicaklik)  # Günlere göre sıcaklık grafiği çizeriz
plt.show()  # Grafiği ekranda gösteririz

# 2. Grafiğe başlık ekleme
plt.plot(gunler, sicaklik)  # Çizgi grafiği oluştururuz
plt.title("Haftalık Sıcaklık")  # Grafiğe başlık ekleriz
plt.show()  # Grafiği gösteririz

# 3. Eksenlere isim verme
plt.plot(gunler, sicaklik)  # Çizgi grafiği oluştururuz
plt.xlabel("Gün")  # Yatay eksene isim veririz
plt.ylabel("Sıcaklık (°C)")  # Dikey eksene isim veririz
plt.show()  # Grafiği gösteririz

# 4. Grafiğe kılavuz çizgileri ekleme
plt.plot(gunler, sicaklik)  # Çizgi grafiği oluştururuz
plt.grid(True)  # Grafiğin arka planına kılavuz çizgileri ekleriz
plt.show()  # Grafiği gösteririz

# 5. Çizgi rengini değiştirme
plt.plot(gunler, sicaklik, color="red")  # Çizgiyi kırmızı renkte çizeriz
plt.show()  # Grafiği gösteririz

# 6. Çizgi kalınlığını değiştirme
plt.plot(gunler, sicaklik, linewidth=3)  # Çizginin kalınlığını artırırız
plt.show()  # Grafiği gösteririz

# 7. Noktaları işaretleme
plt.plot(gunler, sicaklik, marker="o")  # Her veri noktasına daire işareti ekleriz
plt.show()  # Grafiği gösteririz
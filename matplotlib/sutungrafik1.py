import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot bölümünü içe aktarır ve plt olarak adlandırır

ogrenciler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]  # Öğrenci isimlerini bir liste içinde tutar
notlar = [70, 85, 60, 95]  # Öğrencilerin notlarını bir liste içinde tutar

plt.bar(ogrenciler, notlar)  # Öğrenci isimlerini ve notlarını kullanarak sütun grafiği oluşturur

plt.title("Öğrenci Notları")  # Grafiğin başlığını belirler
plt.xlabel("Öğrenciler")  # Yatay eksenin adını belirler
plt.ylabel("Notlar")  # Dikey eksenin adını belirler

plt.show()  # Oluşturulan grafiği ekranda gösterir
import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot bölümünü içe aktarır ve plt olarak adlandırır

dersler = ["Python", "Matematik", "İngilizce", "Veri Bilimi"]  # Ders isimlerini bir liste içinde tutar
saatler = [10, 5, 3, 7]  # Her derse ayrılan çalışma saatlerini bir liste içinde tutar

plt.pie(saatler, labels=dersler, autopct="%1.1f%%")  # Çalışma saatlerini pasta grafiğinde gösterir, ders isimlerini ekler ve yüzdeleri bir ondalık basamakla gösterir

plt.title("Ders Çalışma Süreleri")  # Grafiğin başlığını belirler

plt.show()  # Oluşturulan pasta grafiğini ekranda gösterir
import numpy as np
import pandas as pd

# Öğrenci notlarını NumPy ile oluşturalım
notlar = np.array([70, 85, 90, 60, 75])

# Öğrenci isimlerini oluşturalım
isimler = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Elif"]

# Verileri tablo hâline getirelim
veriler = pd.DataFrame({
    "Öğrenci Adı": isimler,
    "Not": notlar
})

# Notların ortalamasını hesaplayalım
print("Notların ortalaması:", np.mean(notlar))

# Tabloyu ekrana yazdıralım
print(veriler)

# Excel dosyasına kaydedelim
veriler.to_excel("ogrenci_notlari.xlsx", index=False)

print("Excel dosyası oluşturuldu!")
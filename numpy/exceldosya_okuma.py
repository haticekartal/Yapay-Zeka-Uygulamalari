import pandas as pd
import numpy as np

# Excel dosyasını okuyalım
veriler = pd.read_excel("ogrenci_notlari2.xlsx")

# Öğrenci tablosunu yazdıralım
print(veriler)

# Matematik notlarını alalım
matematik = veriler["Matematik"].to_numpy()

# Ortalama notu hesaplayalım
print("Matematik ortalaması:", np.mean(matematik))

# En yüksek notu bulalım
print("En yüksek not:", np.max(matematik))

# En düşük notu bulalım
print("En düşük not:", np.min(matematik))
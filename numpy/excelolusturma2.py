# Bu program NumPy ve Pandas kütüphanelerini kullanarak aylık gider tablosu oluşturur ve Excel dosyasına kaydeder.

import numpy as np
import pandas as pd

# Gider kategorileri
kategoriler = ["Kira", "Market", "Ulaşım", "Elektrik", "Su", "İnternet"]

# NumPy ile gider tutarlarını oluşturalım
giderler = np.array([12000, 4500, 1500, 800, 300, 500])

# Pandas ile tablo oluşturalım
veriler = {
    "Gider Kategorisi": kategoriler,
    "Gider Tutarı (TL)": giderler
}

tablo = pd.DataFrame(veriler)

# Excel dosyasına kaydedelim
tablo.to_excel("aylik_giderler.xlsx", index=False)

# Tabloyu ekrana yazdıralım
print(tablo)

print("Excel gider tablosu oluşturuldu.")

# Bu program giderleri hesaplar ve toplam ile ortalamayı Excel dosyasına kaydeder.

import pandas as pd

# Excel dosyasını okuyalım
tablo = pd.read_excel("aylik_giderler.xlsx")

# Önceki toplam ve ortalama satırlarını temizleyelim
tablo = tablo[
    ~tablo["Gider Kategorisi"].isin(["TOPLAM", "ORTALAMA"])
].copy()

# Gider tutarlarını alalım
giderler = tablo["Gider Tutarı (TL)"]

# Toplam ve ortalamayı hesaplayalım
toplam = giderler.sum()
ortalama = giderler.mean()

# Excel tablosuna toplam satırını ekleyelim
tablo.loc[len(tablo)] = ["TOPLAM", toplam]

# Excel tablosuna ortalama satırını ekleyelim
tablo.loc[len(tablo)] = ["ORTALAMA", round(ortalama, 2)]

# Excel dosyasını güncelleyelim
with pd.ExcelWriter(
    "aylik_giderler.xlsx",
    engine="openpyxl",
    mode="w"
) as writer:
    tablo.to_excel(writer, index=False, sheet_name="Giderler")

# Sonuçları ekrana yazdıralım
print(tablo)
print("Toplam gider:", toplam, "TL")
print("Ortalama gider:", round(ortalama, 2), "TL")
print("Sonuçlar Excel dosyasına kaydedildi.")

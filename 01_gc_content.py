dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGA GTGTCTGATA GCAGC   "

# 1. Boşluklar silinmeden önceki Ham (Raw) uzunluk
raw = len(dna)

# 2. Tüm boşluk, alt satır (\n) ve sekme (\t) karakterlerini temizleme
dna = "".join(dna.split())

# 3. Baz sayılarını hesaplama
A_sayisi = dna.count("A")
G_sayisi = dna.count("G")
T_sayisi = dna.count("T")
C_sayisi = dna.count("C")

# 4. Boşluksuz gerçek baz sayısı
total_k = len(dna)

# 5. GC oranı hesaplama
GC_orani = ((C_sayisi + G_sayisi) / total_k) * 100

print("A:", A_sayisi)
print("G:", G_sayisi)
print("T:", T_sayisi)
print("C:", C_sayisi)
print("raw (boşluklu karakter sayısı):", raw)
print("total (temizlenmiş baz sayısı):", total_k)
print("G ve C oranı: %", round(GC_orani, 2))

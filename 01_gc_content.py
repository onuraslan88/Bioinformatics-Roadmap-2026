dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
A_sayisi =  dna.count("A")
print("A:" , A_sayisi)
G_sayisi = dna.count("G")
print("G:" , G_sayisi)
T_sayisi = dna.count("T")
print("T:" , T_sayisi)
C_sayisi = dna.count("C")
print("C:" , C_sayisi)
total_k = len(dna)
print("total:" , total_k)
GC_orani = ((C_sayisi + G_sayisi) / total_k) * 100
print("G ve C oranı:", GC_orani)
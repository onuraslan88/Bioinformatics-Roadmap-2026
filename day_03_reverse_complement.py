dna_seq = "AAAACCcgtG GT "
clean_dna_seq = dna_seq.strip().upper().replace(" " , "")
print("Original DNA:" , clean_dna_seq)

transed = str.maketrans("ACGT" , "TGCA")
complement_dna = clean_dna_seq.translate(transed)
print("Complement DNA:" , complement_dna)

reverse_seq = complement_dna[::-1]
print("Reverse complement:" , reverse_seq)

print("Total sequence lenght:" , len(clean_dna_seq))

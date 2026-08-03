dna_seq = "gatgGaacttgacacataaaccc t"

clean_dna_seq = dna_seq.upper().strip().replace(" ", "")

clean_rna_seq = clean_dna_seq.replace("T", "U")

print(f"Original DNA : {clean_dna_seq}")
print(f"RNA Sequence : {clean_rna_seq}")
print(f"Length of Seq: {len(clean_rna_seq)}")

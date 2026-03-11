# Meu primeiro script de Bioinformática
sequencia_dna = "ATGCGTAATGCCGTCGTCGA"

# Contando o tamanho
tamanho = len(sequencia_dna)

# Calculando a porcentagem de GC (muito comum em Bioinfo)
gc_count = sequencia_dna.count('G') + sequencia_dna.count('C')
porcentagem_gc = (gc_count / tamanho) * 100

print(f"DNA: {sequencia_dna}")
print(f"Comprimento: {tamanho} bp")
print(f"Conteúdo GC: {porcentagem_gc:.2f}%")
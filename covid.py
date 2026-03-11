from Bio import Entrez, SeqIO
import os

# 1. Identificação - Use seu e-mail para o NCBI te autorizar
Entrez.email = "pedrocapelabioinfo@gmail.com"

print("Iniciando download do genoma do SARS-CoV-2...")

try:
    # 2. Fazendo o download e salvando em um arquivo real no seu PC
    filename = "sars_cov2.gb"
    
    # Este 'if' verifica se você já baixou o arquivo antes para não repetir o download
    if not os.path.exists(filename):
        print("Conectando ao NCBI...")
        with Entrez.efetch(db="nucleotide", id="NC_045512.2", rettype="gb", retmode="text") as handle:
            with open(filename, "w") as out_handle:
                out_handle.write(handle.read())
        print("Arquivo baixado e salvo com sucesso!")
    else:
        print("Usando o arquivo que já foi baixado anteriormente...")
    
    # 3. Lendo o arquivo que agora está salvo na sua pasta
    registro = SeqIO.read(filename, "genbank")
    genoma = registro.seq
    
    print("-" * 35)
    print(f"Vírus: {registro.description[:50]}...")
    print(f"Tamanho: {len(genoma)} bases (letras)")
    print("-" * 35)

except Exception as e:
    print(f"Ocorreu um problema: {e}")

from Bio.SeqUtils import gc_fraction

# ... (seu código anterior continua aqui) ...

# 4. Cálculos Bioinformáticos
tamanho = len(genoma)
contagem_a = genoma.count("A")
contagem_t = genoma.count("T")
contagem_g = genoma.count("G")
contagem_c = genoma.count("C")

# Porcentagem de GC (Guanina + Citosina)
porcentagem_gc = gc_fraction(genoma) * 100

# 5. Relatório Detalhado
print("-" * 35)
print(f"Total de Bases: {tamanho}")
print(f"Adeninas (A): {contagem_a}")
print(f"Timinas (T): {contagem_t}")
print(f"Guaninas (G): {contagem_g}")
print(f"Citosinas (C): {contagem_c}")
print(f"Conteúdo GC: {porcentagem_gc:.2f}%")
print("-" * 35)
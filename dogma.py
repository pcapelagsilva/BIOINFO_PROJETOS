from Bio.Seq import Seq

#1. Nossa sequência de DNA (um gene hipotético)
dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(f"DNA: {dna}")

#2. Transcrição (DNA -> RNA Mensageiro)
rna = dna.transcribe()
print(f"RNA: {rna}")

#3. Tradução (RNA -> Proteína)
proteina = rna.translate()
print(f"Proteína: {proteina}")

from Bio.Seq import Seq
from Bio.SeqUtils import ProtParam

# Sequência original
dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
proteina = dna.translate()

#Vamos analisar apenas a primeira parte da proteína, para isso usamos o .split('*')[0]
proteina_limpa = str(proteina).split('*')[0]
analise = ProtParam.ProteinAnalysis(proteina_limpa)

print(f"Proteína Analisada: {proteina_limpa}")
print(f"Peso Molecular: {analise.molecular_weight():.2f} Da")
print(f"Índice de Aromaticidade: {analise.aromaticity():.2f}")
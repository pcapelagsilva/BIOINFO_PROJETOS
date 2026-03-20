from Bio.Seq import Seq
from Bio.SeqUtils import ProtParam

# Definição da sequencia de DNA da Insulina B:
dna_seq = Seq("TTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACC")

#Tradução para Proteina
proteina = dna_seq.translate()

# Peso da proteína
peso = ProtParam.ProteinAnalysis(str(proteina))

#Tamanho da proteína:
tamanho = len(proteina)

# Verificação se a Cisteína (C):
tem_cisteina = "C" in proteina

print("A sequência de DNA da Insulina B é {}. Quando traduzida em forma de proteína sua sequência se torna {}. Essa proteína pesa no total: {} Da e possui {} aminoácidos de comprimento. Para tirar a dúvida observamos se a proteína em questão obtinha cisteína em sua composição e chegamos a conclusão que esta afirmativa é {}.".format(dna_seq, proteina, peso.molecular_weight() , tamanho, tem_cisteina))
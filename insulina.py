from Bio.Seq import Seq
from Bio.SeqUtils import ProtParam

# Sequência de DNA da Insulina
dna_seq = Seq("TTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACC")

# DNA da Insulina convertido em proteína
proteina = dna_seq.translate()

# Tamanho da proteína
tamanho = len(proteina)

# Peso molecular da Insulina
peso = ProtParam.ProteinAnalysis(str(proteina))

# Verficação de Cisteína (C) na Insulina
tem_cisteina = bool("C" in proteina)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

print('A sequência de DNA da insulina é dada pela sequência {}, sendo sua proteína a seguinte: {}. O tamanho dessa proteína é de {} e seu peso {}Da. Quando perguntado se em sua sequência existe a presença de Cisteina (C) a resposta é {}'.format(dna_seq, proteina, tamanho, peso.molecular_weight(), tem_cisteina))
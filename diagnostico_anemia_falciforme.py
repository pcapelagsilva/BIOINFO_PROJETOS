from Bio.Seq import Seq
import matplotlib.pyplot as plt

def processar_paciente(nome, seq_dna):
    print("\n-=-=-=-=-=-=-=-=-=-=- PROCESSANDO O LAUDO -=-=-=-=-=-=-=-=-=-=-")

    # 1ª Define a base de referência: Posição do 6° aminoácido - GAG (Ácido Glutâmico)
    gene_ref = "ATGGTGCACCTGACTCCTGAGGAG"

    # 2ª Transcrição e Tradução
    dna_obj = Seq(seq_dna)
    proteina = dna_obj.translate(to_stop=True)

    # 3ª Identificação da Mutação (Screening)
    tem_mutacao = False
    for i, (base_ref, base_pac) in enumerate(zip(gene_ref, seq_dna)):
        if base_ref != base_pac:
            print(f"🚨 MUTAÇÃO DETECTADA 🚨 \nPosição: {i+1} ({base_ref} -> {base_pac})")
            print(60*"-")
            if base_ref == "A" and base_pac == "T":
                print("📋 Diagnóstico 📋: \nCompatível com Hemoglobina S (Drepanocitose).")
                tem_mutacao = True
                print(30*"-=")

    # 4ª Gerar gráfico de qualidade para o Laudo
    bases = ['A', 'T', 'C', 'G']
    valores = [seq_dna.count(b) for b in bases]
    cores = ['royalblue', 'firebrick', 'forestgreen', 'darkorange']
    plt.bar(bases, valores, color=cores)
    plt.title(f"Perfil Genético - Paciente: {nome}")
    plt.show()

while True:
    print("\n" + "="*40)
    print("SISTEMA DE ANALISES DE VARIANTES (HBB)")
    print(40*"=")

    nome = input("\n Digite o nome do Paciente (ou 'sair'): ").strip().capitalize()

    if nome.lower() == "sair":
        print("Encerrando o programa...")
        break

    dna = input("Digite a sequência de DNA: ").strip().upper().replace(" ", "")
    if len(dna) >= 3:
        processar_paciente(nome, dna)
    else:
        print("❌ ERRO ❌ \n Sequência inválida...")

# ------------------ SIMULAÇÃO DE DADOS DO HOSPITAL ------------------
'''paciente = André
sequencia = ATGGTGCACCTGACTCCTGTGGAG

paciente = Pedro
sequencia = ATGCGGATGATCGGATCGATAGCTAGCGATGAC

paciente = Maria
sequencia = ATGCCGTAGCTCGTACGATAGATCATATGCTATAGCTAGATCG'''
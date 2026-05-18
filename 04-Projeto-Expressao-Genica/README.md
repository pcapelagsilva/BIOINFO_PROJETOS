# Gene Expression Analysis

A beginner bioinformatics project focused on gene expression analysis using Python and Linux tools.

This project simulates a simple gene expression workflow commonly found in computational biology and bioinformatics, including data manipulation, statistical analysis, and visualization.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Linux Command Line
- Git & GitHub

## Project Goals

- Practice biological data manipulation
- Perform basic statistical analysis
- Explore gene expression datasets
- Learn Linux command-line workflows
- Integrate Python with bioinformatics-oriented data analysis

## Dataset

The dataset contains simulated gene expression levels for cancer-related genes, including:

- BRCA1
- TP53
- EGFR
- MYC
- KRAS
- HER2
- VEGFA

The goal is to perform exploratory analysis and understand data distribution patterns.

## Analysis Performed

- Dataset loading with Pandas
- Mean calculation
- Variance calculation
- Highest gene expression identification
- Lowest gene expression identification
- Histogram visualization

## Linux Commands Practiced

This project also includes basic Linux-based data manipulation using:

- `grep`
- `cut`
- `wc`
- pipes (`|`)

Examples:

```bash
cut -d "," -f 1 genes_cancer.csv
grep "BRCA" genes_cancer.csv
wc -l genes_cancer.csv
cut -d "," -f 1 genes_cancer.csv | grep "K"
```

## Project Structure

```txt
bioinformatics-gene-expression-analysis/
│
├── genes_cancer_de_mama.csv
├── analise_cancer_de_mama.ipynb
├── README.md
```

## Installation

Install dependencies:

```bash
pip install pandas matplotlib
```

## Running the Project

Run the script:

```bash
python analise.py
```

## Learning Outcomes

Through this project, I practiced:

- Basic bioinformatics workflows
- Data manipulation using Python
- Statistical analysis of biological datasets
- Data visualization
- Linux command-line data processing
- Project organization with Git/GitHub

## Future Improvements

Potential next steps include:

- Comparing healthy vs. tumor samples
- Additional statistical analysis
- Boxplots and scatter plots
- More realistic biological datasets
- Transcriptomics-inspired workflows

## Author

Pedro Silva  
Biology student interested in Genetics, Bioinformatics, and Computational Biology.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Análise de Expressão Gênica

Mini projeto de Bioinformática utilizando Python e Linux para análise de expressão gênica relacionada ao câncer.

## Tecnologias utilizadas
- Python
- Pandas
- Matplotlib
- Linux

## Objetivos
- Manipular datasets biológicos
- Realizar análises estatísticas
- Criar visualizações de dados
- Praticar comandos Linux

## Dataset
O dataset contém níveis simulados de expressão gênica de genes relacionados ao câncer.

## Análises realizadas
- Média
- Variância
- Maior expressão gênica
- Menor expressão gênica
- Histograma

## Comandos Linux utilizados
- grep
- cut
- wc
- pipes (|)

## Como executar

Instale as bibliotecas:
```bash
pip install pandas matplotlib

## Autor
Pedro Silva  
Estudante de Biologia interessado em Genética, Bioinformática, e Biologia Computacional
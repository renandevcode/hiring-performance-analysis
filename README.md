#  Sistema de Análise de Dados (Recrutamento & Passageiros)

Este projeto reúne diferentes módulos de análise de dados utilizando Python, com foco em extração de insights a partir de arquivos **Excel** e **CSV**.

O objetivo é aplicar conceitos de análise de dados, manipulação com **Pandas** e geração de métricas úteis para tomada de decisão.

---

##  Objetivo Geral

Desenvolver soluções de análise de dados que permitam:

- Identificar padrões em dados corporativos (RH)
- Avaliar desempenho de fontes de recrutamento
- Analisar comportamento e satisfação de usuários (passageiros)
- Gerar métricas quantitativas e percentuais

---

##  Módulos do Projeto

### 📁 1. Análise de Recrutamento e Performance (Excel)

Este módulo realiza a análise de dados de Recursos Humanos a partir de planilhas Excel.

#### Objetivo
Identificar quais fontes de recrutamento trazem colaboradores com melhor desempenho.

#### ⚙️ Funcionalidades

- Filtrar dados por nível de performance
- Identificar canais de recrutamento utilizados
- Contar contratações por canal
- Gerar ranking dos canais mais eficientes
- Exibir dados formatados no terminal
- Exportar resultados para Excel

####  Tecnologias

- Python  
- Pandas  
- Tabulate  
- OpenPyXL  

---

### 📁 2. Análise de Passageiros e Satisfação (CSV)

Este módulo trabalha com dados de passageiros de companhia aérea a partir de arquivos CSV.

####  Objetivo

Analisar características demográficas e nível de satisfação dos clientes.

#### ⚙️ Funcionalidades

- Filtrar passageiros por gênero e faixa etária  
- Contar quantidade de passageiros por critérios definidos  
- Calcular métricas de satisfação:
  - Total de entrevistas  
  - Quantidade de satisfeitos  
  - Quantidade de neutros/insatisfeitos  
  - Percentuais de satisfação  

####  Lógica Implementada

##### 🔹 Segmentação por idade e gênero
A função percorre o dataset e retorna a quantidade de passageiros dentro de uma faixa etária específica e gênero.

##### 🔹 Análise de satisfação
Cálculo de métricas absolutas e percentuais com base nas respostas dos passageiros.

####  Tecnologias

- Python  
- Pandas  

---

## 📁 Dataset (CSV - Passageiros)

Os dados utilizados neste módulo foram obtidos no Kaggle:

🔗 https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction

### ⚠️ Importante

Os arquivos de dados **não estão incluídos no repositório**.

Para utilizar este módulo:

1. Instale a biblioteca:
```bash
pip install kagglehub
```

2. Baixe o dataset:
```python
import kagglehub

path = kagglehub.dataset_download("teejmahal20/airline-passenger-satisfaction")
print(path)
```

3. Copie os arquivos `.csv` para a pasta:

```
read_csv/airline/
```

---


## 📌 Estrutura do Projeto

```
.
├── read_excel/
├── read_csv/
│   └── airline/
├── data/
├── README.md
├── requirements.txt
└── .gitignore
```

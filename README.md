# Projeto: Provisão de Vendas

Este projeto tem como objetivo prever as vendas do produto "Produto Alfa" utilizando a biblioteca **Prophet**.

## Estrutura do Repositório

- **dados/**
  - **bronze/**: dados brutos em CSV
  - **silver/**: dados tratados (parquet)
  - **gold/**: dados modelados prontos para análise
- **notebooks/**
  - `eda.ipynb`: exploração e visualização de dados
  - `modelagem.ipynb`: criação e treino do modelo Prophet
- **src/**
  - `limpeza.py`: scripts de limpeza de dados
  - `silver_to_gold.py`: transformação do silver para gold
- **docs/**: documentação do projeto (ex: EDA_docs.md)
- **modelos/**: modelos salvos para deploy futuro
- **warnings.log**: logs de processamento
- **venv/**: ambiente virtual Python

## Fluxo do Projeto

1. Coleta dos dados (`dados/bronze`)
2. Limpeza e transformação (`src/limpeza.py`) → (`dados/silver`)
3. Treinamento do modelo Prophet (`notebooks/modelagem.ipynb`) → (`dados/gold`)
4. Análise exploratória (`notebooks/eda.ipynb`)
5. Armazenamento em Parquet para eficiência
6. Deploy futuro: arquitetura para nuvem e monitoramento

Fluxo do Projeto

Coleta dos dados: armazenados em dados/bronze/
Limpeza e transformação: src/limpeza.py → dados/silver/
Treinamento do modelo Prophet: notebooks/modelagem.ipynb → dados/gold/
Análise exploratória: notebooks/eda.ipynb
Armazenamento em Parquet para eficiência
Deploy futuro: arquitetura para nuvem e monitoramento

## Como Rodar

```bash
# Ativar o ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\Activate.ps1  # Windows PowerShell

# Instalar dependências
pip install -r requirements.txt

# Rodar limpeza e transformação
python src/limpeza.py
python src/silver_to_gold.py

Requisitos Python
numpy>=1.25
pandas>=2.1
prophet>=1.1
matplotlib>=3.8
seaborn>=0.13
scikit-learn>=1.3


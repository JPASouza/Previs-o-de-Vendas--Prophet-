📦 Projeto: Provisão de Vendas
│
├─ dados/
│   ├─ bronze/           <- dados brutos (CSV)
│   │   └─ vendas_produto_alfa.csv
│   ├─ silver/           <- dados tratados (Parquet)
│   │   └─ vendas_limpos.parquet
│   └─ gold/             <- dados modelados (Parquet)
│       └─ vendas_modelo.parquet
│
├─ notebooks/
│   ├─ eda.ipynb         <- exploração de dados
│   └─ modelagem.ipynb   <- criação e treino do modelo Prophet
│
├─ src/
│   ├─ limpeza.py         <- scripts de limpeza de dados
│   └─ silver_to_gold.py  <- transformação do silver para gold
│
├─ modelos/              <- modelos salvos (futuro)
├─ docs/                 <- documentação (EDA_docs.md)
├─ warnings.log          <- logs de warnings
└─ venv/                 <- ambiente virtual

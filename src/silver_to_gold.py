import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__). resolve().parents[1]
SILVER = BASE_DIR / 'dados' / 'prata' / 'vendas_limpos.parquet'
GOLD = BASE_DIR / 'dados' / 'gold' / 'vendas_modelo.parquet'

df = pd.read_parquet(r'C:\Users\João Pedro\Desktop\previsao_vendas\dados\silver\vendas_limpos.parquet')

#Criar colunas MM e Defasagem
df = df.sort_values('data')
df['media_movel_7d'] = df['vendas'].rolling(window=7).mean()
df['lag_1'] = df['vendas'].shift(1)
df['lag_7'] = df['vendas'].shift(7)

#Separando ultimos 30 dias como conj. de teste
df['conjunto'] = 'treino'
df.loc[df['data'] >= df['data'].max() - pd.Timedelta(days=30), 'conjunto'] = 'teste'

df.to_parquet(GOLD, index=False)

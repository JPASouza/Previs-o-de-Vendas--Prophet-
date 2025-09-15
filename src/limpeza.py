import pandas as pd 

df = pd.read_csv(r'C:\Users\João Pedro\Desktop\previsao_vendas\dados\bronze\vendas_produto_alfa.csv')

#Analisando os tipos de dados e valores Null
print(df.info())
print(df.isnull().sum())

#Conversão para DateTime
df['data'] = pd.to_datetime(df['data'], errors = 'coerce')

#Confirmando bool
df['feriado_nacional'] = df['feriado_nacional'].astype(bool)
df['em_promocao'] = df['em_promocao'].astype(bool)

#Jogar 0 para valores (NA)
df['vendas'] = df['vendas'].fillna(0)

df.to_parquet('dados/silver/vendas_limpos.parquet', index = False)




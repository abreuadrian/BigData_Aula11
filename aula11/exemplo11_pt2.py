#Ex02.:
import pandas as pd

#importando dados csv

df_dados = pd.read_csv('./aula11/base1.csv', sep=';')

print(df_dados.head(50))
print('=== Maior preço ===')
print(f'R$ {df_dados['preco'].max():,.2f}')
print('\n=== Menor preço ===')
print(f'R$ {df_dados['preco'].min():,.2f}')
print('\n=== Média de preço ===')
print(f'R$ {df_dados['preco'].mean():,.2f}') #round(x, 2)
print('\n=== Total dos preços ===')
print(f'R$ {df_dados['preco'].sum():,.2f}')
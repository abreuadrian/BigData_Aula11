#Ex01.: 
import pandas as pd 

dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente'],
    'salários': [2500, 1800, 7500]
}

print(dados)
print(type(dados)) #Mostra o tipo de dado 

# Usando pandas 
df_dados = pd.DataFrame(dados)
print(df_dados)

print('Printando os cargos\n')
print(df_dados['cargos'])
print('Printando os salários\n')
print(df_dados['salários'])
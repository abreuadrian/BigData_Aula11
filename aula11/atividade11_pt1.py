import pandas as pd
from helper.utilities import error_msg, time_clear, clean


clean()

list_filmes = []
for i in range(3):
    dict_filmes = {}
    dict_filmes['Nome'] = input('Informe o nome do filme: ').capitalize()
    time_clear(1)
    while True:
        try:
            dict_filmes['Ano de Lançamento'] = int(input('Informe o ano de lançamento: '))
            break
        except ValueError:
            error_msg(1, 'Erro. Insira um número válido')
    time_clear(1)
    dict_filmes['Gênero'] = input('Informe o gênero do filme: ').capitalize()
    time_clear(1)
    list_filmes.append(dict_filmes)

df_dados = pd.DataFrame(list_filmes)
print(df_dados)
import pandas as pd

# Carregar dataset
url = 'https://raw.githubusercontent.com/higoramario/univesp-com360-mineracao-dados/main/dados-covid-limpeza.csv'
casos_covid = pd.read_csv(url)

# Exploração inicial
casos_covid.head(20)
casos_covid.info()
casos_covid.describe()

# ---------------------------
# Limpeza e padronização
# ---------------------------

# Padronizar 'uf' em maiúsculo
casos_covid['uf'] = casos_covid['uf'].str.upper()

# Preenche os valores faltantes da coluna 'uf' usando forward fill (ffill),
# ou seja, cada NaN é substituído pelo último valor não nulo acima na mesma coluna
casos_covid['uf'] = casos_covid['uf'].ffill()

# Preencher valores faltantes em 'idade' com a média arredondada
casos_covid['idade'] = casos_covid['idade'].fillna(round(casos_covid['idade'].mean()))

# Preenche os valores faltantes da coluna 'renda' usando backward fill (bfill),
# ou seja, cada NaN é substituído pelo próximo valor não nulo abaixo na mesma coluna
casos_covid['renda'] = casos_covid['renda'].bfill()


# ---------------------------
# Conferir resultados
# ---------------------------
print("\nDistribuição por UF:")
print(casos_covid['uf'].value_counts())

print("\nDistribuição por idade:")
print(casos_covid['idade'].value_counts())

print("\nDistribuição por renda:")
print(casos_covid['renda'].value_counts())

print("\nDistribuição por vacina:")
print(casos_covid['vacina'].value_counts())


# Resultado
casos_covid.info()
casos_covid.head(len(casos_covid))



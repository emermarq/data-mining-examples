import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

sb.set(rc={'figure.figsize': (15, 8)})

url = 'https://dados.educacao.sp.gov.br/sites/default/files/Quantidade%20de%20alunos%20por%20tipo%20de%20ensino%20da%20rede%20estadual_2021_1%C2%B0SEMESTRE.csv'

# Ler o CSV diretamente da web
escolas = pd.read_csv(url, sep=';')  # O separador é ; e encoding pode ser latin1

# Mostrar as 10 primeiras linhas
print(escolas.head(20))

# Informações gerais sobre o dataframe
print(escolas.info())

filtro_escolas = escolas[escolas['ANOS INICIAIS'] > 0]
sb.displot(filtro_escolas['ANOS INICIAIS'], bins=10)
plt.show()

filtro_escolas = escolas[escolas['ANOS INICIAIS'] > 0]
sb.boxplot(y=filtro_escolas['ANOS INICIAIS'])
plt.show()

filtro_escolas = escolas[escolas['ANOS FINAIS'] > 0]
sb.displot(filtro_escolas['ANOS FINAIS'], bins=10)
plt.show()

filtro_escolas = escolas[escolas['CLASSES ESPECIAIS'] > 0]
sb.displot(filtro_escolas['CLASSES ESPECIAIS'], bins=10)
plt.show()

fundamental_inicias = escolas['ANOS INICIAIS'].sum()
fundamental_finais = escolas['ANOS FINAIS'].sum()
especiais = escolas['CLASSES ESPECIAIS'].sum()

filtro_escolas = escolas[escolas['ANOS INICIAIS'] > 0]
sb.boxplot(y=filtro_escolas['ANOS INICIAIS'])
plt.show()

filtro_escolas = escolas[(escolas['ANOS INICIAIS'] > 0)  & (escolas['ANOS FINAIS'] > 0)]
sb.scatterplot(x=filtro_escolas['ANOS INICIAIS'], y=escolas['ANOS FINAIS'] )
plt.show()

print(fundamental_inicias + fundamental_finais + especiais )

alunos = [fundamental_inicias, fundamental_finais, especiais]
periodo = ['fundamental anos iniciais', 'fundamental anos finais', 'especiais']
plt.pie(alunos, labels=periodo, autopct='%0.0f%%')
plt.show()

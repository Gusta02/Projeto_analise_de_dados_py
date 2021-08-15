# Passo 1: Importar a base de dados pro python

import pandas as pd
import plotly.express as px 

tabela = pd.read_csv ("telecom_users.csv")
#display(tabela)


# Passo 2: Visualizar a base
#   Entender quais informações vc tem disponivel
#   Descobrir as cagadas da base de dados.

tabela = tabela.drop("Unnamed: 0", axis=1) # 0 é linha e 1 é coluna
#display(tabela)

# Passo 3: Tratamento da base de dados
#   Valores que são números mas que o python acha que são texto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # transforma a coluna de texto em numero e ignora os erros

#   Valores que estão vazios
#       Coluna Vazia
tabela = tabela.dropna(how="all", axis=1) # all quando quer excluir uma coluna inteiramente vazia
#       Linhas Vazias
tabela = tabela.dropna(how="any", axis=0)# any exclui somente colunas que tem pelo menos 1 valor vazio


#print(tabela.info())


# Passo 4: Análise exploratoria --> Analise Geral --> Identificar o motivo dos clientes cancelarem
display(tabela["Churn"].value_counts()) #conta os sim e não

display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #conta os sim e não

# Passo 5: Olhando as colunas da nossa base de dados --> identidicar o motivo dos clientes cancelarem

for coluna in tabela.columns: #Executa o codigo varias vezes, nesse caso ele executa ate terminar as colunas
    #print(coluna)


    grafico = px.histogram(tabela, x=coluna, color="Churn") #Cria o grafico; Color define a cor do gráfico
    grafico.show() #mostra o grafico





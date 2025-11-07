import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar base original
file_path = "/home/pedro/Estudos/Estatistica/projetoEstatistica/Desempenho_Alunos.xlsx"   # coloque aqui a versão bruta, sem tratamento
df = pd.read_excel(file_path)

# Verificar dados ausentes
print("Valores ausentes por coluna:")
print(df.isnull().sum())

# Opcional: remover ou preencher valores ausentes
df = df.dropna()   # ou df.fillna(df.mean(), inplace=True)

# Transformar variáveis categóricas em numéricas (one-hot encoding)
df = pd.get_dummies(df, columns=["atividade_extracurricular", "nivel_socioeconomico"], drop_first=True)

# Separar variáveis numéricas para padronização
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Conferir tabela final tratada
print(df.head())

# Salvar a tabela tratada
df.to_excel("Desempenho_Alunos_tratado.xlsx", index=False)
print("Tabela tratada salva como 'Desempenho_Alunos_tratado.xlsx'")

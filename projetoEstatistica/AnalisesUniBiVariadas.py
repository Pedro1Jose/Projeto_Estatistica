import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Carregar o dataset
file_path = "Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Exibir as primeiras linhas para verificar se o carregamento está correto
print(df.head())

# Identificar variáveis numéricas para correlação
# As colunas booleanas serão convertidas para int (True=1, False=0)
colunas_numericas = df.select_dtypes(include=[np.number, 'bool']).columns.tolist()

# Converter colunas booleanas para int
for col in df.select_dtypes(include='bool').columns:
    df[col] = df[col].astype(int)

# Separar variáveis explicativas (X) e a variável resposta (y)
X = df.drop('desempenho', axis=1)
y = df['desempenho']

# Definir as variáveis numéricas e categóricas
variaveis_numericas = ['idade', 'horas_estudo', 'frequencia', 'motivacao', 'notas_anteriores', 'sono']
variaveis_categoricas = ['atividade_extracurricular', 'nivel_socioeconomico']

# Análise Univariada da variável resposta 'desempenho'
plt.figure(figsize=(8, 6))
sns.histplot(df['desempenho'], kde=True)
plt.title('Distribuição da Variável Desempenho')
plt.xlabel('Desempenho')
plt.ylabel('Frequência')
plt.show()

# Análise Univariada das variáveis explicativas numéricas
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
fig.suptitle('Distribuição das Variáveis Explicativas Numéricas', fontsize=16)

for i, col in enumerate(variaveis_numericas):
    sns.histplot(df[col], kde=True, ax=axes[i//3, i%3])
    axes[i//3, i%3].set_title(col)
    
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Análise Univariada das variáveis explicativas categóricas
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
fig.suptitle('Distribuição das Variáveis Explicativas Categóricas', fontsize=16)

for i, col in enumerate(variaveis_categoricas):
    sns.countplot(x=df[col], ax=axes[i])
    axes[i].set_title(col)
    
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Convertendo colunas booleanas para inteiros (1 e 0)
for col in df.columns:
    if df[col].dtype == 'bool':
        df[col] = df[col].astype(int)
# Calcular a correlação entre todas as variáveis e a variável resposta 'desempenho'
correlacao_com_desempenho = df.corr()['desempenho'].sort_values(ascending=False)
print('Correlação com a variável "desempenho":')
print(correlacao_com_desempenho)

# Calcular a matriz de correlação
matriz_correlacao = df.corr()

# Criar o heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matriz de Correlação das Variáveis')
plt.show()
# Análise Exploratória de Dados (EDA)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
file_path = "Desempenho_Alunos_tratado.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

print("VISÃO GERAL DA BASE")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificar dados ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Distribuição das variáveis numéricas (histogramas)
df.hist(figsize=(12,8), bins=15, edgecolor="black")
plt.suptitle("Distribuição das variáveis numéricas", fontsize=14)
plt.show()

# Boxplots para detectar outliers
plt.figure(figsize=(12,6))
df.select_dtypes(include=["float64", "int64"]).boxplot()
plt.title("Boxplots - Detecção de Outliers")
plt.xticks(rotation=45)
plt.show()

# Matriz de correlação
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()

# Sugerir correções na base
# Exemplo de identificação de outliers via IQR
def detectar_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = df[(df[col] < limite_inferior) | (df[col] > limite_superior)]
    return outliers

print("\nPossíveis outliers detectados:")
for col in df.select_dtypes(include=["float64", "int64"]).columns:
    outliers = detectar_outliers(col)
    if not outliers.empty:
        print(f"- Variável {col}: {len(outliers)} outliers")

print("\nSugestões de correção:")
print("- Tratar valores ausentes (imputação com média/mediana ou remoção de linhas).")
print("- Avaliar se os outliers são erros de digitação/medição → se sim, corrigir ou remover.")
print("- Normalizar ou padronizar variáveis numéricas para modelos de ML.")
print("- Garantir que variáveis categóricas estejam codificadas corretamente (one-hot encoding).")

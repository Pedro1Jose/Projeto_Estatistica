import pandas as pd
import matplotlib.pyplot as plt

# Carregar base de dados
file_path = "/home/pedro/Estudos/Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Selecionar apenas variáveis numéricas
num_vars = data.select_dtypes(include=["float64", "int64"])

# --- Boxplots ---
plt.figure(figsize=(12,6))
num_vars.boxplot()
plt.title("Boxplot das variáveis numéricas")
plt.xticks(rotation=45)
plt.show()

# --- Histogramas ---
num_vars.hist(figsize=(12,8), bins=15, edgecolor="black")
plt.suptitle("Histogramas das variáveis numéricas", fontsize=14)
plt.show()

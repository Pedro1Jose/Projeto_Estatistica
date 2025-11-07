# Regressão Linear Simples (MRLS)
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carregar base de dados
file_path = "/home/pedro/Estudos/Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Definir variáveis
X_mrls = data[["horas_estudo"]]   # variável independente
y = data["desempenho"]            # variável dependente

# Treinar modelo
model_mrls = LinearRegression()
model_mrls.fit(X_mrls, y)

# Predições
y_pred = model_mrls.predict(X_mrls)

# Resultados
print("Regressão Linear Simples (MRLS)")
print(f"Equação: desempenho = {model_mrls.coef_[0]:.3f} * horas_estudo + {model_mrls.intercept_:.3f}")
print(f"R²: {model_mrls.score(X_mrls, y):.3f}")

# --- Gráfico ---
plt.scatter(X_mrls, y, color="blue", label="Dados reais")
plt.plot(X_mrls, y_pred, color="red", linewidth=2, label="Linha de regressão")
plt.xlabel("Horas de estudo")
plt.ylabel("Desempenho")
plt.title("Regressão Linear Simples")
plt.legend()
plt.show()
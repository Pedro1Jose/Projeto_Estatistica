# Regressão Linear Múltipla (MRLM)
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carregar base de dados
file_path = "/home/pedro/Estudos/Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx"
data = pd.read_excel(file_path, sheet_name="Sheet1")

# Definir variáveis (todas numéricas, exceto a dependente)
X_mrlm = data.drop(columns=["desempenho", "atividade_extracurricular", "nivel_socioeconomico"])
y = data["desempenho"]

# Treinar modelo
model_mrlm = LinearRegression()
model_mrlm.fit(X_mrlm, y)

# Predições e resíduos
y_pred = model_mrlm.predict(X_mrlm)
residuos = y - y_pred

# Resultados
print("Regressão Linear Múltipla (MRLM)")
print("Equação: desempenho = ", end="")
for col, coef in zip(X_mrlm.columns, model_mrlm.coef_):
    print(f"{coef:.3f} * {col} + ", end="")
print(f"{model_mrlm.intercept_:.3f}")

print(f"R²: {model_mrlm.score(X_mrlm, y):.3f}")

# --- Gráfico de resíduos ---
plt.scatter(y_pred, residuos, color="purple")
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Valores preditos")
plt.ylabel("Resíduos")
plt.title("Resíduos do Modelo de Regressão Múltipla")
plt.show()
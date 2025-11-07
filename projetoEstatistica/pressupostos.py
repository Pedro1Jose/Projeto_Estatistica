import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Exemplo: carregar os dados
df = pd.read_excel("Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx")

# Separar X e y
y = df['notas_anteriores']  # variável resposta (exemplo)
X = df.drop(columns=['notas_anteriores'])

# Adicionar constante para o intercepto
X = sm.add_constant(X)
X = pd.get_dummies(X, drop_first=True)  # cria variáveis dummy e evita multicolinearidade
X = X.astype(float)
y = y.astype(float)

# Ajustar modelo de regressão linear
melhorModelo = sm.OLS(y, X).fit()

vif_data = pd.DataFrame()
vif_data["Variável"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)


# ----- Verificação de pressupostos -----

residuos = melhorModelo.resid
y_pred = melhorModelo.fittedvalues

# 1. Linearidade
plt.figure(figsize=(6,4))
sns.scatterplot(x=y_pred, y=residuos)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Valores Ajustados")
plt.ylabel("Resíduos")
plt.title("Verificação de Linearidade")
plt.show()

# 2. Normalidade dos resíduos
plt.figure(figsize=(6,4))
sns.histplot(residuos, kde=True)
plt.title("Distribuição dos Resíduos")
plt.show()

shapiro_test = shapiro(residuos)
print(f"Shapiro-Wilk Test: Estatística={shapiro_test.statistic:.4f}, p-valor={shapiro_test.pvalue:.4f}")

# 3. Homocedasticidade
plt.figure(figsize=(6,4))
sns.scatterplot(x=y_pred, y=residuos)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Valores Ajustados")
plt.ylabel("Resíduos")
plt.title("Verificação de Homocedasticidade")
plt.show()

# 4. Independência dos resíduos
dw = durbin_watson(residuos)
print(f"Durbin-Watson: {dw:.4f}")

# 5. Multicolinearidade
vif_data = pd.DataFrame()
vif_data["Variável"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("\n--- VIF ---")
print(vif_data)

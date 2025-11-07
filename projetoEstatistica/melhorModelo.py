import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# 1. Carregar o dataset do arquivo Excel
file_path = "Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 2. Separar variáveis explicativas (X) e a variável resposta (y)
X = df.drop('desempenho', axis=1)
y = df['desempenho']

# 3. Identificar e processar variáveis
variaveis_numericas = X.select_dtypes(include=np.number).columns.tolist()
variaveis_categoricas = X.select_dtypes(include='object').columns.tolist()

# Converter colunas numéricas que possam estar como object
for col in variaveis_numericas:
    X[col] = pd.to_numeric(X[col], errors='coerce')

# Tratar valores nulos (substituir por média)
X[variaveis_numericas] = X[variaveis_numericas].fillna(X[variaveis_numericas].mean())

# Padronizar as variáveis numéricas
scaler = StandardScaler()
X[variaveis_numericas] = scaler.fit_transform(X[variaveis_numericas])

# Aplicar One-Hot Encoding nas variáveis categóricas
X = pd.get_dummies(X, columns=variaveis_categoricas, drop_first=True)

# Adicionar uma constante (intercepto)
X = sm.add_constant(X)

# Certificar que todos os dados são numéricos
X = X.astype(float)

# 4. Processo de Eliminação Retroativa
variaveis_a_manter = X.columns.tolist()
modelo_final = None

while True:
    X_atual = X[variaveis_a_manter]
    modelo = sm.OLS(y, X_atual).fit()
    
    # Encontrar variável com maior p-value (exceto constante)
    p_valores = modelo.pvalues.drop('const')
    maior_p_valor = p_valores.max()
    variavel_a_remover = p_valores.idxmax()
    
    if maior_p_valor > 0.05:
        print(f"Removendo '{variavel_a_remover}' (p-value: {maior_p_valor:.4f})")
        variaveis_a_manter.remove(variavel_a_remover)
    else:
        print("\nTodas as variáveis restantes são significativas (p < 0.05).")
        modelo_final = modelo
        break

# 5. Resumo do modelo final
print("\n--- Resumo do Modelo Final ---")
print(modelo_final.summary())


# Definir dois novos conjuntos de valores para as variáveis explicativas
# Atenção: deve conter todas as variáveis que ficaram no modelo_final, exceto a constante
xh1 = X[variaveis_a_manter].iloc[0].copy()  # Exemplo: primeira linha original
xh2 = X[variaveis_a_manter].iloc[1].copy()  # Exemplo: segunda linha original

# Garantir que a constante está presente
xh1['const'] = 1
xh2['const'] = 1

# Criar DataFrame com as observações
X_novas = pd.DataFrame([xh1, xh2])

# 1. Previsões pontuais e intervalos de confiança da média esperada E(Y|X)
pred_media = modelo_final.get_prediction(X_novas)
intervalo_media = pred_media.summary_frame(alpha=0.05)  # 95% de confiança

print("\n--- Previsões Pontuais e Intervalos de Confiança da Média Esperada ---")
print(intervalo_media[['mean', 'mean_ci_lower', 'mean_ci_upper']])

# 2. Previsões pontuais e intervalos de predição para novas observações Yh
intervalo_predicao = pred_media.summary_frame(alpha=0.05)  # mesmo objeto já possui 'obs_ci'
print("\n--- Previsões Pontuais e Intervalos de Predição para Novas Observações ---")
print(intervalo_predicao[['mean', 'obs_ci_lower', 'obs_ci_upper']])

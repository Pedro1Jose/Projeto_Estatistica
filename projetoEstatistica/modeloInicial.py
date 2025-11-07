import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler

# 1. Carregar o dataset
file_path = "Estatistica/projetoEstatistica/Desempenho_Alunos_tratado.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 2. Separar variáveis explicativas (X) e variável resposta (y)
X = df.drop('desempenho', axis=1)
y = df['desempenho']

# 3. Identificar variáveis numéricas e categóricas
variaveis_numericas = ['idade', 'horas_estudo', 'frequencia', 'motivacao', 'notas_anteriores', 'sono']
variaveis_categoricas = [col for col in X.columns if col not in variaveis_numericas]

# 4. Tratar valores ausentes antes da padronização e conversão
X[variaveis_numericas] = X[variaveis_numericas].fillna(X[variaveis_numericas].mean())
for col in variaveis_categoricas:
    X[col] = X[col].fillna('Nao Informado')  # ou outro valor padrão

# 5. Padronizar variáveis numéricas
scaler = StandardScaler()
X[variaveis_numericas] = scaler.fit_transform(X[variaveis_numericas])

# 6. Converter variáveis categóricas para 0 e 1 (ou dummies)
for col in variaveis_categoricas:
    if X[col].dtype == 'object':
        # Supondo categorias 'Sim' e 'Não'
        X[col] = X[col].map({'Sim': 1, 'Não': 0})
        # Valores que não forem 'Sim'/'Não' se tornam NaN, então substituímos por 0
        X[col] = X[col].fillna(0)
    else:
        X[col] = X[col].astype(int)

# 7. Adicionar constante
X = sm.add_constant(X)

# 8. Garantir que não existam inf ou NaN
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.fillna(0, inplace=True)

# 9. Calcular VIF
vif_data = pd.DataFrame()
vif_data['variavel'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

# 10. Exibir resultados
print('Fator de Inflação da Variância (VIF):')
print(vif_data.sort_values(by='VIF', ascending=False))

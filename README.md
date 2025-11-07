# 📊 Projeto de Estatística Aplicada à Computação

**Curso:** Ciência da Computação — Universidade Federal de Campina Grande (UFCG)  
**Disciplina:** Estatística Aplicada à Computação  
**Autor:** Pedro José da Silva Filho  

---

## 🧠 Descrição Geral

Este projeto tem como objetivo **analisar fatores que influenciam o desempenho dos alunos**, a partir de um conjunto de dados contendo **1.998 observações**.  
A análise envolve variáveis relacionadas ao **perfil pessoal**, **hábitos de estudo**, **condições socioeconômicas** e **aspectos comportamentais** dos estudantes.

O foco principal é compreender como essas variáveis afetam o **desempenho escolar** e construir um modelo de regressão linear que permita **prever o desempenho esperado** com base em diferentes perfis de alunos.

---

## 🧩 Estrutura dos Dados

A base de dados final contém **1.930 observações** após o pré-processamento (remoção de outliers).  
As variáveis analisadas são:

| Variável | Descrição | Tipo / Unidade |
|-----------|------------|----------------|
| `idade` | Idade do aluno | Anos |
| `horas_estudo` | Horas semanais de estudo | Horas/semana |
| `frequencia` | Frequência escolar | Percentual (%) |
| `atividade_extracurricular` | Participação em atividades extracurriculares | Categórica ("Sim"/"Não") |
| `nivel_socioeconomico` | Condição socioeconômica | Categórica ("Baixo", "Médio", "Alto") |
| `motivacao` | Nível de motivação para os estudos | Escala numérica |
| `notas_anteriores` | Média das notas anteriores | Escala 0–10 |
| `sono` | Horas de sono por noite | Horas/noite |
| `desempenho` | Variável resposta (rendimento escolar) | Escala numérica |

---

## 🔍 Análise Exploratória (EDA)

- Remoção de **67 observações atípicas** via critério IQR (1.5×IQR)  
- Imputação de valores ausentes:
  - Numéricos → média
  - Categóricos → moda  
- Padronização das variáveis numéricas (Z-score)
- Nenhum valor ausente após o pré-processamento
- Visualizações por **boxplots**, **heatmaps** e **matriz de correlação**

Principais descobertas:
- **`notas_anteriores`** e **`motivacao`** têm as maiores correlações positivas com o desempenho.  
- Não há **multicolinearidade significativa** (VIF baixo).

---

## ⚙️ Modelagem Estatística

O modelo inicial foi uma **Regressão Linear Ordinária (OLS)** incluindo todas as variáveis explicativas.  
Posteriormente foi aplicada **seleção stepwise backward** (remoção com p > 0.10) para obter um modelo mais parcimonioso.

### Principais resultados:
- Variáveis significativas: `motivacao` e `horas_estudo`  
- Ambas correlacionadas positivamente com o desempenho dos alunos  
- Modelo final apresentou **bom ajuste** e **poucos parâmetros**, mantendo poder explicativo

---

## ✅ Validação dos Pressupostos do MRLM

| Pressuposto | Resultado | Ação |
|--------------|------------|-------|
| Normalidade dos resíduos | Aceitável (Shapiro, QQ-plot) | Nenhuma |
| Homoscedasticidade | Violada (Breusch–Pagan p<0.05) | Erros padrão robustos (HC3) |
| Independência dos resíduos | OK (Durbin–Watson ≈ 2.11) | Nenhuma |
| Multicolinearidade | VIF baixo | Nenhuma |

> O modelo final usa **erros padrão robustos** para corrigir heterocedasticidade e manter inferência confiável.

---

## 📈 Previsões e Interpretação

Foram realizadas previsões pontuais e intervalos de confiança/predição para dois conjuntos simulados de variáveis (`xh1`, `xh2`):

- **Previsão pontual da média esperada (E[Y|X])** → indica o desempenho médio esperado de alunos com determinado perfil.
- **Intervalo de confiança (95%)** → mostra a faixa provável da média real.
- **Intervalo de predição (95%)** → mostra a faixa provável para o desempenho de um aluno específico.

Essas análises permitem **identificar perfis de alunos com maiores ou menores expectativas de desempenho**, auxiliando estratégias educacionais e de suporte ao aprendizado.

---

## 📂 Estrutura do Projeto

Estatistica/
│
├── modeloInicial.py # Ajuste do modelo OLS completo
├── melhorModelo.py # Modelo final otimizado (stepwise)
├── dados.csv # Base de dados original (não incluída publicamente)
├── analise_exploratoria.ipynb # Notebooks com visualizações e EDA
└── README.md # Este arquivo

---

## 🧾 Conclusão

O modelo final mostrou-se **estatisticamente consistente** e **teoricamente coerente**, destacando a importância da **motivação** e das **horas de estudo** no desempenho acadêmico.  
A análise fornece insights relevantes sobre fatores que influenciam o rendimento escolar e pode ser expandida para análises mais complexas em contextos educacionais.

---

## 🧑‍💻 Autor

**Pedro José da Silva Filho**  
Discente de Ciência da Computação — UFCG  
Disciplina: Estatística Aplicada à Computação  
Ano: 2025.1

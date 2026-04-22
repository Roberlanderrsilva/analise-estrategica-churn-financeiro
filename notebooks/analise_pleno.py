import pandas as pd

# Carregando os dados
df = pd.read_csv('data/BankChurners.csv')
df = df.iloc[:, :-2] # Limpeza de colunas desnecessárias

# 1. Taxa de Churn Geral
churn_count = df['Attrition_Flag'].value_counts(normalize=True) * 100

# 2. Visão por Gênero (Métrica de CRM)
churn_por_genero = df.groupby('Gender')['Attrition_Flag'].value_counts(normalize=True).unstack() * 100

# 3. Visão por Limite de Crédito (Métrica Financeira)
limite_medio = df.groupby('Attrition_Flag')['Credit_Limit'].mean()

print("=== RELATÓRIO ESTRATÉGICO INICIAL ===")
print(f"\n1. TAXA DE CHURN GERAL: {churn_count['Attrited Customer']:.2f}%")
print("\n2. CHURN POR GÊNERO (%):")
print(churn_por_genero)
print("\n3. LIMITE DE CRÉDITO MÉDIO (Fiel vs Churn):")
print(limite_medio)
print("\n=====================================")

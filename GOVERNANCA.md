# ⚖️ Relatório de Governança e Proteção de Dados (LGPD)

## 1. Objetivo
Este documento descreve as medidas de segurança e conformidade adotadas no projeto de Análise de Churn Bancário, garantindo a privacidade dos titulares conforme a Lei 13.709/2018 (LGPD).

## 2. Tratamento de Dados e Anonimização
Para este projeto, foram aplicadas técnicas de **pseudonimização** e **anonimização**:
- **Nomes e IDs:** Substituídos por chaves numéricas aleatórias.
- **Dados Sensíveis:** Informações de contato direto foram removidas da base final.
- **Princípio da Necessidade:** Apenas dados relevantes para o cálculo de Churn (como score de crédito e saldo) foram mantidos.

## 3. Base Legal
O tratamento desses dados para fins de análise estatística e inteligência de negócio fundamenta-se no **Legítimo Interesse** do controlador (Art. 7º, IX da LGPD), visando a melhoria dos serviços e retenção de clientes.

## 4. Segurança da Informação
O dashboard interativo foi configurado com acesso de "Apenas Visualização" para evitar vazamentos ou alterações na base de dados original.

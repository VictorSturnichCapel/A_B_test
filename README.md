# 📊 A/B Teste Simples com Python

Este repositório contém um exemplo prático e comentado de como realizar um **teste A/B estatístico** usando Python, com geração de dados simulados para uma campanha digital.


---

## 🔍 Sobre o Projeto

A ideia é comparar a **taxa de conversão** entre dois grupos (A e B) de usuários que visualizaram versões diferentes de uma campanha, determinando se a diferença observada é estatisticamente significativa.

---

## ⚙️ O que o código faz?

1. **Gera dados simulados** para dois grupos de usuários (A e B), com taxas de conversão diferentes (`20%` e `25%`).
2. **Salva os dados** em um arquivo `.csv`.
3. **Lê os dados** e agrupa os usuários conforme sua versão da campanha.
4. **Calcula conversões** por grupo.
5. **Executa um teste de hipótese (Z-teste)** para verificar se a diferença de conversão é significativa.
6. **Exibe o resultado** do teste com p-valor e interpretação.

---

## 📁 Estrutura dos Dados

Cada linha do dataset representa um usuário com as seguintes colunas:

- `user_id`: identificador único do usuário
- `group`: grupo de experimento (`A` ou `B`)
- `shown`: flag indicando que o anúncio foi exibido (fixo em 1)
- `clicked`: flag binária indicando se o usuário converteu (1 = sim, 0 = não)

---

## 🧪 Função `ab_test`

ab_test(n_A, conv_A, n_B, conv_B, alpha=0.05)

---

## Parâmetros:

n_A: número de usuários no grupo A

conv_A: número de conversões no grupo A

n_B: número de usuários no grupo B

conv_B: número de conversões no grupo B

alpha: nível de significância (padrão: 5%)

A função utiliza a proporção combinada para estimar o erro padrão e aplica o Z-teste bicaudal. O resultado indica se há ou não diferença estatisticamente significativa entre os grupos.

---

## 📦 Requisitos

pandas

numpy

scipy

---

## 📈 Exemplo de saída

Grupo A - Conversão: 20.27% (2027/10000)

Grupo B - Conversão: 25.09% (2509/10000)

Z = 6.8555, P = 0.0000

✅ Diferença significativa entre os grupos!

---

## 📌 Observação
Esse código é uma simulação, útil para fins educativos, testes e validações de modelos de teste A/B.

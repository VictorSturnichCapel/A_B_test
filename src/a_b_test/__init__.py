import pandas as pd
import numpy as np
from scipy import stats

'''
🔹 Define a função ab_test, que recebe:

n_A: número de usuários do grupo A

conv_A: número de conversões no grupo A

n_B: número de usuários do grupo B

conv_B: número de conversões no grupo B

alpha: nível de significância (padrão é 0.05 = 5%)
'''
# Função de A/B test
def ab_test(n_A, conv_A, n_B, conv_B, alpha=0.05):
    # Calcula a taxa de conversão do grupo A (conversões dividido pelo total de usuários).
    p_A = conv_A / n_A
    p_B = conv_B / n_B
    # Calcula a taxa de conversão combinada ("pooled proportion") dos dois grupos juntos.
    # Isso é usado para estimar a variância sob a hipótese nula (de que A e B são iguais).
    p_pool = (conv_A + conv_B) / (n_A + n_B)
    # Calcula o erro padrão da diferença entre as duas proporções.
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n_A + 1/n_B))
    # Calcula o valor Z (Z-score) — ou seja, quantos desvios padrão a diferença entre as taxas de conversão está afastada do zero (que seria esperado se não houvesse diferença real).
    z = (p_B - p_A) / se
    # Calcula o p-valor baseado no Z-score.
    #stats.norm.cdf() é a função de distribuição acumulada da normal padrão — ela nos dá a probabilidade de obter um valor menor ou igual ao Z.
    #Como queremos o valor nas caudas, usamos 1 - cdf(...).
    #E usamos abs(z) porque é um teste bicaudal (duas direções: B melhor ou A melhor).

    p_value = 1 - stats.norm.cdf(abs(z))

    print(f"Grupo A - Conversão: {p_A:.2%} ({conv_A}/{n_A})")
    print(f"Grupo B - Conversão: {p_B:.2%} ({conv_B}/{n_B})")
    print(f"Z = {z:.4f}, P = {p_value*2:.4f}")

    if p_value * 2 < alpha:
        return "✅ Diferença significativa entre os grupos!"
    else:
        return "❌ Sem diferença estatística significativa."


# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_users = 10000
conv_rate_A = 0.20
conv_rate_B = 0.25

# Group A
group_A = pd.DataFrame({
    "user_id": range(1, n_users + 1),
    "group": "A",
    "shown": 1,
    "clicked": np.random.binomial(1, conv_rate_A, n_users)
})

# Group B
group_B = pd.DataFrame({
    "user_id": range(n_users + 1, 2 * n_users + 1),
    "group": "B",
    "shown": 1,
    "clicked": np.random.binomial(1, conv_rate_B, n_users)
})

# Combine both groups
df = pd.concat([group_A, group_B], ignore_index=True)

# Shuffle rows
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
df.to_csv("campaign_data.csv", index=False)

# 1. Ler os dados
df = pd.read_csv("campaign_data.csv")

# 2. Separar grupos
group_A = df[df["group"] == "A"]
group_B = df[df["group"] == "B"]

# 3. Contar amostras e conversões
n_A = len(group_A)
conv_A = group_A["clicked"].sum()

n_B = len(group_B)
conv_B = group_B["clicked"].sum()

# 4. Rodar o teste
resultado = ab_test(n_A, conv_A, n_B, conv_B)
print(resultado)

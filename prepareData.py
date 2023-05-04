import re
import pandas as pd

# leitura do arquivo de registro de pesca
with open("24042023.txt", "r", encoding='latin-1') as f:
    lines = f.readlines()

# expressão regular para identificar eventos relevantes
pattern = r"^(\d{2}:\d{2}:\d{2}): (Started fishing|\.{3}|Shiny (Tentacool|Krabby) defeated!)$"

# lista para armazenar os dados
data = []

# percorre as linhas do arquivo e extrai os dados relevantes
for line in lines:
    match = re.match(pattern, line)
    if match:
        time = match.group(1)
        rare = 1 if "Shiny" in match.group(2) else 0
        data.append((time, rare))

# cria um DataFrame com os dados
df = pd.DataFrame(data, columns=["Hora", "Peixe Raro"])
#print(df)

import matplotlib.pyplot as plt

# converte a coluna "Hora" para um objeto datetime
df["Hora"] = pd.to_datetime(df["Hora"], format="%H:%M:%S")

# agrupa os dados por hora e calcula a média da coluna "Peixe Raro"
hourly_means = df.groupby(df["Hora"].dt.hour)["Peixe Raro"].mean()

# plota um histograma da distribuição das médias por hora
plt.bar(hourly_means.index, hourly_means)
plt.xlabel("Hora")
plt.ylabel("Frequência média de peixes raros")
plt.show()

from scipy import stats

# separa os dados em duas amostras: 20h-22h e outras horas
sample1 = df.loc[(df["Hora"].dt.hour >= 20) & (df["Hora"].dt.hour < 22), "Peixe Raro"]
sample2 = df.loc[(df["Hora"].dt.hour < 20) | (df["Hora"].dt.hour >= 22), "Peixe Raro"]

# realiza o teste t de Student para duas amostras independentes
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

#Se o valor p for menor do que um nível de significância (por exemplo, 0,05), 
#Podemos rejeitar a hipótese nula (não há diferença estatisticamente significativa entre as duas amostras).



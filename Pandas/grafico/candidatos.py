
import matplotlib.pyplot as plt
import pandas as pd
 
vereadores = pd.read_csv('Pandas/grafico/candidatos.csv')
nome = vereadores["Candidato"]
voto = vereadores["Votos"]

bars = plt.bar(nome, voto, color="skyblue")
plt.xticks(rotation=45, ha='right')  # Rotacionar rótulos em 45 graus
plt.tight_layout()  # Ajustar layout para evitar sobreposição
plt.show()

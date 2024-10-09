import matplotlib.pyplot as plt
import pandas as pd


#------------------------------------------------------------------------------------------------------------------------------------------
titanic = pd.read_csv('Novo Desktop/tested.csv')
counts = titanic['Survived'].value_counts()
explode = (0.1, 0)  
labels = ['Sobreviveu', 'Não Sobreviveu']
plt.pie(counts, explode=explode, labels=labels, autopct='%.2f%%', startangle=90,shadow=True)
plt.title("Sobrevivência no Titanic")
plt.axis('equal') 
plt.grid(True)
plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]#Lista de idade 
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']#passando a lista do bins "de iddade" para a label 
titanic['AgeGroup'] = pd.cut(titanic['Age'], bins=bins, labels=labels, right=False)#criando o "agegroup" que vai ser igual a o titanic age 
age_counts = titanic['AgeGroup'].value_counts().sort_index()#
plt.bar(age_counts.index, age_counts.values, color='skyblue')#cria o grafico por assim dizer,seria o esqueleto 
plt.xlabel('Faixa Etária')#é o bglh do eixo X 
plt.ylabel('Número de Passageiros')#o mesmo só que do Y
plt.title('Distribuição da Idade dos Passageiros do Titanic')# esse ta facil
plt.xticks(rotation=45)#para facilitar a leitura 
plt.show()#Permite a visu do grafico
#------------------------------------------------------------------------------------------------------------------------------------------




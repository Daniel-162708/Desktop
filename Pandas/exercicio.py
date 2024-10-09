import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")#Para ler csv
#•Quantas crianças abaixo de 10 anos sobreviveram?
#Quantas mulheres sobreviveram?
#•Quantos Homens sobreviveram?
#•Quantos idosos acima de 50 anos sobreviveram?
#•Quantas crianças abaixo de 12 anos do sexo feminino sobreviveram?
#print(df.columns)
print(df.loc[0])
print(df.query('Age < 10 & Survived==1')['Survived'].count())
print(df.query('Sex == "female" & Survived==1')['Survived'].count())
print(df.query('Sex == "male"')['Survived'].count())
print(df.query('Age < 50 & Survived==1')['Survived'].count())
print(df.query('Age < 12 & Survived==1 & Sex=="female"')['Survived'].count())

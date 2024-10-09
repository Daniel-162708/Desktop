import pandas as pd
 

#print(pd.__version__)Verção do "Pandas"
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")#Para ler csv
#print(df.head())
#print(df.loc[1:10, ['Name','Sex','Age']])1 a 10
print(df.loc[1:, ['Name','Sex','Age']])#1 ao max






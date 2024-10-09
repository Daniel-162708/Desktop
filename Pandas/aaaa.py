import pandas as pd
import matplotlib as plt
df=pd.read_csv("C:/Users/DanielSilva/Documents/desktop/Desktop/Pandas/all_seasons.csv")
df1 = df.loc[0:11145, ["player_height"]]
df2 = df.loc[0:11145, ["player_weght"]]
import pandas as pd

df = pd.read_csv ("nba.csv")

#groupby
#groupby using team

gk = df.groupby("Team")
print (gk.first())

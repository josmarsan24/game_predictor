import pandas as pd

#read csv
df = pd.read_csv("game_predictor/nba_data.csv", header = 0)
not_abs_cols = ['team_id',"Row.names","FG%","3P%","opFG%","op3P%"]

for col in df.columns:
    if col not in not_abs_cols:
        max = df.loc[df[col].idxmax()][col]
        min = df.loc[df[col].idxmin()][col]
        df[[col]] = df[[col]].apply(lambda n: (n - min) / (max - min))

#pd df to csv
df.to_csv('nba_data_norm.csv', index=False, header=True)

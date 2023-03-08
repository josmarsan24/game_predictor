import pandas as pd

#read csv
try:
    df = pd.read_csv("nba_data_norm.csv", header = 0)
except:
    df = pd.read_csv("game_predictor/nba_data_norm.csv", header = 0)

not_abs_cols = ['team_id',"Row.names","FG%","3P%","opFG%","op3P%"]
good_cols = ["TRB","AST","STL","BLK","PTS","opTOV","opPF"]
bad_cols = ["opTRB","opAST","opSTL","opBLK","opPTS","TOV","PF"]

def drop_asterisc(s):
    return s.split('*')[0]

if len(df.columns) == len(not_abs_cols) + len(good_cols) + len(bad_cols):
    df['Row.names'] = df['Row.names'].apply(lambda t: drop_asterisc(t))
    for col in df.columns:
        if col in good_cols:
            max = df.loc[df[col].idxmax()][col]
            min = df.loc[df[col].idxmin()][col]
            df[[col]] = df[[col]].apply(lambda n: (n - min) / (max - min))
        elif col in bad_cols:
            max = df.loc[df[col].idxmax()][col]
            min = df.loc[df[col].idxmin()][col]
            df[[col]] = df[[col]].apply(lambda n: 1 - ((n - min) / (max - min)))
        elif col == "opFG%" or  col == "op3P%":
            df[[col]] = df[[col]].apply(lambda n: 1 - n)
    
else:
    print("error")



#pd df to csv
df.to_csv('nba_data_norm.csv', index=False, header=True)

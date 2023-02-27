import pandas as pd

#read csv
teams = pd.read_csv("game_predictor/nba_data_norm.csv", header = 0)
games = pd.read_csv("game_predictor/nba_games.csv", header = 0)

def get_teams_by_name(home_name, away_name):
    home_team = teams.loc[teams['Row.names'] == home_name]
    away_team = teams.loc[teams['Row.names'] == away_name]
    return home_team, away_team

new_df = pd.DataFrame(columns = ['away_PTS', 'away_op_PTS', 'away_AST', 'away_TRB', 'away_TOV', 'away_PF', 'home_PTS', 'home_op_PTS', 'home_AST', 'home_TRB', 'home_TOV', 'home_PF', 'Date', 'away', 'away_PTS', 'home', 'home_PTS'])

for index, row in games.iterrows():
    home, away = get_teams_by_name(games['Home/Neutral'].values[index],games['Visitor/Neutral'].values[index])
    #new row
    #'Date', 'away', 'away_PTS', 'home', 'home_PTS'
    #away_PTS,away_op_PTS,away_AST,away_TRB,away_TOV,away_PF,home_PTS,home_op_PTS,home_AST,home_TRB,home_TOV,home_PF,Date,away,away_PTS,home,home_PTS
    new_df.loc[len(new_df.index)] = [away['PTS'].values[0],away['opPTS'].values[0],away['AST'].values[0],away['TRB'].values[0],away['TOV'].values[0],away['PF'].values[0],
    home['PTS'].values[0],home['opPTS'].values[0],home['AST'].values[0],home['TRB'].values[0],home['TOV'].values[0],home['PF'].values[0],
    games['Date'].values[index],games['Visitor/Neutral'].values[index],games['away_PTS'].values[index],games['Home/Neutral'].values[index],games['home_PTS'].values[index]]

#pd df to csv
new_df.to_csv('game_predictor/nba_games_full_data.csv', index=False, header=True)

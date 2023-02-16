import pandas as pd
import numpy as np
import random

#read csv
data = pd.read_csv("nba_data_norm.csv", header = 0)
#data = pd.read_csv("nba_data.csv", header = 0)
data.set_index("team_id")
games = pd.read_csv("nba_games.csv", header=0)

def get_teams_by_id(home_id, away_id):
    home_team = data.loc[data['team_id'] == home_id]
    away_team = data.loc[data['team_id'] == away_id]
    return home_team, away_team

def predict(home, away):
    home_rtg = home['PTS'].values[0]*0.175 + home['PF'].values[0]*0.025 + home['TOV'].values[0]*0.05 + home['BLK'].values[0]*0.025 + home['STL'].values[0]*0.025 + home['AST'].values[0]*0.075 + home['TRB'].values[0]*0.075 + home['FG%'].values[0]*0.025 + home['3P%'].values[0]*0.025 + home['opPTS'].values[0]*0.175 + home['opPF'].values[0]*0.025 + home['opTOV'].values[0]*0.05 + home['opBLK'].values[0]*0.025 + home['opSTL'].values[0]*0.025 + home['opAST'].values[0]*0.075 + home['opTRB'].values[0]*0.075 + home['opFG%'].values[0]*0.025 + home['op3P%'].values[0]*0.025
    away_rtg = away['PTS'].values[0]*0.175 + away['PF'].values[0]*0.025 + away['TOV'].values[0]*0.05 + away['BLK'].values[0]*0.025 + away['STL'].values[0]*0.025 + away['AST'].values[0]*0.075 + away['TRB'].values[0]*0.075 + away['FG%'].values[0]*0.025 + away['3P%'].values[0]*0.025 + away['opPTS'].values[0]*0.175 + away['opPF'].values[0]*0.025 + away['opTOV'].values[0]*0.05 + away['opBLK'].values[0]*0.025 + away['opSTL'].values[0]*0.025 + away['opAST'].values[0]*0.075 + away['opTRB'].values[0]*0.075 + away['opFG%'].values[0]*0.025 + away['op3P%'].values[0]*0.025
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def rtg_team(team):
    rtg = team['PTS'].values[0]*0.333 + team['opPTS'].values[0]*0.333 + team['AST'].values[0]*0.167 + team['TRB'].values[0]*0.167
    return rtg
    

def main(home_id, away_id):
    home, away = get_teams_by_id(home_id, away_id)
    home_name = home['Row.names'].values[0]
    away_name = away['Row.names'].values[0]
    home_odds, away_odds = predict(home,away)
    print (away_name + " at " + home_name)
    print (away_name + " odds: " + str(away_odds))
    print (home_name + " odds: " + str(home_odds))

main(2,5)
main(10,15)
main(24,18)
main(28,2)

def test():
    test_games = games.sample(n=50)
    print(test_games.head())

test()
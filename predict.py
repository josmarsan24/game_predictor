import pandas as pd
import numpy as np

#read csv
try:
    data = pd.read_csv("nba_data_norm.csv", header = 0)
except:
    data = pd.read_csv("game_predictor/nba_data_norm.csv", header = 0)
data.set_index("team_id")


def get_teams_by_id(home_id, away_id):
    home_team = data.loc[data['team_id'] == home_id]
    away_team = data.loc[data['team_id'] == away_id]
    return home_team, away_team

def get_teams_by_name(home_name, away_name):
    home_team = data.loc[data['Row.names'] == home_name]
    away_team = data.loc[data['Row.names'] == away_name]
    return home_team, away_team

def predict(home, away):
    home_rtg = home['PTS'].values[0]*0.175 + home['PF'].values[0]*0.025 + home['TOV'].values[0]*0.05 + home['BLK'].values[0]*0.025 + home['STL'].values[0]*0.025 + home['AST'].values[0]*0.075 + home['TRB'].values[0]*0.075 + home['FG%'].values[0]*0.025 + home['3P%'].values[0]*0.025 + home['opPTS'].values[0]*0.175 + home['opPF'].values[0]*0.025 + home['opTOV'].values[0]*0.05 + home['opBLK'].values[0]*0.025 + home['opSTL'].values[0]*0.025 + home['opAST'].values[0]*0.075 + home['opTRB'].values[0]*0.075 + home['opFG%'].values[0]*0.025 + home['op3P%'].values[0]*0.025
    away_rtg = away['PTS'].values[0]*0.175 + away['PF'].values[0]*0.025 + away['TOV'].values[0]*0.05 + away['BLK'].values[0]*0.025 + away['STL'].values[0]*0.025 + away['AST'].values[0]*0.075 + away['TRB'].values[0]*0.075 + away['FG%'].values[0]*0.025 + away['3P%'].values[0]*0.025 + away['opPTS'].values[0]*0.175 + away['opPF'].values[0]*0.025 + away['opTOV'].values[0]*0.05 + away['opBLK'].values[0]*0.025 + away['opSTL'].values[0]*0.025 + away['opAST'].values[0]*0.075 + away['opTRB'].values[0]*0.075 + away['opFG%'].values[0]*0.025 + away['op3P%'].values[0]*0.025
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def predict_with_home_adv(home, away):
    home_rtg = home['PTS'].values[0]*0.175 + home['PF'].values[0]*0.025 + home['TOV'].values[0]*0.05 + home['BLK'].values[0]*0.025 + home['STL'].values[0]*0.025 + home['AST'].values[0]*0.075 + home['TRB'].values[0]*0.075 + home['FG%'].values[0]*0.025 + home['3P%'].values[0]*0.025 + home['opPTS'].values[0]*0.175 + home['opPF'].values[0]*0.025 + home['opTOV'].values[0]*0.05 + home['opBLK'].values[0]*0.025 + home['opSTL'].values[0]*0.025 + home['opAST'].values[0]*0.075 + home['opTRB'].values[0]*0.075 + home['opFG%'].values[0]*0.025 + home['op3P%'].values[0]*0.025
    away_rtg = away['PTS'].values[0]*0.175 + away['PF'].values[0]*0.025 + away['TOV'].values[0]*0.05 + away['BLK'].values[0]*0.025 + away['STL'].values[0]*0.025 + away['AST'].values[0]*0.075 + away['TRB'].values[0]*0.075 + away['FG%'].values[0]*0.025 + away['3P%'].values[0]*0.025 + away['opPTS'].values[0]*0.175 + away['opPF'].values[0]*0.025 + away['opTOV'].values[0]*0.05 + away['opBLK'].values[0]*0.025 + away['opSTL'].values[0]*0.025 + away['opAST'].values[0]*0.075 + away['opTRB'].values[0]*0.075 + away['opFG%'].values[0]*0.025 + away['op3P%'].values[0]*0.025
    home_odds = 110 * home_rtg / (home_rtg + away_rtg)
    away_odds = 90 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def rtg_team(team):
    rtg = team['PTS'].values[0]*0.175 + team['PF'].values[0]*0.025 + team['TOV'].values[0]*0.05 + team['BLK'].values[0]*0.025 + team['STL'].values[0]*0.025 + team['AST'].values[0]*0.075 + team['TRB'].values[0]*0.075 + team['FG%'].values[0]*0.025 + team['3P%'].values[0]*0.025 + team['opPTS'].values[0]*0.175 + team['opPF'].values[0]*0.025 + team['opTOV'].values[0]*0.05 + team['opBLK'].values[0]*0.025 + team['opSTL'].values[0]*0.025 + team['opAST'].values[0]*0.075 + team['opTRB'].values[0]*0.075 + team['opFG%'].values[0]*0.025 + team['op3P%'].values[0]*0.025
    return rtg

def predict_by_name(home_name, away_name, v):
    home, away = get_teams_by_name(home_name,away_name)
    if str(v) == '1.0':
        home_odds, away_odds = predict(home,away)
    elif str(v) == '1.1':
        home_odds, away_odds = predict_with_home_adv(home,away)
    else:
        home_odds, away_odds = 0.0
    return home_odds, away_odds


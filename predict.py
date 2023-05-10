import pandas as pd
import numpy as np

#read csv
try:
    data = pd.read_csv("nba_data_norm.csv", header = 0)
except:
    data = pd.read_csv("game_predictor/nba_data_norm.csv", header = 0)
data.set_index("team_id")

try:
    data2023 = pd.read_csv("2022_2023_season/nba_data_norm.csv", header = 0)
except:
    data2023 = pd.read_csv("game_predictor/2022_2023_season/nba_data_norm.csv", header = 0)
data2023.set_index("team_id")


def get_teams_by_id(home_id, away_id,season='2022'):
    if season == '2022':
        home_team = data.loc[data['team_id'] == home_id]
        away_team = data.loc[data['team_id'] == away_id]
        return home_team, away_team
    elif season == '2023':
        home_team = data2023.loc[data['team_id'] == home_id]
        away_team = data2023.loc[data['team_id'] == away_id]
        return home_team, away_team
    else:
        print('NO DATA FOR THE SEASON')
        return 0,0

def get_teams_by_name(home_name, away_name,season='2022'):
    if season == '2022':
        home_team = data.loc[data['Row.names'] == home_name]
        away_team = data.loc[data['Row.names'] == away_name]
        return home_team, away_team
    elif season == '2023':
        home_team = data2023.loc[data['Row.names'] == home_name]
        away_team = data2023.loc[data['Row.names'] == away_name]
        return home_team, away_team
    else:
        print('NO DATA FOR THE SEASON')
        return 0,0

def get_home_away_WL(home_id,away_id,season='2022'):
    if season == '2022':
        try:
            wr = pd.read_csv("win_rate.csv", header = 0)
        except:
            wr = pd.read_csv("game_predictor/win_rate.csv", header = 0)
    elif season == '2023':
        try:
            wr = pd.read_csv("2022_2023_season/win_rate.csv", header = 0)
        except:
            wr = pd.read_csv("game_predictor/2022_2023_season/win_rate.csv", header = 0)
    else:
        print('NO DATA FOR THE SEASON')
        wr = 0 
    home_WL = wr.loc[wr['team_id']==home_id]['home_W/L'].values[0]
    away_WL = wr.loc[wr['team_id']==away_id]['away_W/L'].values[0]
    return home_WL,away_WL

def get_h2h(home_name,away_name,season='2022'):
    if season == '2022':
        try:
            h2h = pd.read_csv("h2h.csv", header = 0)
        except:
            h2h = pd.read_csv("game_predictor/h2h.csv", header = 0)
    elif season == '2023':
        try:
            h2h = pd.read_csv("2022_2023_season/h2h.csv", header = 0)
        except:
            h2h = pd.read_csv("game_predictor/2022_2023_season/h2h.csv", header = 0)
    else:
        print('NO DATA FOR THE SEASON')
        h2h = 0
    
    try:
        home_rec = h2h.loc[h2h['home_team']==home_name][away_name].values[0]
        away_rec = h2h.loc[h2h['home_team']==away_name][home_name].values[0]
    
        home_wr = float(home_rec.split('-')[0]) / (float(home_rec.split('-')[0]) + float(home_rec.split('-')[1]))
        away_wr = float(away_rec.split('-')[1]) / (float(away_rec.split('-')[0]) + float(away_rec.split('-')[1]))

        home_adv = 1 - 0.5 + (home_wr*2+away_wr)/3
        away_adv = 1 + 0.5 - (home_wr*2+away_wr)/3

        return home_adv, away_adv
    except:

        return 1,1

def get_h2h_custom(home_name,away_name,h2h):
    try:
        home_rec = h2h.loc[h2h['home_team']==home_name][away_name].values[0]
        away_rec = h2h.loc[h2h['home_team']==away_name][home_name].values[0]

        home_wr = float(home_rec.split('-')[0]) / (float(home_rec.split('-')[0]) + float(home_rec.split('-')[1]))
        away_wr = float(away_rec.split('-')[1]) / (float(away_rec.split('-')[0]) + float(away_rec.split('-')[1]))
        n = (float(home_rec.split('-')[0])) + float(home_rec.split('-')[1]) + (float(away_rec.split('-')[0]) + float(away_rec.split('-')[1]))
        
        home_adv = 1 - 0.5 + (home_wr*2+away_wr)/3
        away_adv = 1 + 0.5 - (home_wr*2+away_wr)/3

        return home_adv, away_adv
    except:

        return 1,1

def predict(home_rtg, away_rtg):
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def rtg_team(team):
    rtg = team['PTS'].values[0]*0.175 + team['PF'].values[0]*0.025 + team['TOV'].values[0]*0.05 + team['BLK'].values[0]*0.025 + team['STL'].values[0]*0.025 + team['AST'].values[0]*0.075 + team['TRB'].values[0]*0.075 + team['FG%'].values[0]*0.025 + team['3P%'].values[0]*0.025 + team['opPTS'].values[0]*0.175 + team['opPF'].values[0]*0.025 + team['opTOV'].values[0]*0.05 + team['opBLK'].values[0]*0.025 + team['opSTL'].values[0]*0.025 + team['opAST'].values[0]*0.075 + team['opTRB'].values[0]*0.075 + team['opFG%'].values[0]*0.025 + team['op3P%'].values[0]*0.025
    return rtg

def new_rtg_team(team):
    rtg = team['PTS'].values[0]*0.15 + team['PF'].values[0]*0.025 + team['TOV'].values[0]*0.075 + team['BLK'].values[0]*0.025 + team['STL'].values[0]*0.025 + team['AST'].values[0]*0.05 + team['TRB'].values[0]*0.05 + team['FG%'].values[0]*0.05 + team['3P%'].values[0]*0.05 + team['opPTS'].values[0]*0.15 + team['opPF'].values[0]*0.025 + team['opTOV'].values[0]*0.075 + team['opBLK'].values[0]*0.025 + team['opSTL'].values[0]*0.025 + team['opAST'].values[0]*0.05 + team['opTRB'].values[0]*0.05 + team['opFG%'].values[0]*0.05 + team['op3P%'].values[0]*0.05
    return rtg

def rtg_no_fg_no3p(team):
    rtg = team['PTS'].values[0]*0.175 + team['PF'].values[0]*0.025 + team['TOV'].values[0]*0.05 + team['BLK'].values[0]*0.025 + team['STL'].values[0]*0.025 + team['AST'].values[0]*0.075 + team['TRB'].values[0]*0.075 + team['opPTS'].values[0]*0.175 + team['opPF'].values[0]*0.025 + team['opTOV'].values[0]*0.05 + team['opBLK'].values[0]*0.025 + team['opSTL'].values[0]*0.025 + team['opAST'].values[0]*0.075 + team['opTRB'].values[0]*0.075
    return rtg

def get_rating_by_type(team,rtg):
    if rtg == '1.0':
        rating = rtg_team(team)
    elif rtg == '1.1':
        rating = new_rtg_team(team)
    elif rtg == 'no FG% or 3P%':
        rating = rtg_no_fg_no3p(team)
    else:
        rating = -1
    return rating

def predict_with_home_adv(home_rtg, away_rtg):
    home_rtg = 1.1 * home_rtg
    away_rtg = 0.9 * away_rtg
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def predict_with_custom_home_adv(home_rtg, away_rtg,home_adv):
    home_rtg = home_adv * home_rtg
    away_rtg = (2 - home_adv) * away_rtg
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def predict_with_advanced_home_adv(home, away, rtg ,season):
    home_rtg = get_rating_by_type(home,rtg)
    away_rtg = get_rating_by_type(away,rtg)
    
    home_WL, away_WL = get_home_away_WL(home['team_id'].values[0],away['team_id'].values[0],season)
    home_rtg = home_rtg * (1 + home_WL - away_WL)
    away_rtg = away_rtg * (1 + away_WL - home_WL)
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def predict_with_h2h(home, away, rtg, season):
    home_rtg = get_rating_by_type(home,rtg)
    away_rtg = get_rating_by_type(away,rtg)
    
    home_adv, away_adv = get_h2h(home['Row.names'].values[0],away['Row.names'].values[0],season)
    home_rtg = home_adv * home_rtg
    away_rtg = away_adv * away_rtg
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds

def predict_with_h2h_custom_data(home, away, rtg, df):
    home_rtg = get_rating_by_type(home,rtg)
    away_rtg = get_rating_by_type(away,rtg)
    
    home_adv, away_adv = get_h2h_custom(home['Row.names'].values[0],away['Row.names'].values[0],df)
    home_rtg = home_adv * home_rtg
    away_rtg = away_adv * away_rtg
    home_odds = 100 * home_rtg / (home_rtg + away_rtg)
    away_odds = 100 * away_rtg / (home_rtg + away_rtg)
    return home_odds, away_odds


def predict_by_name(home_name, away_name, v, rtg, season='2022'):
    home, away = get_teams_by_name(home_name,away_name,season)
    home_rtg = get_rating_by_type(home,rtg)
    away_rtg = get_rating_by_type(away,rtg)
    
    if str(v) == 'default':
        home_odds, away_odds = predict(home_rtg,away_rtg)
    elif str(v) == 'home advantage':
        home_odds, away_odds = predict_with_home_adv(home_rtg,away_rtg)
    elif str(v) == 'advanced home advantage':
        home_odds, away_odds = predict_with_advanced_home_adv(home,away,rtg,season)
    elif str(v) == 'h2h':
        home_odds, away_odds = predict_with_h2h(home,away,rtg,season)
    else:
        return 50.0,50.0
    
    return home_odds, away_odds

def get_message(home_team,away_team,home_odds,away_odds):
    if home_odds == away_odds:
        return 'The odds for each team are the same, the game is as close as it could be'
    elif home_odds - away_odds > 10:
        return 'The winner should be ' + home_team + ' by a wide margain'
    elif home_odds - away_odds <=10 and home_odds - away_odds > 5:
        return 'The winner should be ' + home_team + ' by a decent margain'
    elif home_odds - away_odds <= 5 and home_odds - away_odds > 0:
        return 'The winner should be' + home_team + ' by a small margain'
    elif away_odds - home_odds > 10:
        return 'The winner should be ' + away_team + ' by a wide margain'
    elif away_odds - home_odds <=10 and away_odds - home_odds > 5:
        return 'The winner should be ' + away_team + ' by a decent margain'
    elif away_odds - home_odds <= 5 and away_odds - home_odds > 0:
        return 'The winner should be ' + away_team + ' by a small margain'
    else:
        return 'Error processing the data'
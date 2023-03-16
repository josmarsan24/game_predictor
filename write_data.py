import pandas as pd
import numpy as np
from predict import get_teams_by_name

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

try:
    wr = pd.read_csv("win_rate.csv", header=0)
    wr.set_index("team_id")
except:
    wr = pd.read_csv("game_predictor/win_rate.csv", header=0)
    wr.set_index("team_id")

def home_adv():
    df = wr
    df['home_W/L'] = 0
    df['away_W/L'] = 0
    for index, row in games.iterrows():
         if (row['away_PTS'] < row['home_PTS']):
            home_name = games['Home/Neutral'].values[index]
            df.loc[df['Row.names'] == home_name,'home_W/L'] = df.loc[df['Row.names'] == home_name,'home_W/L'] + 1
    df['home_W/L'] = (df['home_W/L'])/(df['W/L']*82)
    df['away_W/L'] = 1 - df['home_W/L']
    df.to_csv('win_rate.csv', index=False, header=True)

def h2h():
    df = pd.DataFrame(columns = ['team_id','home_team','Atlanta Hawks',
        'Boston Celtics',
        'Brooklyn Nets',
        'Charlotte Hornets',
        'Chicago Bulls',
        'Cleveland Cavaliers',
        'Dallas Mavericks',
        'Denver Nuggets',
        'Detroit Pistons',
        'Golden State Warriors',
        'Houston Rockets',
        'Indiana Pacers',
        'Los Angeles Clippers',
        'Los Angeles Lakers',
        'Memphis Grizzlies',
        'Miami Heat',
        'Milwaukee Bucks',
        'Minnesota Timberwolves',
        'New Orleans Pelicans',
        'New York Knicks',
        'Oklahoma City Thunder',
        'Orlando Magic',
        'Philadelphia 76ers',
        'Phoenix Suns',
        'Portland Trail Blazers',
        'Sacramento Kings',
        'San Antonio Spurs',
        'Toronto Raptors',
        'Utah Jazz',
        'Washington Wizards'])
    df['home_team'] = wr['Row.names']
    df['team_id'] = wr['team_id']
    df = df.replace(np.nan, '0-0')

    
    for index, row in games.iterrows():
        home_name = games['Home/Neutral'].values[index]
        away_name = games['Visitor/Neutral'].values[index]
        if (row['away_PTS'] < row['home_PTS']):
            df.loc[df['home_team'] == home_name,away_name] = add_vict(df.loc[df['home_team'] == home_name,away_name].values[0],True)
        else:
            df.loc[df['home_team'] == home_name,away_name] = add_vict(df.loc[df['home_team'] == home_name,away_name].values[0],False)
    df.to_csv('h2h.csv', index=False, header=True)

def add_vict(record, home):
    try:
        if home==True:
            record = str(int(record.split('-')[0]) + 1) + '-' + record.split('-')[1]
        else:
            record = record.split('-')[0] + '-' + str(int(record.split('-')[1]) + 1)
        return record
    except:
        return '0-0'


#h2h()
#home_adv()
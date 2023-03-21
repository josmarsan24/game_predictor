from predict import *
import pandas as pd
from write_data import add_vict

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

def test_adv_home_adv(test_games,rtg):
    right = 0
    wrong = 0
    small_mistake = 0
    big_mistake = 0
    for index, row in test_games.iterrows():
        home_name = row['Home/Neutral']
        away_name = row['Visitor/Neutral']
        if (row['away_PTS'] > row['home_PTS']):
            winner = away_name
        else:
            winner = home_name
        home, away = get_teams_by_name(home_name,away_name)
        home_rtg = get_rating_by_type(home,rtg)
        away_rtg = get_rating_by_type(away,rtg)
        home_odds, away_odds = predict_with_advanced_home_adv(home_rtg,away_rtg)
        if (away_odds > home_odds and winner==away_name) or (away_odds < home_odds and winner==home_name):
            right += 1
        elif (away_odds - home_odds > 20 and winner==home_name) or (home_odds - away_odds > 20 and winner==away_name):
            wrong += 1
            big_mistake += 1
        elif (away_odds - home_odds < 10 and winner==home_name) or (home_odds - away_odds < 10 and winner==away_name):
            wrong += 1
            small_mistake += 1
        else:
            wrong += 1
    return right, wrong, big_mistake, small_mistake

def test_home_adv(test_games,home_adv, rtg):
    right = 0
    wrong = 0
    small_mistake = 0
    big_mistake = 0
    for index, row in test_games.iterrows():
        home_name = row['Home/Neutral']
        away_name = row['Visitor/Neutral']
        if (row['away_PTS'] > row['home_PTS']):
            winner = away_name
        else:
            winner = home_name
        home, away = get_teams_by_name(home_name,away_name)
        home_rtg = get_rating_by_type(home,rtg)
        away_rtg = get_rating_by_type(away,rtg)
        home_odds, away_odds = predict_with_custom_home_adv(home_rtg,away_rtg,home_adv)
        if (away_odds > home_odds and winner==away_name) or (away_odds < home_odds and winner==home_name):
            right += 1
        elif (away_odds - home_odds > 20 and winner==home_name) or (home_odds - away_odds > 20 and winner==away_name):
            wrong += 1
            big_mistake += 1
        elif (away_odds - home_odds < 10 and winner==home_name) or (home_odds - away_odds < 10 and winner==away_name):
            wrong += 1
            small_mistake += 1
        else:
            wrong += 1
    return right, wrong, big_mistake, small_mistake

def test_predict_by_name(test_games,v,rtg):
    right = 0
    wrong = 0
    small_mistake = 0
    big_mistake = 0
    for index, row in test_games.iterrows():
        home_name = row['Home/Neutral']
        away_name = row['Visitor/Neutral']
        if (row['away_PTS'] > row['home_PTS']):
            winner = away_name
        else:
            winner = home_name
        home_odds, away_odds = predict_by_name(home_name,away_name,v,rtg)
        if (away_odds > home_odds and winner==away_name) or (away_odds < home_odds and winner==home_name):
            right += 1
        elif (away_odds - home_odds > 20 and winner==home_name) or (home_odds - away_odds > 20 and winner==away_name):
            wrong += 1
            big_mistake += 1
        elif (away_odds - home_odds < 10 and winner==home_name) or (home_odds - away_odds < 10 and winner==away_name):
            wrong += 1
            small_mistake += 1
        else:
            wrong += 1
    return right, wrong, big_mistake, small_mistake

def create_test_h2h(train_games):
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

    
    for row in train_games.iterrows():
        home_name = row[1]['Home/Neutral']
        away_name = row[1]['Visitor/Neutral']
        if (row[1]['away_PTS'] < row[1]['home_PTS']):
            df.loc[df['home_team'] == home_name,away_name] = add_vict(df.loc[df['home_team'] == home_name,away_name].values[0],True)
        else:
            df.loc[df['home_team'] == home_name,away_name] = add_vict(df.loc[df['home_team'] == home_name,away_name].values[0],False)
    return df

def test_h2h(df, rtg, test_games):
    right = 0
    wrong = 0
    small_mistake = 0
    big_mistake = 0
    for index, row in test_games.iterrows():
        home_name = row['Home/Neutral']
        away_name = row['Visitor/Neutral']
        home, away = get_teams_by_name(home_name,away_name)
        if (row['away_PTS'] > row['home_PTS']):
            winner = away_name
        else:
            winner = home_name
        home_odds, away_odds = predict_with_h2h_custom_data(home,away,rtg,df)
        if (away_odds > home_odds and winner==away_name) or (away_odds < home_odds and winner==home_name):
            right += 1
        elif (away_odds - home_odds > 20 and winner==home_name) or (home_odds - away_odds > 20 and winner==away_name):
            wrong += 1
            big_mistake += 1
        elif (away_odds - home_odds < 10 and winner==home_name) or (home_odds - away_odds < 10 and winner==away_name):
            wrong += 1
            small_mistake += 1
        else:
            wrong += 1
    return right, wrong, big_mistake, small_mistake

def print_test(desc,a,b,c,d):
    print(desc)
    print("SUCCESS RATE: ", 100*a/(a+b),"%")
    print("RIGHT PREDICTIONS: ", a)
    print("WRONG PREDICTIONS: ", b)
    print(" OF WHICH:")
    print(" MISTAKES IN ACCEPTABLE MARGAIN: ", d)
    print(" MISTAKES IN DECENT MARGAIN: ", b - (c + d))
    print(" MISTAKES IN UNACCEPTABLE MARGAIN: ", c)

train=games.sample(frac=0.67,random_state=200)
test=games.drop(train.index)

print("GAMES PREDICTED: ", len(games))

a,b,c,d = test_predict_by_name(games,'default','1.0')
print_test('USING DEFAULT FORMULA',a,b,c,d)
a,b,c,d = test_predict_by_name(games,'default','no FG% or 3P%')
print_test('IGNORING FG% AND 3P%',a,b,c,d)
a,b,c,d = test_predict_by_name(games,'default','1.1')
print_test('USING NEW RATING',a,b,c,d)

a,b,c,d = test_home_adv(games,1.1,'1.1')
print_test('USING 1.1% HOME ADVANTAGE',a,b,c,d)
a,b,c,d = test_home_adv(games,1.05,'1.1')
print_test('USING 1.05% HOME ADVANTAGE',a,b,c,d)
a,b,c,d = test_home_adv(games,1.075,'1.1')
print_test('USING 1.075% HOME ADVANTAGE',a,b,c,d)


a,b,c,d = test_predict_by_name(games,'advanced home advantage','1.1')
print_test('USING ADVANCED HOME ADVANTAGE',a,b,c,d)

print("GAMES PREDICTED: ", len(test))

train_h2h = create_test_h2h(train)
a,b,c,d = test_h2h(train_h2h, '1.0', test)
print_test('USING H2H: 67% TRAIN DATA AND 33% TEST DATA',a,b,c,d)

a,b,c,d = test_predict_by_name(test,'default','1.1')
print_test('USING DEFAULT FORMULA',a,b,c,d)

a,b,c,d = test_predict_by_name(test,'h2h','1.1')
print_test('USING H2H',a,b,c,d)
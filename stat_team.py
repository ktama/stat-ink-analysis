import pandas as pd
from utility import *


def filter(df):
    header = list(df)
    if len([s for s in header if 'W1' in s]) > 0:
        return df.drop(['mode', 'stage', 'time', 'win',
                        'W1-weapon', 'W1-kill-assist', 'W1-kill', 'W1-assist', 'W1-death', 'W1-special', 'W1-inked', 'W1-level',
                        'W2-weapon', 'W2-kill-assist', 'W2-kill', 'W2-assist', 'W2-death', 'W2-special', 'W2-inked', 'W2-level',
                        'W3-weapon', 'W3-kill-assist', 'W3-kill', 'W3-assist', 'W3-death', 'W3-special', 'W3-inked', 'W3-level',
                        'W4-weapon', 'W4-kill-assist', 'W4-kill', 'W4-assist', 'W4-death', 'W4-special', 'W4-inked', 'W4-level',
                        'L1-weapon', 'L1-kill-assist', 'L1-kill', 'L1-assist', 'L1-death', 'L1-special', 'L1-inked', 'L1-level',
                        'L2-weapon', 'L2-kill-assist', 'L2-kill', 'L2-assist', 'L2-death', 'L2-special', 'L2-inked', 'L2-level',
                        'L3-weapon', 'L3-kill-assist', 'L3-kill', 'L3-assist', 'L3-death', 'L3-special', 'L3-inked', 'L3-level',
                        'L4-weapon', 'L4-kill-assist', 'L4-kill', 'L4-assist', 'L4-death', 'L4-special', 'L4-inked', 'L4-level'], axis=1)
    else:
        return df.drop(['mode', 'stage', 'time', 'win',
                        'A1-weapon', 'A1-kill-assist', 'A1-kill', 'A1-assist', 'A1-death', 'A1-special', 'A1-inked', 'A1-level',
                        'A2-weapon', 'A2-kill-assist', 'A2-kill', 'A2-assist', 'A2-death', 'A2-special', 'A2-inked', 'A2-level',
                        'A3-weapon', 'A3-kill-assist', 'A3-kill', 'A3-assist', 'A3-death', 'A3-special', 'A3-inked', 'A3-level',
                        'A4-weapon', 'A4-kill-assist', 'A4-kill', 'A4-assist', 'A4-death', 'A4-special', 'A4-inked', 'A4-level',
                        'B1-weapon', 'B1-kill-assist', 'B1-kill', 'B1-assist', 'B1-death', 'B1-special', 'B1-inked', 'B1-level',
                        'B2-weapon', 'B2-kill-assist', 'B2-kill', 'B2-assist', 'B2-death', 'B2-special', 'B2-inked', 'B2-level',
                        'B3-weapon', 'B3-kill-assist', 'B3-kill', 'B3-assist', 'B3-death', 'B3-special', 'B3-inked', 'B3-level',
                        'B4-weapon', 'B4-kill-assist', 'B4-kill', 'B4-assist', 'B4-death', 'B4-special', 'B4-inked', 'B4-level'], axis=1)


def get_item_list():
    return ['kill', 'assist', 'death', 'special', 'inked', 'level']


def mean_stat(df):
    m = df.mean()
    print(m)
    header = list(df)
    if len([s for s in header if 'W1' in s]) > 0:
        for item in get_item_list():
            delta = m['WT-'+item] - m['LT-'+item]
            print(item + ': ' + str(delta))
    else:
        for item in get_item_list():
            delta = m['AT-'+item] - m['BT-'+item]
            print(item + ': ' + str(delta))


def median_stat(df):
    m = df.median()
    print(m)
    header = list(df)
    if len([s for s in header if 'W1' in s]) > 0:
        for item in get_item_list():
            delta = m['WT-'+item] - m['LT-'+item]
            print(item + ': ' + str(delta))
    else:
        for item in get_item_list():
            delta = m['AT-'+item] - m['AT-'+item]
            print(item + ': ' + str(delta))


def mean_team(df, kind):
    header = list(df)
    if len([s for s in header if 'W1' in s]) > 0:
        df['WT-'+kind] = (df['W1-'+kind] + df['W2-'+kind] +
                          df['W3-'+kind] + df['W4-'+kind]) / 4
        df['LT-'+kind] = (df['L1-'+kind] + df['L2-'+kind] +
                          df['L3-'+kind] + df['L4-'+kind]) / 4
    else:
        df['AT-'+kind] = (df['A1-'+kind] + df['A2-'+kind] +
                          df['A3-'+kind] + df['A4-'+kind]) / 4
        df['BT-'+kind] = (df['B1-'+kind] + df['B2-'+kind] +
                          df['B3-'+kind] + df['B4-'+kind]) / 4
    return df


def stat_team_data(df):
    team_index = ['A', 'B']
    header = list(df)
    if len([s for s in header if 'W1' in s]) > 0:
        team_index = ['W', 'L']

    # for category in ['kill']:
    for category in ['kill', 'assist', 'death', 'special', 'inked', 'level']:
        x, y = extract_team_data(df, team_index, category)
        df[team_index[0]+'T-'+category+'-mean'] = x.mean(axis=1)
        df[team_index[1]+'T-'+category+'-mean'] = y.mean(axis=1)
        df[team_index[0]+'T-'+category+'-median'] = x.median(axis=1)
        df[team_index[1]+'T-'+category+'-median'] = y.median(axis=1)
        df[team_index[0]+'T-'+category+'-max'] = x.max(axis=1)
        df[team_index[1]+'T-'+category+'-max'] = y.max(axis=1)
        df[team_index[0]+'T-'+category+'-min'] = x.min(axis=1)
        df[team_index[1]+'T-'+category+'-min'] = y.min(axis=1)
        df[team_index[0]+'T-'+category+'-std'] = x.std(axis=1)
        df[team_index[1]+'T-'+category+'-std'] = y.std(axis=1)
        df[team_index[0]+'T-'+category+'-var'] = x.var(axis=1)
        df[team_index[1]+'T-'+category+'-var'] = y.var(axis=1)
        df[team_index[0]+'T-'+category +
            '-delta'] = x.mean(axis=1) - y.mean(axis=1)
        df = df.drop([team_index[0]+'1-'+category, team_index[0]+'2-'+category,
                      team_index[0]+'3-'+category, team_index[0]+'4-'+category,
                      team_index[1]+'1-'+category, team_index[1]+'2-'+category,
                      team_index[1]+'3-'+category, team_index[1]+'4-'+category], axis=1)
    df = df.drop([team_index[0]+'1-kill-assist', team_index[0]+'2-kill-assist',
                  team_index[0]+'3-kill-assist', team_index[0]+'4-kill-assist',
                  team_index[1]+'1-kill-assist', team_index[1]+'2-kill-assist',
                  team_index[1]+'3-kill-assist', team_index[1]+'4-kill-assist'], axis=1)

    return df


def stat_table(df):
    mean = df.mean().reset_index(name='mean')
    median = df.median().reset_index(name='median')
    max = df.max().reset_index(name='max')
    min = df.min().reset_index(name='min')
    std = df.std().reset_index(name='std')
    var = df.var().reset_index(name='var')
    stat_df = pd.merge(mean, median)
    stat_df = pd.merge(stat_df, max)
    stat_df = pd.merge(stat_df, min)
    stat_df = pd.merge(stat_df, std)
    stat_df = pd.merge(stat_df, var)
    return stat_df

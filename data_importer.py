import pandas as pd
import glob

from stat_team import *
from buki import *
from plot import *


def read_battle_result():
    csv_files = glob.glob('battle-results/2021-11-05.csv')
    # csv_files = glob.glob('battle-results/2021*.csv')

    df = pd.DataFrame(columns=[])

    for csv_file in csv_files:
        tmp = pd.read_csv(csv_file)
        df = pd.concat([df, tmp])

    ver = df['game-ver'].max()

    gachi = df.query(
        '`lobby-mode` == "gachi" & lobby == "standard" & `A1-rank` == "x" & `game-ver` == @ver')
    # queryで指定した条件の列は削除
    gachi = gachi.drop(['# period', 'lobby-mode', 'lobby', 'A1-rank', 'A2-rank', 'A3-rank', 'A4-rank',
                        'B1-rank', 'B2-rank', 'B3-rank', 'B4-rank', 'game-ver'], axis=1)
    return gachi


def translate_win_lose(df):
    alpha = df.query('win == "alpha"')
    bravo = df.query('win == "bravo"')

    alpha = alpha.rename(columns={'A1-weapon': 'W1-weapon', 'A1-kill-assist': 'W1-kill-assist', 'A1-kill': 'W1-kill', 'A1-assist': 'W1-assist', 'A1-death': 'W1-death', 'A1-special': 'W1-special', 'A1-inked': 'W1-inked', 'A1-rank': 'W1-rank', 'A1-level': 'W1-level',
                                  'A2-weapon': 'W2-weapon', 'A2-kill-assist': 'W2-kill-assist', 'A2-kill': 'W2-kill', 'A2-assist': 'W2-assist', 'A2-death': 'W2-death', 'A2-special': 'W2-special', 'A2-inked': 'W2-inked', 'A2-rank': 'W2-rank', 'A2-level': 'W2-level',
                                  'A3-weapon': 'W3-weapon', 'A3-kill-assist': 'W3-kill-assist', 'A3-kill': 'W3-kill', 'A3-assist': 'W3-assist', 'A3-death': 'W3-death', 'A3-special': 'W3-special', 'A3-inked': 'W3-inked', 'A3-rank': 'W3-rank', 'A3-level': 'W3-level',
                                  'A4-weapon': 'W4-weapon', 'A4-kill-assist': 'W4-kill-assist', 'A4-kill': 'W4-kill', 'A4-assist': 'W4-assist', 'A4-death': 'W4-death', 'A4-special': 'W4-special', 'A4-inked': 'W4-inked', 'A4-rank': 'W4-rank', 'A4-level': 'W4-level',
                                  'B1-weapon': 'L1-weapon', 'B1-kill-assist': 'L1-kill-assist', 'B1-kill': 'L1-kill', 'B1-assist': 'L1-assist', 'B1-death': 'L1-death', 'B1-special': 'L1-special', 'B1-inked': 'L1-inked', 'B1-rank': 'L1-rank', 'B1-level': 'L1-level',
                                  'B2-weapon': 'L2-weapon', 'B2-kill-assist': 'L2-kill-assist', 'B2-kill': 'L2-kill', 'B2-assist': 'L2-assist', 'B2-death': 'L2-death', 'B2-special': 'L2-special', 'B2-inked': 'L2-inked', 'B2-rank': 'L2-rank', 'B2-level': 'L2-level',
                                  'B3-weapon': 'L3-weapon', 'B3-kill-assist': 'L3-kill-assist', 'B3-kill': 'L3-kill', 'B3-assist': 'L3-assist', 'B3-death': 'L3-death', 'B3-special': 'L3-special', 'B3-inked': 'L3-inked', 'B3-rank': 'L3-rank', 'B3-level': 'L3-level',
                                  'B4-weapon': 'L4-weapon', 'B4-kill-assist': 'L4-kill-assist', 'B4-kill': 'L4-kill', 'B4-assist': 'L4-assist', 'B4-death': 'L4-death', 'B4-special': 'L4-special', 'B4-inked': 'L4-inked', 'B4-rank': 'L4-rank', 'B4-level': 'L4-level'})

    bravo = bravo.rename(columns={'B1-weapon': 'W1-weapon', 'B1-kill-assist': 'W1-kill-assist', 'B1-kill': 'W1-kill', 'B1-assist': 'W1-assist', 'B1-death': 'W1-death', 'B1-special': 'W1-special', 'B1-inked': 'W1-inked', 'B1-rank': 'W1-rank', 'B1-level': 'W1-level',
                                  'B2-weapon': 'W2-weapon', 'B2-kill-assist': 'W2-kill-assist', 'B2-kill': 'W2-kill', 'B2-assist': 'W2-assist', 'B2-death': 'W2-death', 'B2-special': 'W2-special', 'B2-inked': 'W2-inked', 'B2-rank': 'W2-rank', 'B2-level': 'W2-level',
                                  'B3-weapon': 'W3-weapon', 'B3-kill-assist': 'W3-kill-assist', 'B3-kill': 'W3-kill', 'B3-assist': 'W3-assist', 'B3-death': 'W3-death', 'B3-special': 'W3-special', 'B3-inked': 'W3-inked', 'B3-rank': 'W3-rank', 'B3-level': 'W3-level',
                                  'B4-weapon': 'W4-weapon', 'B4-kill-assist': 'W4-kill-assist', 'B4-kill': 'W4-kill', 'B4-assist': 'W4-assist', 'B4-death': 'W4-death', 'B4-special': 'W4-special', 'B4-inked': 'W4-inked', 'B4-rank': 'W4-rank', 'B4-level': 'W4-level',
                                  'A1-weapon': 'L1-weapon', 'A1-kill-assist': 'L1-kill-assist', 'A1-kill': 'L1-kill', 'A1-assist': 'L1-assist', 'A1-death': 'L1-death', 'A1-special': 'L1-special', 'A1-inked': 'L1-inked', 'A1-rank': 'L1-rank', 'A1-level': 'L1-level',
                                  'A2-weapon': 'L2-weapon', 'A2-kill-assist': 'L2-kill-assist', 'A2-kill': 'L2-kill', 'A2-assist': 'L2-assist', 'A2-death': 'L2-death', 'A2-special': 'L2-special', 'A2-inked': 'L2-inked', 'A2-rank': 'L2-rank', 'A2-level': 'L2-level',
                                  'A3-weapon': 'L3-weapon', 'A3-kill-assist': 'L3-kill-assist', 'A3-kill': 'L3-kill', 'A3-assist': 'L3-assist', 'A3-death': 'L3-death', 'A3-special': 'L3-special', 'A3-inked': 'L3-inked', 'A3-rank': 'L3-rank', 'A3-level': 'L3-level',
                                  'A4-weapon': 'L4-weapon', 'A4-kill-assist': 'L4-kill-assist', 'A4-kill': 'L4-kill', 'A4-assist': 'L4-assist', 'A4-death': 'L4-death', 'A4-special': 'L4-special', 'A4-inked': 'L4-inked', 'A4-rank': 'L4-rank', 'A4-level': 'L4-level'})
    # bravo = bravo.loc[:, ['# period', 'game-ver', 'lobby-mode', 'lobby', 'mode', 'stage', 'time', 'win', 'knockout',
    bravo = bravo.loc[:, ['mode', 'stage', 'time', 'win', 'knockout',
                          'W1-weapon', 'W1-kill-assist', 'W1-kill', 'W1-assist', 'W1-death', 'W1-special', 'W1-inked', 'W1-level',
                          'W2-weapon', 'W2-kill-assist', 'W2-kill', 'W2-assist', 'W2-death', 'W2-special', 'W2-inked', 'W2-level',
                          'W3-weapon', 'W3-kill-assist', 'W3-kill', 'W3-assist', 'W3-death', 'W3-special', 'W3-inked', 'W3-level',
                          'W4-weapon', 'W4-kill-assist', 'W4-kill', 'W4-assist', 'W4-death', 'W4-special', 'W4-inked', 'W4-level',
                          'L1-weapon', 'L1-kill-assist', 'L1-kill', 'L1-assist', 'L1-death', 'L1-special', 'L1-inked', 'L1-level',
                          'L2-weapon', 'L2-kill-assist', 'L2-kill', 'L2-assist', 'L2-death', 'L2-special', 'L2-inked', 'L2-level',
                          'L3-weapon', 'L3-kill-assist', 'L3-kill', 'L3-assist', 'L3-death', 'L3-special', 'L3-inked', 'L3-level',
                          'L4-weapon', 'L4-kill-assist', 'L4-kill', 'L4-assist', 'L4-death', 'L4-special', 'L4-inked', 'L4-level']]

    gachi = pd.concat([alpha, bravo])
    return gachi


if __name__ == '__main__':
    alpha_beta_gachi = read_battle_result()
    win_lose_gachi = translate_win_lose(alpha_beta_gachi)
    print(alpha_beta_gachi)
    tmp = replace_name2no(alpha_beta_gachi)
    print(tmp)
    print(win_lose_gachi)
    alpha_beta_gachi.to_csv('alpha_beta_data.csv')
    win_lose_gachi.to_csv('win_lose_data.csv')
    alpha_beta_stat_data = filter(alpha_beta_gachi)
    win_lose_stat_data = filter(win_lose_gachi)
    alpha_beta_stat_data.to_csv('alpha_beta_filter.csv')
    win_lose_stat_data.to_csv('win_lose_filter.csv')
    alpha_beta_stat_df = stat_table(alpha_beta_stat_data)
    win_lose_stat_df = stat_table(win_lose_stat_data)
    print(alpha_beta_stat_df)
    print(win_lose_stat_df)
    print(alpha_beta_stat_df.corr())
    print(win_lose_stat_df.corr())
    plot_table(alpha_beta_stat_df, 'alpha_beta')
    plot_table(win_lose_gachi, 'win_lose')

import pandas as pd


def filter(df):
    return df.drop(['# period', 'game-ver', 'lobby-mode', 'lobby', 'mode', 'stage', 'time', 'win',
                    'W1-weapon', 'W1-kill-assist', 'W1-kill', 'W1-assist', 'W1-death', 'W1-special', 'W1-inked', 'W1-rank', 'W1-level',
                    'W2-weapon', 'W2-kill-assist', 'W2-kill', 'W2-assist', 'W2-death', 'W2-special', 'W2-inked', 'W2-rank', 'W2-level',
                    'W3-weapon', 'W3-kill-assist', 'W3-kill', 'W3-assist', 'W3-death', 'W3-special', 'W3-inked', 'W3-rank', 'W3-level',
                    'W4-weapon', 'W4-kill-assist', 'W4-kill', 'W4-assist', 'W4-death', 'W4-special', 'W4-inked', 'W4-rank', 'W4-level',
                    'L1-weapon', 'L1-kill-assist', 'L1-kill', 'L1-assist', 'L1-death', 'L1-special', 'L1-inked', 'L1-rank', 'L1-level',
                    'L2-weapon', 'L2-kill-assist', 'L2-kill', 'L2-assist', 'L2-death', 'L2-special', 'L2-inked', 'L2-rank', 'L2-level',
                    'L3-weapon', 'L3-kill-assist', 'L3-kill', 'L3-assist', 'L3-death', 'L3-special', 'L3-inked', 'L3-rank', 'L3-level',
                    'L4-weapon', 'L4-kill-assist', 'L4-kill', 'L4-assist', 'L4-death', 'L4-special', 'L4-inked', 'L4-rank', 'L4-level'], axis=1)


def get_item_list():
    return ['kill', 'assist', 'death', 'special', 'inked', 'level']


def mean_stat(df):
    m = df.mean()
    for item in get_item_list():
        pass


if __name__ == '__main__':
    mean_stat()

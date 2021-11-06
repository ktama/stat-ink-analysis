import pandas as pd


def read_battle_result():
    df = pd.read_csv('battle-results/2021-11-05.csv', header=1)
    print(df)


if __name__ == '__main__':
    read_battle_result()

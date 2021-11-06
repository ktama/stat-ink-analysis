import pandas as pd
import glob


def read_battle_result():
    csv_files = glob.glob('battle-results/2021*.csv')

    df = pd.DataFrame(columns=[])

    for csv_file in csv_files:
        tmp = pd.read_csv(csv_file)
        df = pd.concat([df, tmp])

    ver = df['game-ver'].max()

    gachi = df.query(
        '`lobby-mode` == "gachi" & lobby == "standard" & `A1-rank` == "x" & `game-ver` == @ver')
    print(gachi)


if __name__ == '__main__':
    read_battle_result()

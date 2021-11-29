import pandas as pd
import dataclasses


@dataclasses.dataclass
class Buki:
    key: str
    category1: str
    category2: str
    mainweapon: str
    subweapon: str
    special: str
    reskin: str
    # TODO:番号に直したメンバーを追加


def read_buki():
    df = pd.read_csv('statink-weapon2/statink-weapon2.csv')
    df = df.drop(['[de-DE]', '[en-GB]', '[en-US]', '[es-ES]', '[es-MX]', '[fr-CA]',
                 '[fr-FR]', '[it-IT]', '[ja-JP]', '[nl-NL]', '[ru-RU]', '[zh-CN]', '[zh-TW]', 'splatnet'], axis=1)
    df.to_csv('buki.csv')
    return df


if __name__ == '__main__':
    print(read_buki())

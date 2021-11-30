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


def convert_no(df):

    def inner_convert_no(df):
        return df.drop_duplicates().reset_index().drop("index", axis=1)

    keys = inner_convert_no(df["key"])
    categories1 = inner_convert_no(df["category1"])
    categories2 = inner_convert_no(df["category2"])
    mainweapons = inner_convert_no(df["mainweapon"])
    subweapons = inner_convert_no(df["subweapon"])
    specials = inner_convert_no(df["special"])

    print(keys)
    print(categories1)
    print(categories2)
    print(mainweapons)
    print(subweapons)
    print(specials)


if __name__ == '__main__':
    df = read_buki()
    print(df)
    convert_no(df)

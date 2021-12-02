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
    category1_no: str
    category2_no: str
    mainweapon_no: str
    subweapon_no: str
    special_no: str
    reskin_no: str


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

    print(categories1.index[(categories1['category1'] == 'roller')].tolist())
    print(
        categories1.index[(categories1['category1'] == 'roller')].tolist()[0])

    # Buki のデータクラスDictにする
    # dict[key] = Buki DataClass


if __name__ == '__main__':
    df = read_buki()
    print(df)
    convert_no(df)

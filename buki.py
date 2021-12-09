import pandas as pd
import dataclasses
from utility import *


@dataclasses.dataclass
class Buki:
    key: str
    category1: str
    category2: str
    mainweapon: str
    subweapon: str
    special: str
    category1_no: str
    category2_no: str
    mainweapon_no: str
    subweapon_no: str
    special_no: str


def read_buki():
    df = pd.read_csv('statink-weapon2/statink-weapon2.csv')
    df = df.drop(['[de-DE]', '[en-GB]', '[en-US]', '[es-ES]', '[es-MX]', '[fr-CA]',
                 '[fr-FR]', '[it-IT]', '[ja-JP]', '[nl-NL]', '[ru-RU]', '[zh-CN]', '[zh-TW]', 'splatnet', 'reskin'], axis=1)
    df.to_csv('buki.csv')
    return df


def convert_dict(df):

    def inner_convert_no(df):
        return df.drop_duplicates().reset_index().drop("index", axis=1)

    keys = inner_convert_no(df["key"])
    categories1 = inner_convert_no(df["category1"])
    categories2 = inner_convert_no(df["category2"])
    mainweapons = inner_convert_no(df["mainweapon"])
    subweapons = inner_convert_no(df["subweapon"])
    specials = inner_convert_no(df["special"])

    buki_dict = {}
    for _, row in df.iterrows():
        buki_dict[row.key] = Buki(key=row.key,
                                  category1=row.category1, category2=row.category2,
                                  mainweapon=row.mainweapon, subweapon=row.subweapon,
                                  special=row.special,
                                  category1_no=categories1.index[(
                                      categories1['category1'] == row.category1)].tolist()[0],
                                  category2_no=categories2.index[(
                                      categories2['category2'] == row.category2)].tolist()[0],
                                  mainweapon_no=mainweapons.index[(
                                      mainweapons['mainweapon'] == row.mainweapon)].tolist()[0],
                                  subweapon_no=subweapons.index[(
                                      subweapons['subweapon'] == row.subweapon)].tolist()[0],
                                  special_no=specials.index[(
                                      specials['special'] == row.special)].tolist()[0])
    return buki_dict


def replace_name2no(df):
    buki_df = read_buki()
    buki_dict = convert_dict(buki_df)
    # 別のファイルの関数と合わせないと動かない
    # 武器の名前を番号に置き換える
    team_index = ['A', 'B']
    header = list(df)
    if len([s for s in header if 'W1' in s]) > 0:
        team_index = ['W', 'L']
    print(df)
    x, y = extract_team_data(df, team_index, 'weapon')
    print(x)
    # TODO:辞書でDataFrameを置き換える方法を調べる
    tmp = buki_dict[x]
    print(tmp)
    print(tmp.category1_no)
    df[team_index[0]+'1-category1'] = buki_dict[x].category1_no
    print(df)


if __name__ == '__main__':
    df = read_buki()
    print(df)
    convert_dict(df)
    buki_dict = convert_dict(df)

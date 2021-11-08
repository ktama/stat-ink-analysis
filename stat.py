import pandas as pd

from data_importer import read_battle_result


def average(data, kind):
    data['WT-'+kind] = (data['W1-'+kind] + data['W2-'+kind] +
                        data['W3-'+kind] + data['W4-'+kind]) / 4
    data['LT-'+kind] = (data['L1-'+kind] + data['L2-'+kind] +
                        data['L3-'+kind] + data['L4-'+kind]) / 4
    return data


if __name__ == '__main__':
    gachi = read_battle_result()
    gachi = average(gachi, 'kill')
    gachi = average(gachi, 'assist')
    gachi = average(gachi, 'death')
    gachi = average(gachi, 'special')
    gachi = average(gachi, 'inked')
    gachi = average(gachi, 'level')
    gachi.to_csv('data.csv')

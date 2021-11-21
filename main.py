from data_importer import *
from stat_team import *

if __name__ == '__main__':
    # データインポート
    alpha_beta_gachi = read_battle_result()

    # 勝敗チームの傾向
    win_lose_gachi = translate_win_lose(alpha_beta_gachi)
    win_lose_stat = stat_team_data(win_lose_gachi)
    win_lose_stat.to_csv('win_lose_stat.csv')
    # 縦列の統計値を取る
    win_lose_stat_table = stat_table(filter(win_lose_gachi))
    win_lose_stat_table.to_csv('win_lose_stat_table.csv')

    # ルール別勝敗チームの傾向

    # alpha beta チームで勝敗予測
    alpha_beta_stat = stat_team_data(alpha_beta_gachi)
    alpha_beta_stat.to_csv('alpha_beta_stat.csv')

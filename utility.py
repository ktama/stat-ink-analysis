

def extract_team_data(df, team_index, category):
    x = df[[team_index[0]+'1-'+category, team_index[0]+'2-'+category,
            team_index[0]+'3-'+category, team_index[0]+'4-'+category]]
    y = df[[team_index[1]+'1-'+category, team_index[1]+'2-'+category,
            team_index[1]+'3-'+category, team_index[1]+'4-'+category]]
    return x, y

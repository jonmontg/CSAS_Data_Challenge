import polars as pl

def tree(df, category_column, player_type):
  return {item: player_type(df.filter(pl.col(category_column) == item)) for item in df[category_column].unique()}

class Player:
  def __init__(self, interactions):
    self.interactions = interactions

  def __getattr__(self, name):
    return self.interactions[name]

class Batter(Player):
  pass

class Pitcher(Player):
  pass

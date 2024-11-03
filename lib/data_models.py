import polars as pl
from .decorators import memoized

def player_lookup(df, category_column, player_type):
  return {item: player_type(df.filter(pl.col(category_column) == item)) for item in df[category_column].unique()}

class Player:
  def __init__(self, interactions):
    self.interactions = interactions

  def __getattr__(self, name):
    return self.interactions[name]

class Batter(Player):

  @memoized
  def swings(self):
    return self.interactions.filter(pl.col("swing_event"))

  @memoized
  def hits_into_play(self):
    return self.interactions.filter(pl.col("description") == "hit_into_play")

  def swing_percentage(self):
    return len(self.swings()) / len(self.interactions)

  def swing_contact_percentage(self):
    return len(self.interactions.filter(pl.col("description") == "hit_into_play")) / len(self.swings())

class Pitcher(Player):
  pass

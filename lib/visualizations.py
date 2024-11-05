import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

class Visualizations:
  def __init__(self, df):
    self.df = df

  def scatterplot(self, data, x, y, output_dir, name):
    sns.scatterplot(data=data, x=x, y=y)
    plt.savefig(Path(output_dir) / f"{name}.png")
    plt.close()

  def percentage_hit_into_play(self, variable, output_dir):
    data = self.df.filter(pl.col("swing_event")).group_by(variable).agg([
      (pl.col("hit_into_play").sum() * 100 / pl.len()).alias("percentage_hit_into_play")
    ]).with_columns(pl.col(variable).cast(pl.Float64))
    self.scatterplot(data, variable, "percentage_hit_into_play", output_dir, "percentage_hit_into_play")
    for pitch_type in self.df["pitch_type"].unique():
      data = self.df.filter((pl.col("pitch_type").eq(pitch_type) & pl.col("swing_event"))).group_by(variable).agg([
        (pl.col("hit_into_play").sum() * 100 / pl.len()).alias("percentage_hit_into_play")
      ]).with_columns(pl.col(variable).cast(pl.Float64))
      self.scatterplot(data, variable, "percentage_hit_into_play", output_dir, f"percentage_hit_into_play_{pitch_type}")

  def swing_length_to_hit_into_play_percentage(self, output_dir):
    self.percentage_hit_into_play("swing_length_bin", output_dir)

  def bat_speed_to_hit_into_play_percentage(self, output_dir):
    self.percentage_hit_into_play("bat_speed_bin", output_dir)

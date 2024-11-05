import polars as pl
from numpy import arange
from .logger import logger

SWING_EVENTS = {
  "hit_into_play",
  "foul",
  "foul_tip",
  "swinging_strike",
  "swinging_strike_blocked",
  "foul_bunt",
  "missed_bunt",
  "bunt_foul_tip"
}

def bins(col, increment, alias):
  mn = col.min()
  mx = col.max()
  return pl.col(col.name).cut(arange(mn, mx, increment), labels=list(map(str, arange(mn, mx+increment, increment)))).alias(alias)

def read_data(arrow_file):
  """
  Read the data from an arrow file.
  All columns with no information are removed.
  The game_date column is converted to a date object
  Data types are downsized via downsize_dtypes
  """
  logger.debug(f"Reading data from {arrow_file}.")
  df = pl.read_ipc(arrow_file, memory_map=False)
  return (df.select([col for col in df.columns if df[col].count() != 0 and len(df[col].value_counts()) > 1])
            .with_columns((
              pl.col("game_date").str.to_date("%Y-%m-%d"),
              pl.col("description").is_in(SWING_EVENTS).alias("swing_event"),
              pl.col("description").eq("hit_into_play").alias("hit_into_play"),
              bins(df["bat_speed"], 2.0, "bat_speed_bin"),
              bins(df["swing_length"], 0.1, "swing_length_bin")))
            .pipe(lambda x: x.with_columns((downsize_dtype(column) for column in x)))
            .filter(~pl.col("swing_event") | (pl.col("bat_speed").is_not_null() & pl.col("swing_length").is_not_null())))

def logged_conversion(logp, newtype):
  logp(newtype)
  return newtype

def downsize_dtype(column):
  """
  Integers are downsized to appropriate byte sizes
  Columns with categorical strings are converted to Categorical objects.
  """
  if column.dtype == pl.String or column.name in {"pitcher", "batter", "on_3b", "on_2b", "on_1b", "pitcher_1", "fielder_2_1", "fielder_3", "fielder_4", "fielder_5", "fielder_6", "fielder_7", "fielder_8", "fielder_9"}:
    value_count = len(column.value_counts())
    log = lambda _: logger.info(f"Column {column.name} converted to Categorical. Found {value_count} categories.")
    if value_count < 1000:
      if column.dtype != pl.String:
        return pl.col(column.name).cast(pl.String).cast(logged_conversion(log, pl.Categorical))
      return pl.col(column.name).cast(logged_conversion(log, pl.Categorical))
  elif column.dtype in (pl.Int64, pl.Int32, pl.Int16):
    if column.min() >= 0:
      mx = column.max()
      log = lambda newtype: logger.info(f"Column {column.name} converted to {str(newtype)}. Max value found is {mx}.")
      if mx < 255:
        return pl.col(column.name).cast(logged_conversion(log, pl.UInt8))
      if mx < 65535:
        return pl.col(column.name).cast(logged_conversion(log, pl.UInt16))
      if mx < 4294967295:
        return pl.col(column.name).cast(logged_conversion(log, pl.UInt32))
    else:
      mx = column.max()
      mn = column.min()
      log = lambda newtype: logger.info(f"Column {column.name} converted to {str(newtype)}. Found range ({mn}-{mx}).")
      if mx < 127 and mn > -128:
        return pl.col(column.name).cast(logged_conversion(log, pl.Int8))
      if mx < 32767 and mn > -32768:
        return pl.col(column.name).cast(logged_conversion(log, pl.Int16))
      if mx < 2147483647 and mn > -2147483648:
        return pl.col(column.name).cast(logged_conversion(log, pl.Int32))
  return pl.col(column.name)

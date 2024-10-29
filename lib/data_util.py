import polars as pl
from .logger import logger

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
            .pipe(lambda x: x.with_columns(pl.col("game_date").str.to_date("%Y-%m-%d")))
            .pipe(lambda x: x.with_columns((pl.col(column.name).cast(downsize_dtype(column)) for column in x))))

def logged_conversion(logp, newtype):
  logp(newtype)
  return newtype

def downsize_dtype(column):
  """
  Integers are downsized to appropriate byte sizes
  Columns with categorical strings are converted to Categorical objects.
  """
  if column.dtype in (pl.Int64, pl.Int32, pl.Int16):
    if column.min() >= 0:
      mx = column.max()
      log = lambda newtype: logger.info(f"Column {column.name} converted to {str(newtype)}. Max value found is {mx}.")
      if mx < 255:
        return logged_conversion(log, pl.UInt8)
      if mx < 65535:
        return logged_conversion(log, pl.UInt16)
      if mx < 4294967295:
        return logged_conversion(log, pl.UInt32)
    else:
      mx = column.max()
      mn = column.min()
      log = lambda newtype: logger.info(f"Column {column.name} converted to {str(newtype)}. Found range ({mn}-{mx}).")
      if mx < 127 and mn > -128:
        return logged_conversion(log, pl.Int8)
      if mx < 32767 and mn > -32768:
        return logged_conversion(log, pl.Int16)
      if mx < 2147483647 and mn > -2147483648:
        return logged_conversion(log, pl.Int32)
  if column.dtype == pl.String:
    value_count = len(column.value_counts())
    log = lambda _: logger.info(f"Column {column.name} converted to Categorical. Found {value_count} categories.")
    if value_count < 1000:
      return logged_conversion(log, pl.Categorical)
  return column.dtype

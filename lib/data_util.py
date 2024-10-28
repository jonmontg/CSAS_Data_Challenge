import polars as pl

def read_data(arrow_file):
  df = pl.read_ipc(arrow_file, memory_map=False)
  return (df.select([col for col in df.columns if df[col].count() != 0 and len(df[col].value_counts()) > 1])
            .pipe(lambda x: x.with_columns(pl.col("game_date").str.to_date("%Y-%m-%d")))
            .pipe(lambda x: x.with_columns((pl.col(column.name).cast(downsize_dtype(column)) for column in x))))

def downsize_dtype(column):
  if column.dtype in (pl.Int64, pl.Int32, pl.Int16):
    if column.min() >= 0:
      if column.max() < 255:
        return pl.UInt8
      if column.max() < 65535:
        return pl.UInt16
      if column.max() < 4294967295:
        return pl.UInt32
    else:
      if column.max() < 127 and column.min() > -128:
        return pl.Int8
      if column.max() < 32767 and column.min() > -32768:
        return pl.Int16
      if column.max() < 2147483647 and column.min() > -2147483648:
        return pl.Int32
  if column.dtype == pl.String and len(column.value_counts()) < 1000:
    return pl.Categorical
  return column.dtype

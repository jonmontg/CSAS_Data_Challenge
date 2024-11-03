from functools import wraps

class memoized:
  """
  Descriptor class for memoizing method results on a per-instance basis.
  """
  def __init__(self, func):
    self.func = func
    self.cache_name = f"_cache_{func.__name__}"

  def __get__(self, instance, cls=None):
    if instance is None:
      return self

    @wraps(self.func)
    def wrapper(*args, **kwargs):
      cache = getattr(instance, self.cache_name, {})
      key = str(args) + str(dict(sorted(kwargs.items())))
      if key not in cache:
        cache[key] = self.func(instance, *args, **kwargs)
        setattr(instance, self.cache_name, cache)
      return cache[key]

    return wrapper
from io import StringIO


class HtmlBuilder:
  def __init__(self, output, tag=None, **properties):
    self.output = output
    self.tag = tag
    self.properties = properties
    self.children = []

  def add(self, tag, text=None, **properties):
    ss = StringIO()
    self.children.append(ss)
    if text is None:
      component = HtmlBuilder(ss, tag, **properties)
      return component
    self._tag(tag, text, ss)
    return self

  def _tag(self, tag, value, output):
    if tag is not None:
      output.write(f"<{tag} {' '.join(key+'='+value for key, value in self.properties.items())}>")
    output.write(value)
    if tag is not None:
      self.output.write(f"</{tag}>")

  def __enter__(self):
    return self

  def __exit__(self, *args):
    self._tag(self.tag, "".join(map(lambda x: x.getvalue(), self.children)), self.output)
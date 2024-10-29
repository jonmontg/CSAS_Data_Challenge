from io import StringIO
import traceback

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

  def __exit__(self, exc_type, exc_value, exc_traceback):
    if exc_type:
      print("An exception has occurred: ", exc_value)
      traceback.print_tb(exc_traceback)
      return False
    self._tag(self.tag, "".join(map(lambda x: x.getvalue(), self.children)), self.output)

def _parse_description_lookup(definition_file):
  """
  Parse the contents of the data_definitions markdown file into a dictionary of column names
  and column descriptions. Column descriptions are formatted as html divs.
  """
  lookup = {}
  field = None
  with open(definition_file, "r") as f:
    for line in f:
      if line.startswith("### "):
        if field is not None:
          lookup[field] = lookup[field] + "</div>"
        field = line[4:].strip()
        lookup[field] = "<div>"
      elif field is not None:
        lookup[field] = lookup[field] + line + "<br>"
  return lookup

def build_description_table(df, definition_file, output_file):
  """
  Create an HTML file with a data dictionary describing the dataframe with the definitions
  specified in the definition file.
  """
  header = ["column", "description", "data_type"]
  lookup = _parse_description_lookup(definition_file)
  with open(output_file, "w") as f:
    with HtmlBuilder(f) as html:
      with html.add("table", border="1") as table:
        with table.add("tr") as row:
          for head in header:
            row.add("th", head)
        for column in df:
          with table.add("tr") as row:
            row.add("td", column.name)
            if column.name in lookup:
              row.add("td", lookup[column.name])
            else:
              row.add("td", "")
            row.add("td", str(column.dtype))

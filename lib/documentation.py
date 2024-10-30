from io import StringIO
import traceback
from pathlib import Path
import polars as pl

class HtmlBuilder:
  def __init__(self):
    self.html = ""
    self.indent = 0

  def __str__(self):
    return self.html

  def _add_indent(self):
    return "  " * self.indent

  def _open_tag(self, tag, **properties):
    self.html += f"{self._add_indent()}<{tag} {' '.join(key+'='+value for key, value in properties.items())}>\n"
    self.indent += 1

  def _close_tag(self, tag):
    self.indent -= 1
    self.html += f"{self._add_indent()}</{tag}>\n"

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    pass

  def save(self, file):
    with open(file, "w") as f:
      f.write(str(self.html))

  def tag(self, tag_name, **properties):
    """
    Allows using 'with' to open a tag, and automatically close it when the block ends.
    """
    class TagContext:
      def __init__(self, builder, tag_name):
        self.builder = builder
        self.tag_name = tag_name

      def __enter__(self):
        self.builder._open_tag(self.tag_name, **properties)
        return self.builder

      def __exit__(self, exc_type, exc_val, exc_tb):
        self.builder._close_tag(self.tag_name)

    return TagContext(self, tag_name)

  def text(self, content):
    self.html += f"{self._add_indent()}{content}\n"

# class HtmlBuilder:
#   def __init__(self, output, tag=None, **properties):
#     self.output = output
#     self.tag = tag
#     self.properties = properties
#     self.children = []

#   def add(self, tag, text=None, **properties):
#     ss = StringIO()
#     self.children.append(ss)
#     if text is None:
#       element = HtmlBuilder(ss, tag, **properties)
#       return element
#     self._tag(tag, text, ss)
#     return self

#   def _tag(self, tag, value, output):
#     if tag is not None:
#       output.write(f"<{tag} {' '.join(key+'='+value for key, value in self.properties.items())}>")
#     output.write(value)
#     if tag is not None:
#       self.output.write(f"</{tag}>")

#   def __enter__(self):
#     return self

#   def __exit__(self, exc_type, exc_value, exc_traceback):
#     if exc_type:
#       print("An exception has occurred: ", exc_value)
#       traceback.print_tb(exc_traceback)
#       return False
#     self._tag(self.tag, "".join(map(lambda x: x.getvalue(), self.children)), self.output)

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

def build_description_table(df, definition_file, output_file, short_cat_size=30, long_cat_show_size=5):
  """
  Create an HTML file with a data dictionary describing the dataframe with the definitions
  specified in the definition file.
  """
  lookup = _parse_description_lookup(definition_file)
  with HtmlBuilder() as html:
    with html.tag("table", border="1"):
      with html.tag("tr"):
        for head in ["column", "description", "data_type", "details"]:
          with html.tag("th"):
            html.text(head)
      for column in df:
        with html.tag("tr"):
          with html.tag("td"):
            html.text(column.name)
          with html.tag("td"):
            if column.name in lookup:
              html.text(lookup[column.name])
          with html.tag("td"):
            html.text(str(column.dtype))
          with html.tag("td"):
            if column.dtype == pl.Categorical:
              uniq = column.unique()
              with html.tag("ul"):
                show_size = long_cat_show_size if len(uniq) > short_cat_size else short_cat_size
                for opt in uniq[:show_size]:
                  with html.tag("li"):
                    if len(opt) == 0:
                      html.text("\"\"")
                    else:
                      html.text(opt)
                if len(uniq) > show_size:
                  html.text("...")
    html.save(output_file)

def build_categorical_documentation(df, path, *cols):
  for col in cols:
    df[col].unique().write_csv(Path(path) / f"{col}.csv")

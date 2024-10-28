from .html_builder import HtmlBuilder


def _parse_description_lookup(definition_file):
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

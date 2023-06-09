import re
import ark
import toml

@ark.filters.register('file_text')
def parse_toml(text, meta_dict):
    if text.startswith("~~~\n"):
        if match := re.match(r"^~~~\n(.*?\n)~~~\n", text, re.DOTALL):
            text = text[match.end(0):]
            data = toml.loads(match.group(1))
            meta_dict.update(data)
    return text

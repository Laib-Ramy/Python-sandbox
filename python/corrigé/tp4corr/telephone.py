import re

def internationalize(tel):
    pattern=r'^(0)(\d-\d{2}-\d{2}-\d{2}-\d{2})$'
    m=re.match(pattern, tel) 
    if m:
        return f'+33-{m.group(2)}'
    raise ValueError("Wrong format")


    
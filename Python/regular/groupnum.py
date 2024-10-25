import re
match = re.search(r'(\d+)-(\d+),id: (\d+)', 'Phone: 123-4567,id: 1234')
if match:
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

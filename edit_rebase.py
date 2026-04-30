import sys, re
f = sys.argv[1]
with open(f, 'r') as file:
    content = file.read()
content = re.sub(r'(?m)^pick 556751e', 'edit 556751e', content)
with open(f, 'w') as file:
    file.write(content)

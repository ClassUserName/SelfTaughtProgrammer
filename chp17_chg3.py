import re

t = "The ghost that says boo haunts the loo."

found = re.findall(".oo", t)

print(found)

import re

t = "Arizona 479, 501, 870. California 209, 213, 650."

#matches all 3 digits
match = re.findall("\d\d\d", t)

print(match)

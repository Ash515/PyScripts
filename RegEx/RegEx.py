import re
txt="The man in the forest"
c = re.search("^The.*forest$", txt)
if c:
    print("Finded ")
else:
    print("Not in")





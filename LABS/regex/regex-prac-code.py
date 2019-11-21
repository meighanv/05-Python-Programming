"""
1. Recognize the following strings: “bat,” “bit,” “but,” “hat,”
“hit,” or “hut.”
"""
string = """
1. Recognize the following strings: “bat,” “bit,” “but,” “hat,”
“hit,” or “hut.”
"""

import re
pattern = re.compile(r'[HB].t', re.IGNORECASE)
matches = pattern.findall(string)

print(type(matches))
for match in matches:
    print(match)

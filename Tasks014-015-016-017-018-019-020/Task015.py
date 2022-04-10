import re

string2 = 'b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'
print(re.findall(r'\ba(?:aa)*(?:|ccc|ccccc)(?:bb)+\b', string2))
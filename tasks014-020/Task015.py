import re

string2 = 'b a ab aaabbb aaacccbbbb aaaccccbbbb aaacccccbb aaaabb aaaaabb'
def task15(string2):
    return(re.findall(r'\ba(?:aa)*(?:|ccc|ccccc)(?:bb)+\b', string2))
print(task15(string2))
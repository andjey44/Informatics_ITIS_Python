import re
string1 = 'aaab aaaac aaad ae ad b aed'
pattern1=re.compile(r'\b\w+\B[c-z]')
print(pattern1.findall(string1))
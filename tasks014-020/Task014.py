import re
string1 = 'aaab aaaac aaad ae ad b aed'
def task14(string1):
# pattern1=re.compile(r'\b\w+\B[c-z]')
# print(pattern1.findall(string1))
    return re.findall(r'\ba+[^b]\b', string1)
print(task14(string1))

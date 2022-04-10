import re

x = open('example.txt', 'r')
print(re.findall(r'\ba+[^b]\b', x.readline()))
print(re.findall(r'\ba(?:aa)*(?:|ccc|ccccc)(?:bb)+\b', x.readline(2)))
print(re.findall(r'\b(?:[0-1][0-9]|2[0-4]):[0-5][0-9]', x.readline(3)))
print(re.findall(r'\b[A-Z А-ЯЁ]{2,}\b', x.readline(4)))
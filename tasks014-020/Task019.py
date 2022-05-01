import re

x = open('example.txt', 'r')
print(re.findall(r'\ba+[^b]\b', x.readline()))
print(re.findall(r'\ba(?:aa)*(?:|ccc|ccccc)(?:bb)+\b', x.readline(2)))
print(re.findall(r'\b(?:[0-1][0-9]|2[0-4]):[0-5][0-9]', x.readline(3)))
print(re.findall(r'\b[A-Z А-ЯЁ]{2,}\b', x.readline(4)))
print(re.findall(r'\b(?:(?:0[1-9]|1\d|2[0-8]|[1-9])-(?:0?2)-(?:\d+)|(?:0[1-9]|1\d|2\d|[1-9])-(?:0?2)-(?:(?:\d*?(?:(?:0[48]|[13579][26]|[2468][048])|(?:(?:[02468][048]|[13579][26])00))|[48]00|[48])(?=\D|\b))|(?:0[1-9]|1\d|2\d|30|[1-9])-(?:0?[469]|11)-(?:\d+)|(?:0[1-9]|1\d|2\d|3[01]|[1-9])-(?:0?[13578]|1[02])-(?:\d+))\b', x.readline(5)))
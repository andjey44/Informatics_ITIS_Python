import re
s = 'abc, ade, abcde, a, bc, abca, cear1, co, cola,coco, coza,colaco, c, cozo, car11'
pattern1=re.compile(r'\ba(?:bc|de)\b')
pattern2=re.compile(r'\b[ce]?ar1?\b')
pattern3=re.compile(r'\bco(?:la|co|za)?\b')
print(pattern1.findall(s))
print(pattern2.findall(s))
print(pattern3.findall(s))
with open('task5.txt', 'w', encoding='utf-8') as file:
    file.write('abc ade\n')
    file.write('car ear car1 ear1\n')
    file.write('co cola coco coza')

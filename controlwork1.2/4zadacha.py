import re
s= 'qe qee qeee qeeeee qaeee qaee'
pattern1=re.compile(r'\bq\w*(?:[e]{2})*\b')
pattern2=re.compile(r'\be.j\w*\\.\b')
pattern3=re.compile(r'\b.*(?:[euioay][qwrtpsdfghjklzxcvbnm][euioay][qwrtpsdfghjklzxcvbnm])+|(?:[qwrtpsdfghjklzxcvbnm][euioay][qwrtpsdfghjklzxcvbnm][euioay])+.*\b')
print(pattern1.findall(s))

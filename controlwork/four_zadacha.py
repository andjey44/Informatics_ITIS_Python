import re
# string=input()
# pattern1=re.compile(r'\b0{2,}1{2,}\b')
# print(pattern1.findall(string))
# string1=input()
# pattern2=re.compile(r'\d*01\d*')
# print(pattern2.findall(string1))
string2=input()
pattern3=re.compile(r'(\d*00\d*11\d*|\d*11\d*00\d*)')
print(pattern3.findall(string2))

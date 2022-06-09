import re
from Task019 import z
# string3='00:59, 03:15, 04:20, 18:30,25:60, 13:71, 101:02, 01:14'
# s = '1 2 6 23 43 35 67 4 33 21 21 10 45 34'
def task16(string3):
    return(re.findall(r'\b(?:[0-1][0-9]|2[0-4]):[0-5][0-9]', string3))
if __name__ == '__main__':
    for string3 in z:
        if task16(string3):
            print(task16(string3))
# print(task16(string3))
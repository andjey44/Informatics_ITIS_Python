import re
from Task019 import z
# string4='ООО, ИП, НИИ МАНАНАЗЭМ, ООН, ИТИС КФУ, ФизРа'
def task17(string4):
    return(re.findall(r'\b[A-Z А-ЯЁ]{2,}\b', string4))
if __name__ == '__main__':
    for string4 in z:
        if task17(string4):
            print(task17(string4))
# print(task17(string4))
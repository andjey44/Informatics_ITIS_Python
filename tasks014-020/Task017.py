import re
string4='ООО, ИП, НИИ МАНАНАЗЭМ, ООН, ИТИС КФУ, ФизРа'
def task17(string4):
    return(re.findall(r'\b[A-Z А-ЯЁ]{2,}\b', string4))
print(task17(string4))
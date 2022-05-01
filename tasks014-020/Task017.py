import re
string4='ООО, ИП, НИИ МАНАНАЗЭМ, ООН, ИТИС КФУ, ФизРа'
print(re.findall(r'\b[A-Z А-ЯЁ]{2,}\b', string4))
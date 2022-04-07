import re
st='10001 0 01000100 01 000 000010 10101010 110 10100 10 10010101010 010100 100 10010101001'
patterns=[r'\b1(?:10|11)1\b', r'\b0[01]1?01?\b', r'\b(?:00|11)?(?:101|01)\b']
with open('task5_output', 'w') as f:
    for p in patterns:
        f.write(str(re.findall(p, st)) + '\n')

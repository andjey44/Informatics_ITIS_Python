# count = {}
# for w in open('Text.txt').read().split():
#     if w in count:
#         count[w] += 1
#     else:
#         count[w] = 1
# for word, times in count.items():
#     print(word, times)
# print(len(set(open('Text.txt').read().lower().split())))
# f = open("Text.txt", "r")
# z=0
# while(True):
#     line = f.readline()
#     print(line)
#     z+=(len(set(line.lower().split())))
#     if not line:
#         break
#
# f.close()
# print(z)
from functools import reduce
import doctest
z=0
d=0
count = []
with open('Text.txt','r+', encoding='utf-8') as f:
    string = f.read()
    new_string = string.upper()
    new_string = new_string.replace('–', '')
    new_string = new_string.replace('-', '')
    new_string = new_string.replace(';', '')
    new_string = new_string.replace('?', '')
    new_string = new_string.replace('!', '')
    new_string = new_string.replace(':', '')
    new_string = new_string.split()
    number_of_unique_elements = len(set(new_string))
    f.write('\n' + '\n')
    f.write(str(number_of_unique_elements) + '\n')
    f.write('\n')
    print(set(new_string))
    print(number_of_unique_elements)
    new_string = list(new_string)
    slov = {}
    for i in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
        slov[i] = 0
    for w in new_string:
        if slov.get(w[0]) is not None:
            slov[w[0]] += 1
    for k in slov.keys():
        if slov[k] > 0:
            f.write(k + ':' + str(slov[k]) + '\n')
    f.write('\n')
    f.write((reduce(lambda a, b: a if len(a) > len(b) else b, new_string)) + '\n')
    f.write('\n')


    def most_frequent(string):

        counter = 0

        num = string[0]

        for i in string:

            curr_frequency = string.count(i)

            if (curr_frequency > counter):
                counter = curr_frequency

                num = i

        return num


    # count = new_string.count(('И'))
    # count2 = new_string.count(('В'))
    # print(count, count2)


    f.write((most_frequent(new_string)))


    def change(izn, col):
        code = list(izn)
        for _, s in enumerate(code):
            code[_] = chr((ord(s) - ord('А') + col + 32) % 32 + ord('А'))
        return ''.join(code)
    string = string.upper()
    # print(string)


    for __, s in enumerate(new_string):
        if len(s) > 4:
            if len(s) % 2 == 0:
                string = string.replace(s, change(s, 1))
            else:
                string = string.replace(s, change(s, -1))



    f.write('\n' + '\n' + string)
if __name__ == '__main__':
    # doctest.testmod()
    doctest.testfile('Text.txt')

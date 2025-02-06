# 1
def count_letter(lst, lttr):
    print(lst)
    print(lttr)
    count = 0
    for word in lst:
        if lttr.upper() in word or lttr.lower() in word:
            count += 1
    print(count)

lstwrd = input('input: ').split()
for i in range(3):
    lttr = input('letter: ')
    count_letter(lstwrd, lttr)
# 1
date_1 = input('Введите дату: ')
task_1 = input('Введите задачу: ')
print(date_1 + ' ' + task_1)

# 2
prnt = []
for i in range(3):
    date_i = input('Введите дату: ')
    task_i = input('Введите задачу: ')
    tmd = date_i + ' ' + task_i
    prnt.append(tmd)
print('\n'.join(prnt))

# 3
dict = {}
for j in range(3):
    date_j = input('Введите дату: ')
    task_j = input('Введите задачу: ')
    dict[date_j] = task_j
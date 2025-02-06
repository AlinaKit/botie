import random
import pickle

HELP = """\
/help - напечатать справку по программе.
/name yourname - представиться боту
/add date task - добавить задачу в список (формат команда`дата`задача).
/show date - напечатать все добавленные задачи(формат команда`дата).
/stop - выход из программы.
/random date - добавление случайной задачи(формат команда`дата)."""

tasks = {}
randomie = [['Написать', 'Обновить', 'Проверить'], ['приложение', 'программу', 'игру'], ['telegramm', 'vk', 'ok.ru']]
def randomtask():
    return f'{random.choice(randomie[0])} {random.choice(randomie[1])} для {random.choice(randomie[2])}'

def addie(day_check, task):
    global tasks
    if day_check not in tasks:
      tasks[day_check] = [task]
    else:
      tasks[day_check].append(task)
    return f"Задача {task} добавлена на дату {day_check}."

# while True:
#   command = input("Введите команду: ")
#   if command == "help":
#     print(HELP)
#   elif command == "show":
#     day_check = input('Введите дату задачи: ')
#     if day_check in tasks:
#       for task in tasks[day_check]:
#         print(f'- {task}')
#     else:
#       print('Нет такой даты.')
#   elif command == "add":
#     day_check = input('Введите дату задачи: ')
#     task = input("Введите название задачи: ")
#     addie(day_check, task)
#   elif command == 'random':
#     day_check = input('Введите дату задачи: ')
#     task = randomtask()
#     addie(day_check, task)
#   elif command == 'exit':
#     print("Спасибо за использование!", end=' ')
#     break
#   else:
#     print("Неизвестная команда. help для списка команд.", end=' ')
#     break
#
# print("До свидания!")
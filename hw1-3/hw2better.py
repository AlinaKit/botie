import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы.
random - добавление случайной задачи."""

tasks = {}
randomie = [['Написать', 'Обновить', 'Проверить'], ['приложение', 'программу', 'игру'], ['telegramm', 'vk', 'ok.ru']]
def randomtask():
    # i = randint(0, 2)
    # j = randint(0, 2)
    # k = randint(0, 2)
    # return f'{randomie[0][i]} {randomie[1][j]} для {randomie[2][k]}'
    return f'{random.choice(randomie[0])} {random.choice(randomie[1])} для {random.choice(randomie[2])}'

def addie(day_check, task):
    global tasks
    if day_check not in tasks:
      tasks[day_check] = [task]
    else:
      tasks[day_check].append(task)
    print(f"Задача {task} добавлена на дату {day_check}.")

while True:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    day_check = input('Введите дату задачи: ')
    if day_check in tasks:
      for task in tasks[day_check]:
        print(f'- {task}')
    else:
      print('Нет такой даты.')
  elif command == "add":
    day_check = input('Введите дату задачи: ')
    task = input("Введите название задачи: ")
    addie(day_check, task)
  elif command == 'random':
    day_check = input('Введите дату задачи: ')
    task = randomtask()
    addie(day_check, task)
  elif command == 'exit':
    print("Спасибо за использование!", end=' ')
    break
  else:
    print("Неизвестная команда. help для списка команд.", end=' ')
    break

print("До свидания!")
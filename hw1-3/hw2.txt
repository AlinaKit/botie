HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы"""

# 1
tasks = []

while True:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")
  elif command == 'exit':
    print("Спасибо за использование!", end=' ')
    break
  else:
    print("Неизвестная команда.", end=' ')
    break

print("До свидания!")

# 2
today = []
tomrr = []
tohard = []

while True:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    day_check = input('Введите дату задачи: ')
    task = input("Введите название задачи: ")
    if day_check == 'Сегодня':
        today.append(task)
    elif day_check == 'Завтра':
        tomrr.append(task)
    else:
        tohard.append(task)
    print("Задача добавлена")
  elif command == 'exit':
    print("Спасибо за использование!", end=' ')
    break
  else:
    print("Неизвестная команда.", end=' ')
    break

print("До свидания!")
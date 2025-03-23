write = [
    "Список:"
]
print(write)

while True:
    choice = int(input("Выбор\n1. Написать список в терминал \n2. Добавить задачу \n3. Очистить список \n4. Выйти\n"))
    if choice == 1:
        print(write)

    if choice == 2:
        name = input("name: ")

        write.append(name)

        with open ("taskes.txt", 'w', encoding="utf-8") as f:
            index = 0
            for repeat in range(len(write)):
                f.write(write[index])
                f.write('\n')
                index = index+1

    if choice == 3:
        with open ("taskes.txt", 'w', encoding="utf-8") as f:
            f.write('Список: ')
    if choice == 4:
        exit()
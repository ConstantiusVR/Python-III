def add_student():
    name = input()
    last_name = input()
    add_pers_data = f"{name},{last_name} \n"
    with open('class_book.txt','a') as data:
        data.write(add_pers_data)
    print('Ученик добавлен')

def add_subject():
    subject = input()
    pers_data = f"{subject} \n"
    with open('class_book.txt','a') as data:
        data.write(pers_data)
    print('Предмет добавлен')


def add_mark():
    mark = int(input())
    pers_data = f"{mark} \n"
    with open('class_book.txt','a') as data:
        data.write(pers_data)
    print('Оценка добавлена')

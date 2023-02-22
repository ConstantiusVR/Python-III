def average_mark_by_subject():
    pass
#      with open('class_book.txt', 'r') as data:
#         for pers_data in data.readlines():
            

def average_mark_by_class_by_subject():
    pass

def best_students():
    pass

def names_list():
    with open('class_book.txt', 'r') as data:
        for pers_data in data.readlines():
            temp = pers_data.split(',')
            print (f"Name - {temp[0]}, Last name - {temp[1]}")


def all_marks_by_student():
    with open('class_book.txt', 'r') as data:
        for pers_data in data.readlines():
            temp = pers_data.split(',')
            print (f"Last name - {temp[1]}, subject:{temp[2]}, marks:{temp[3]}")

            
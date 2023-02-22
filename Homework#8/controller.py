import view
import selection
import generate_classbook
import output_classbook
import input_classbook 



def start(): 
    while True:
        creation_new_class = generate_classbook.gen_classbook()
        op_code = None
        number = view.operation()
        if number == 0:
            op_code = output_classbook.get_database()
        elif number ==1:
            op_code = input_classbook.add_student()
        elif number ==2:
            op_code = input_classbook.add_subject()
        elif number ==3:
            op_code = input_classbook.add_mark()
        elif number ==4:
            op_code = selection.names_list()
        elif number ==5:
            op_code = selection.all_marks_by_student()
        elif number ==6:
            op_code = selection.average_mark_by_subject()
        elif number ==7:
            op_code = selection.average_mark_by_class_by_subject()
        elif number ==8:
            op_code = selection.best_students()
        elif number == 9:
            break  
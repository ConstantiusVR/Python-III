def gen_classbook():
    import random
    name = random.choice(['Steven','Paul','Andrew','Sean','Alan','Walter','William','Peter'])
    last_name = random.choice(['McBright','Kirby','Brennan','Fitzgerald','Clark','Lloyd','Patrick','Hartman'])
    subject = random.choice(['Math','History','Biology','Chemistry','PE'])
    mark = random.randint(1,5)
    pers_data = (f"{name} {last_name} - {subject}:{mark} \n")
    with open('class_book.txt','a') as data:
        data.write(pers_data)
        
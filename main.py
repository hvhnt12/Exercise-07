# TASK1
def create_file(file_name):
    with open(file_name, 'w') as f:
        f.write('Ada,Alan,Isabella,Lizbeth,Abigail,Meltem,Gülcan,John,Doe,Jane')


create_file('names.txt')


# TASK2
def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as input_f:
        input_str = input_f.read()

    words = input_str.split(',')

    with open(output_file, 'w') as output_f:
        for word in words:
            output_f.write(word.strip() + '\n')

    transform_to_row('names.txt', 'names_new.txt')


# TASK3

def add_greeting(input_file, output_file):
    with open(input_file, 'r') as inp:
        read = inp.readlines()

    update = []
    for i in read:
        new = 'Hello ' + i
        update.append(new)
    with open(output_file, 'w') as output:
        output.writelines(update)


add_greeting('names.txt', 'new_names.txt')


# TASK4

def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as inp:
        read = inp.read()
        strip = read.replace('Hello ', '')

    with open(output_file, 'w') as output:
        output.writelines(strip)


strip_greeting('names.txt', 'new_names.txt')


# TASK5

def combine_files(file1, file2, output_file):
    with open(file1, 'r') as file1:
        read1 = file1.readlines()
    with open(file2, 'r') as file2:
        read2 = file2.readlines()

    combined = []
    for i, j in zip(read1, read2):
        combined.append(i.strip('\n') + ' ' + j)

    with open(output_file, 'w') as output:
        output.writelines(combined)


combine_files('names.txt', 'new_names.txt', 'combined.txt')

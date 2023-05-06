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

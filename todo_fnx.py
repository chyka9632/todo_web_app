FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):  # read a text file and return the list of read to_do items
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # write a to_do item list to the text file
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__todo__":
    print("hello")

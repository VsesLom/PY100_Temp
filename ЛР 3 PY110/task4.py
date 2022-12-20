INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    # перезаписать содержимое одного файла в другой
    with open(INPUT_FILE) as f_1:
        with open(OUTPUT_FILE, 'w') as f_2:
            for line in map(str.upper, f_1):
                f_2.write(line)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")

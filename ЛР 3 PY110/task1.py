INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE) as file:  # открыть указатель на файл
        # файл является итератором, который работает с циклом for в построчном режиме
        for line in file:
            print(line.rstrip())

if __name__ == "__main__":
    task()

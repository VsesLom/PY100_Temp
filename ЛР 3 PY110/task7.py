import json


def task():
    filename = "input.json"
    with open(filename) as f: # считать содержимое JSON файла
        data = json.load(f)
    return max(data, key=lambda x: x["score"])  # найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())

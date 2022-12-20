import json


def task():
    filename = "input.json"
    with open(filename) as f:
        data = json.load(f)

    map_iterator = map(lambda x: x["score"] * x["weight"], data)
    return sum(map_iterator)


if __name__ == "__main__":
    result = task()
    print(f"{result:.3f}")

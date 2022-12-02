def task(numbers: list) -> int:
    return sum(n ** 3 for n in numbers if n < 0)


if __name__ == "__main__":
    list_numbers = [-2, -1, 0, 1, -3, 2, -3]
    print(task(list_numbers))

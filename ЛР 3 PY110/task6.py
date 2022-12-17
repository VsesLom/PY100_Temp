import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename) as inp_f:  # считать содержимое json файл input.json
        data = json.load(inp_f)
    with open(output_filename, 'w') as out_f:  # записать содержимое в json файл output.json с отступами
        json.dump(data, out_f, indent=4)


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")

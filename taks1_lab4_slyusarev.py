# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    data = []
    with open(INPUT_FILENAME, 'r', newline='') as csvfile:
        read_csv = csv.DictReader(csvfile)
        for row in read_csv:
            data.append(row)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as result:
        for line in result:
            print(line, end="")

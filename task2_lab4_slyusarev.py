import json


# TODO решите задачу
def task() -> float:
    with open("input.json", "r") as file_read:
        data = json.load(file_read)

    sum_products = 0

    for item in data:
        sum_products += item["score"] * item["weight"]
    return sum_products


print(task())

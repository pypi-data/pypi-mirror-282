from datadict import DataDict
import pandas as pd

data = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21},
    {"name": "Jim", "age": 22},
    {"name": "Jack", "age": 23, "heart_rate": {"value": 120, "unit": "bpm"}},
]

data2 = [
    {"name": "John", "age": "20"},
    {"name": "Jane", "age": "21"},
    {"name": "Jim", "age": "22"},
    {"name": "Jack", "age": "23", "heart_rate": {"value": 120, "unit": "bpm"}},
]

# dd2 = DataDict(data2)
# print(dd2)
# dd2.to_int("age")
# print(dd2)

# n = 5
# print(type(n))
# print(type(float(n)))
# print(float(n))


d = {"a": 1, "b": 2, "c": 3}

print(str(d))
print(type(str(d)))


# pyplup = DataDict(data)
# # print(pyplup)
# # print(type(pyplup[0]))


# # print(pyplup.select("name"))
# # print(pyplup.select("name", "age"))

# print(pyplup.where("name", "==", "John"))
# print(pyplup.where("heart_rate.value", ">", 100))

# print(pyplup.where("heart_rate.value", ">", 100).select("name", "heart_rate.value"))

# pyplup.append({"name": "Josh", "age": 35})

# print(pyplup)

# pyplup.sort(key=lambda x: x["age"], reverse=True)
# sorted_data = pyplup
# print("Sorted by age:", sorted_data)

# print(pyplup.where("age", ">", 20))


# # pyplup.append("hello")

# # print(pyplup)

# # print("\n")

# # print(dir(list))


# # print(dir(dict))

# d = {"a": 1, "b": 2, "c": 3}


# conditions = [
#     "a > 1",
#     "b < 2",
#     "c == 3",
#     "d != 4",
#     "e >= 5",
#     "f <= 6",
#     "g>10",
#     "h<=11",
#     "d === 5",
# ]


# def parse_condition(condition: str):
#     import re

#     parts = re.split(r"(>=|<=|==|!=|>|<)", condition, 2)
#     return parts[0].strip(), parts[1].strip(), parts[2].strip()


# for condition in conditions:
#     print(parse_condition(condition))

# dd = DataDict(data)
# print(dd.tail(-2))
# print(dd.tail(2) == dd.tail(-2))


# export PYTHONPATH=/Users/eijaz/Documents/github_pyph/pyph
# then from pyph folder, the below command will run the tests
# pytest tests

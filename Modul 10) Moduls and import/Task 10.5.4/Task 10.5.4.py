import os

lst = [
    "First line\n",
    "Second line\n",
    "Third line\n",
    "Second line\n",
]

with open("input.txt", "w") as input_file:
    input_file.writelines(lst)

with open("input.txt") as input_file:
    with open("output.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line)





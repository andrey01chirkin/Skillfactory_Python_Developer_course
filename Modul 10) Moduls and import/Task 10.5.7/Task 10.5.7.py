

with open("input_data.txt") as input_data:
    lst = input_data.readlines()
    lst.reverse()
    with open("output_data.txt", "w") as output_data:
        output_data.writelines(lst)


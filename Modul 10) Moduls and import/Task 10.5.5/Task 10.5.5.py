
with open("numbers.txt") as numbers_file:
    lst = []
    for line in numbers_file:
        lst.append(float(line))
    print(lst)
    sum = max(lst) + min(lst)
    print(f"sum = {sum}")

with open("output.txt", "w") as output_file:
    output_file.write(str(sum))




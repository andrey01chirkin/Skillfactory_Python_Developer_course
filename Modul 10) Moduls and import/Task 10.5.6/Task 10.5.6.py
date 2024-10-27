
with open("source_file.txt", encoding='utf-8') as source_file:
    for line in source_file:
        point = int(line.split()[-1])
        if point < 3:
            print(" ".join(line.split()[:-1]))

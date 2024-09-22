
line = 'aaabbccccdaa'

result_line = ''
counter = 0
last_char = line[0]

for char in line:
    if char == last_char:
        counter += 1
    else:
        result_line += last_char + str(counter)
        last_char = char
        counter = 1

result_line += last_char + str(counter)

print(result_line)


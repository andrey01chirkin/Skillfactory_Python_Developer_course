#------------------------------------------------------------------------------------------------------------------------------------
# 5.5
# Напишите программу, которая будет считать количество всех подстрок независимо от регистра букв в них.
# Например, в такой фразе подстрока «тр» встречается шесть раз: «Три утёнка по три раза тёрли лапки
# потрёпанными мочалками и крякали друг другу: „смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!»
str = ("Три утёнка по три раза тёрли лапки потрёпанными мочалками и крякали друг другу: "
       "„смотри, мои лапки чище твоих!“ Смотри, утёнок, насквозь не протри!")

substr = "тр"

if len(str) and len(substr):
    print("5.5: ", str.casefold().count(substr.casefold()))
else:
    print("5.5: ", "Line is empty")
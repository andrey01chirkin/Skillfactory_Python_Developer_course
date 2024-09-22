symbols = ['a', 'b', 'c']
values = [1, 2, 3]
for x in symbols:
  print(x)
  squared = [x*x for x in values] # Все плохо. "x" из верхнего "for" затёрт
  print(x)

print()

symbols = ['a', 'b', 'c']
values = [1, 2, 3]
for x in symbols:
  print(x)
  squared = map(lambda x: x*x, values) # Все норм, это локальная область видимости
  print(x)


a = [(lambda n: n**2)(n) for n in range(10)]
b = list(map(lambda n: n**2, [n for n in range(10)]))


print(a)
print(b)


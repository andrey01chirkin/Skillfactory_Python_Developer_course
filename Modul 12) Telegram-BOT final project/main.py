
vehicles = ['car', 'motorbike', 'boat', 'ship']

res = 'Vehicles:\ncar'

for vehicle in vehicles:
    res = '\n'.join((res, vehicle))

print(res)


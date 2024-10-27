
def find_duplicates(arr):
  duplicates = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        duplicates.append(arr[i])
  return duplicates

def find_duplicates2(arr):
    duplicates = []
    unique_items = set()
    for item in arr:
        if item in unique_items:
            duplicates.append(item)
        else:
            unique_items.add(item)
    return duplicates

print(find_duplicates([1, 2, 3, 1, 1, 1, 2, 3, 3]))
print(find_duplicates2([1, 2, 3, 1, 1, 1, 2, 3, 3]))


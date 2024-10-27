"""
Как мы уже выяснили, текущий алгоритм поиска в ширину файла в N-арном дереве файловой системы не учитывает ситуацию, когда в
системе может быть несколько файлов с одним и тем же именем. Для решения этой проблемы вам предлагается модифицировать алгоритм
таким образом, чтобы он возвращал все пути к файлам с заданным именем.
"""

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None


def breadth_first_search_for_files(root, target_file):
    # Создаем очередь для обхода в ширину
    queue = Queue()
    queue.enqueue((root, ""))

    paths = []  # Список для хранения путей к файлам

    while not queue.is_empty():
        current_node, current_path = queue.dequeue()

        # Обновляем текущий путь, добавляя текущее имя узла
        current_path += current_node.name + "/"

        if current_node.name == target_file:
            # Если текущий узел содержит искомый файл, добавляем путь в список путей
            paths.append(current_path)

        # Добавляем детей текущего узла в очередь для дальнейшего обхода
        for child in current_node.children:
            queue.enqueue((child, current_path))

    return paths if paths else None
    

root = TreeNode("C:")

root.add_child(TreeNode("Summary.docx"))

documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))
documents.add_child(TreeNode("Summary.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))
pictures.add_child(TreeNode("Summary.docx"))

file_paths = breadth_first_search_for_files(root, 'Summary.docx')
for file_path in file_paths:
    print(file_path[:-1])
# C:/Summary.docx
# C:/Documents/Summary.docx
# C:/Pictures/Summary.docx


#Обход дерева в глубину не работает

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def depth_first_search_for_file(node, target_file, current_path=""):
    # Обновляем текущий путь, добавляя текущее имя узла
    current_path += node.name + "/"

    if node.name == target_file:
        # Если имя текущего узла совпадает с искомым файлом, возвращаем текущий путь
        return current_path

    if node.children:
        for child in node.children:
            # Рекурсивно вызываем функцию для каждого ребенка, передавая текущий путь
            result = depth_first_search_for_file(child, target_file, current_path)
            if result:
                return result

    # Если файл не найден в текущем поддереве, возвращаем None
    return None

root = TreeNode("C:")
documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Report.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("WorldSkills.jpg"))
pictures.add_child(TreeNode("Doctor.jpg"))

found_node = depth_first_search_for_file(root, 'Doctor.jpg')
print(found_node) # Report.docx
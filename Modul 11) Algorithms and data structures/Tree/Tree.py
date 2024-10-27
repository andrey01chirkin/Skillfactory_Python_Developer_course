class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_file_system(node, indent=""):
    print(indent + node.value + ("/" if not node.children else "\\"))
    if node.children:
        for child in node.children:
            print_file_system(child, indent + "  ")



if __name__ == "__main__":
    root = TreeNode("C:")

    documents = TreeNode("Documents")
    root.add_child(documents)
    documents.add_child(TreeNode("Homework.docx"))
    documents.add_child(TreeNode("Report.docx"))

    pictures = TreeNode("Pictures")
    root.add_child(pictures)
    pictures.add_child(TreeNode("Summer.jpg"))
    pictures.add_child(TreeNode("Winter.jpg"))

    print_file_system(root)
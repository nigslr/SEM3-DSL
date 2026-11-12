
# Binary Search Tree: Insertion, Deletion, Search and Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def minimum(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = minimum(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

while True:
    print("\n\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        root = insert(root, value)

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if search(root, value):
            root = delete(root, value)
            print("Node deleted.")
        else:
            print("Value not found.")

    elif choice == 3:
        value = int(input("Enter value to search: "))
        if search(root, value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == 4:
        print("Inorder:", end=" ")
        inorder(root)

    elif choice == 5:
        print("Preorder:", end=" ")
        preorder(root)

    elif choice == 6:
        print("Postorder:", end=" ")
        postorder(root)

    elif choice == 7:
        break

    else:
        print("Invalid choice!")

'''
1. Insert
2. Delete
3. Search
4. Inorder Traversal
5. Preorder Traversal
6. Postorder Traversal
7. Exit

Enter choice: 1
Enter value: 50

Enter choice: 1
Enter value: 30

Enter choice: 1
Enter value: 70

Enter choice: 4
Inorder: 30 50 70

Enter choice: 3
Enter value to search: 30
Value found.




Practical Title:. Binary Search Tree (BST) Creation, Insertion, Deletion and Traversal

Aim: Implement various operations on a Binary Search Tree, such as insertion, deletion, display, and search

Objective:
Construct a Binary Search Tree (BST)
Insert new nodes into the BST
Delete nodes from the BST
Perform In-order, Pre-order, and Post-order traversals

Input: A set of integers to be inserted into the BST and keys to be deleted

Outcome: Students will be able to implement and manipulate BSTs and understand the role of tree traversal in data processing.

Theory:
A Binary Search Tree is a node-based binary tree where each node has a comparable key and satisfies the property: left child < parent < right child.
Insertion: Place the node in left subtree if value is less, else in right subtree
Deletion: Delete leaf node directly; if one child, connect parent to that child; if two children, replace with inorder successor
Traversal: In-order gives sorted output, Pre-order for prefix expression, Post-order for postfix

Algorithm:
Insert(node, key):
1. If node is null create node
2. If key node.key insert into left subtree
3. Else insert into right subtree
Delete(node, key):
1. If node is null return null
2. Recurse left or right depending on key
3. If found:
If leaf delete
If one child replace with child
If two children replace with inorder successor
Inorder(node):
1. Traverse left
2. Print node
3. Traverse right
Preorder(node):
1. Print node
2. Traverse left
3. Traverse right
Postorder(node):
1. Traverse left
2. Traverse right
3. Print node

Conclusion:
By this way,
.
We implemented dynamic data structure for efficient data organization
Learned to manage nodes with recursive logic
Understood real-life importance of tree traversals
'''

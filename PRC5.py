class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        print("Student added successfully.")

    def display(self):
        if self.head is None:
            print("No student records found.")
            return

        temp = self.head

        print("\n-----------------------------------------")
        print("Roll No\tName\t\tMarks")
        print("-----------------------------------------")

        while temp is not None:
            print(temp.roll_no, "\t", temp.name, "\t\t", temp.marks)
            temp = temp.next

        print("-----------------------------------------")

    def search_student(self, roll_no):
        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("\nStudent Found")
                print("Roll No :", temp.roll_no)
                print("Name :", temp.name)
                print("Marks :", temp.marks)
                return
            temp = temp.next

        print("Student not found.")

    def delete_student(self, roll_no):
        if self.head is None:
            print("No student records found.")
            return

        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.roll_no == roll_no:
                temp.next = temp.next.next
                print("Student deleted successfully.")
                return
            temp = temp.next

        print("Student not found.")

    def update_student(self, roll_no):
        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("Current Name :", temp.name)
                print("Current Marks:", temp.marks)

                temp.name = input("Enter new name: ")
                temp.marks = float(input("Enter new marks: "))

                print("Student record updated successfully.")
                return
            temp = temp.next

        print("Student not found.")

    def sort_by_marks(self, order):
        if self.head is None:
            print("No records to sort.")
            return

        current = self.head

        while current is not None:
            index = current.next

            while index is not None:
                if order == "asc":
                    condition = current.marks > index.marks
                else:
                    condition = current.marks < index.marks

                if condition:
                    current.roll_no, index.roll_no = index.roll_no, current.roll_no
                    current.name, index.name = index.name, current.name
                    current.marks, index.marks = index.marks, current.marks

                index = index.next

            current = current.next

        print("Records sorted by marks.")

    def sort_by_roll(self, order):
        if self.head is None:
            print("No records to sort.")
            return

        current = self.head

        while current is not None:
            index = current.next

            while index is not None:
                if order == "asc":
                    condition = current.roll_no > index.roll_no
                else:
                    condition = current.roll_no < index.roll_no

                if condition:
                    current.roll_no, index.roll_no = index.roll_no, current.roll_no
                    current.name, index.name = index.name, current.name
                    current.marks, index.marks = index.marks, current.marks

                index = index.next

            current = current.next

        print("Records sorted by roll number.")

students = StudentList()

while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Sort by Marks")
    print("7. Sort by Roll Number")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        students.add_student(roll_no, name, marks)

    elif choice == "2":
        roll_no = int(input("Enter Roll No to delete: "))
        students.delete_student(roll_no)

    elif choice == "3":
        roll_no = int(input("Enter Roll No to update: "))
        students.update_student(roll_no)

    elif choice == "4":
        roll_no = int(input("Enter Roll No to search: "))
        students.search_student(roll_no)

    elif choice == "5":
        students.display()

    elif choice == "6":
        print("1. Ascending")
        print("2. Descending")
        order_choice = input("Enter choice: ")

        if order_choice == "1":
            students.sort_by_marks("asc")
        elif order_choice == "2":
            students.sort_by_marks("desc")
        else:
            print("Invalid choice.")
        
        students.display()

    elif choice == "7":
        print("1. Ascending")
        print("2. Descending")
        order_choice = input("Enter choice: ")

        if order_choice == "1":
            students.sort_by_roll("asc")
        elif order_choice == "2":
            students.sort_by_roll("desc")
        else:
            print("Invalid choice.")
            
        students.display()

    elif choice == "8":
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")

'''
===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 1
Enter Roll No: 09
Enter Name: Om Gaikwad
Enter Marks: 85
Student added successfully.

1. Aim
To implement a Student Record Management System using a singly linked list and perform
operations such as Add, Delete, Update, Search, Display, and Sort student records.

2. Introduction
A Linked List is a dynamic linear data structure in which elements are stored in the form of
nodes. Each node contains:
1. Data – information stored in the node.
2. Link/Pointer – reference to the next node.
For this practical, each student record contains:
 Roll Number
 Student Name
 Marks
 Link to the next student
The nodes are connected sequentially to form a linked list.

3. Node Structure
The structure of a student node can be represented as:

Roll No Name Marks Next
Pointer

Conceptually:

HEAD
↓
[101, Rahul, 85] → [102, Sneha, 92] → [103, Amit, 78] → NULL
HEAD stores the address/reference of the first node, while NULL indicates the end of the list.

4. Operations Performed
A. Add Student
A new node is created containing the student&#39;s roll number, name, and marks.
If the list is empty, the new node becomes the HEAD.
Otherwise, the list is traversed until the last node and the new node is attached to it.
Before:
HEAD → [101] → [102] → NULL

Add 103:

HEAD → [101] → [102] → [103] → NULL
Time Complexity: O(n) when inserting at the end.

B. Delete Student
Deletion removes a student record based on the Roll Number.
The list is traversed until the required node is found. The link of the previous node is changed so
that it points to the next node.
Before:

[101] → [102] → [103] → NULL

Delete 102:

[101] ─────────→ [103] → NULL
If the first node is deleted, HEAD is moved to the second node.
Time Complexity: O(n)

C. Update Student
The list is searched using the student&#39;s Roll Number.
After finding the required node, the Name and Marks can be modified.
Before:
[101, Rahul, 85]

After Update:
[101, Rahul, 90]
Time Complexity: O(n)

D. Search Student
Searching is performed using the Roll Number.
The list is traversed from the first node to the last node until the required Roll Number is found.
Example:
HEAD
↓
[101] → [102] → [103] → NULL
↑
Search 102

If the roll number exists, the student&#39;s complete record is displayed.
Time Complexity: O(n)

E. Display Student Records
The list is traversed from HEAD to NULL.
Each student&#39;s Roll Number, Name, and Marks are displayed.
HEAD
↓
[101] → [102] → [103] → NULL
↓ ↓ ↓
Display Display Display
Time Complexity: O(n)

F. Sort Student Records
Sorting arranges student records according to a particular field.
In this practical, records can be sorted by:
1. Roll Number
2. Marks
Two orders are supported:
 Ascending order
 Descending order
For example, sorting by marks in ascending order:
Before:

Rahul → 85
Sneha → 92
Amit → 78

After:

Amit → 78
Rahul → 85
Sneha → 92
Sorting Algorithm Used: Bubble Sort
Time Complexity: O(n²)

5. Why Linked List is Used?
A linked list is useful for student records because:
 Its size can grow or shrink dynamically.
 Memory does not need to be allocated in advance.
 Insertion and deletion can be performed without shifting other records.
 It provides a convenient way to represent a collection of records.
6 .Algorithm:
Write Algorithms for program/code which you have implemented.
7. Flowchart :
Draw flowchart for above algorithm.

8. Conclusion
The Student Record Management System demonstrates how a singly linked list can be used to
store and manage dynamic student records. The practical implements fundamental linked-list
operations such as insertion, deletion, searching, updating, traversal, and sorting, providing a
practical understanding of linked-list data structures.
'''

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

===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 3
Enter Roll No to update: 09
Current Name : Om Gaikwad
Current Marks: 85.0
Enter new name: Gaikwad Om
Enter new marks: 78
Student record updated successfully.

===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 4
Enter Roll No to search: 09

Student Found
Roll No : 9
Name : Gaikwad Om
Marks : 78.0

===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 5

-----------------------------------------
Roll No Name            Marks
-----------------------------------------
9        Gaikwad Om              78.0
-----------------------------------------

===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 6
1. Ascending
2. Descending
Enter choice: 7
Invalid choice.

-----------------------------------------
Roll No Name            Marks
-----------------------------------------
9        Gaikwad Om              78.0
-----------------------------------------

===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 2
Enter Roll No to delete: 09
Student deleted successfully.

===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add Student
2. Delete Student
3. Update Student
4. Search Student
5. Display Students
6. Sort by Marks
7. Sort by Roll Number
8. Exit
Enter your choice: 8
Program terminated.
'''
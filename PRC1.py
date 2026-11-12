print("Enter the no of members ")
no_mem = int(input())

borrow_mem = []

for i in range (no_mem):
    books = int(input("Enter the number of books borrowed "))
    borrow_mem.append(books)

t_borrowlist = sum(borrow_mem)
avg = t_borrowlist / no_mem
print("AVERAGE ",avg)

high = max(borrow_mem)
low = min(borrow_mem)
print("Highest borrow count = ",high)
print("Lowest borrow count = ",low)

no_borrow = borrow_mem.count(0)
print("Member who borrowed nothing = ",no_borrow)

count_dict = {}

for books in borrow_mem:
    if books in count_dict:
        count_dict[books] += 1
    else:
        count_dict[books] = 1

mode = borrow_mem[0]
high_count = count_dict[mode]

for books in count_dict:
    if count_dict[books] > high_count:
        high_count = count_dict[books]
        mode = books

print("Most frequent borrow count = ", mode)


'''
Enter the no of members 
5
Enter the number of books borrowed 74
Enter the number of books borrowed 56
Enter the number of books borrowed 21
Enter the number of books borrowed 11
Enter the number of books borrowed 74
AVERAGE 47.2
Highest borrow count =  74
Lowest borrow count =  11
Member who borrowed nothing =  0
Most frequent borrow count =  74



Practical No: 01(A)

Practical Title: Write a Python program to manage the borrowing records of books in a library..

Aim: - Write a Python program to manage the borrowing records of books in a library. Implement the following functionalities:
Compute the average number of books borrowed by all library members.
Find the book with the highest and lowest number of borrowings in the library.
Count the number of members who have not borrowed any books (denoted by a borrow count of 0).
Display the most frequently borrowed book (i.e., the mode of borrow counts).
After performing, determine the time and Space complexity of each operation

Prerequisite:
Python Programming

Objectives:
Compute the average number of books borrowed by all library members.
Identify the book with the highest and lowest number of borrowings.
Count how many members have not borrowed any books.
Find the most frequently borrowed book (mode).
Input: N number of books.

Outcome:
Able to manage and process tabular data.
Practice with basic statistics and control structures in Python.
Understand time and space complexity of data handling.

Theory:
ARRAYS
Arrays a kind of data structure that can store a fixed-size sequential collection of elements of th same type. An array is used to store a collection of data, but it is often more useful to think of a array as a collection of variables of the same type.
Instead of declaring individual variables, such as number0, numberl, ..., and number99, you decla one array variable such as numbers and use numbers[0], numbers[1], and numbers[99] represent individual variables. A specific element in an array is accessed by an index.
All arrays consist of contiguous memory locations. The lowest address corresponds to the fir element and the highest address to the last element.
Data Structure and Lab (DSL)
SE Computer Engineering
Declaring Arrays
To declare an array in C, a programmer specifies the type of the elements and the number of elements required by an array as follows -
type arrayName [ arraySize ];
पूज्य
This is called a ingle-dime array. The The arraySize must be an integer constant greater than zero and type can be any valid C data type. For example, to declare a 10-element array called balance of type double, use this statement -
double balance[10];

'''

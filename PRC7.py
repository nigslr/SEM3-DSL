SIZE = 10
table = [None] * SIZE

def hash_function(key):
    return key % SIZE

def insert(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            table[pos] = key
            print("Key inserted at index", pos)
            return

        if table[pos] == key:
            print("Key already exists")
            return

    print("Hash table is full")

def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] is None:
            print("Key not found")
            return

        if table[pos] == key:
            print("Key found at index", pos)
            return

    print("Key not found")

def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] == key:
            table[pos] = None
            print("Key deleted")
            return

    print("Key not found")

def display():
    print("\nHash Table")
    for i in range(SIZE):
        print(i, ":", table[i])

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")

'''
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 1
Enter key: 34
Key inserted at index 4

Practical No:6 (C)

Practical Title:

Aim: Design and implement a hash table of fixed size. Use the division method for the hash function and resolve 
collisions using linear probing. Allow the user to perform the following operations:
Insert a key
Search for a key
Delete a key
Display the table
पूज्यते!

Objective:
Use division method to create hash function
Implement collision handling using linear probing
Perform insertion, search, and display operations in a hash table

Input:
A list of integer keys to be inserted into the hash table

Theory:
Hashing maps keys to table indices using a hash function. 
Division method calculates index key size. Linear probing resolves collisions by checking subsequent slots 
until an empty one is found This method uses open addressing

Algorithm:
Insert(key):
1. Compute index = key % table_size
2. If slot at index is empty insert key
3. Else:
Probe next index (index + 1) % size
Repeat until empty slot is found or table is full
Search(key):
1. Compute index = key % table_size
2. While slot not empty:
If slot contains key return index
Else, move to next index using linear probing
3. If looped back to start, key not found
Display():
1. Traverse entire table
2. Print key at each index (or 'Empty' if slot is vacant)

'''

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

1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 4

Hash Table
0 : None
1 : None
2 : None
3 : None
4 : 34
5 : None
6 : None
7 : None
8 : None
9 : None

1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 5
Program ended
'''
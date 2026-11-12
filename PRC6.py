class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print("Key already exists. Value updated.")
                return

        self.table[index].append([key, value])
        print("Key-value pair inserted successfully.")
        print("Hash index:", index)

    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print("Key-value pair deleted successfully.")
                return

        print("Key not found.")

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])

ht = HashTable()

while True:
    print("\n--- HASH TABLE MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        ht.insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        value = ht.search(key)

        if value is not None:
            print("Value found:", value)
        else:
            print("Key not found.")

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == 4:
        ht.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")

'''
--- HASH TABLE MENU ---
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter your choice: 1
Enter key: 15
Enter value: Apple
Key-value pair inserted successfully.
Hash index: 5

--- HASH TABLE MENU ---
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter your choice: 1
Enter key: 11
Enter value: Samsung
Key-value pair inserted successfully.
Hash index: 1

--- HASH TABLE MENU ---
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter your choice: 2
Enter key to search: 11
Value found: Samsung

--- HASH TABLE MENU ---
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter your choice: 3
Enter key to delete: 15
Key-value pair deleted successfully.

--- HASH TABLE MENU ---
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter your choice: 4

Hash Table:
0 : []
1 : [[11, 'Samsung']]
2 : []
3 : []
4 : []
5 : []
6 : []
7 : []
8 : []
9 : []

--- HASH TABLE MENU ---
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter your choice: 5
Program terminated.
'''
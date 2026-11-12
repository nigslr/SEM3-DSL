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

Practical No:05(C)

Practical Title: Implementation of Hash Table using Division Method and Chaining

Aim:
Implement a hash table of size 10 and use the division method as a hash function. In case of a collision, use chaining. Implement the following operations:
Insert(key): Insert key-value pairs into the hash table.
Search(key): Search for the value associated with a given key.
Delete(key): Delete a key-value pair from the hash table
ते

Objective:
To implement a hash function using the division method
To handle collisions using linked list chaining
To perform insert, search, and display operations

Input: A list of key values (e.g., integers) to be inserted into the hash table
Outcome: Students will understand how hash tables manage data efficiently and how chaining handles hash collisions.

Theory:
Hash tables provide efficient data retrieval. A hash function maps keys to indices. 
The division method uses h(k) km to compute index. If collisions occur (same index for different keys), 
chaining uses a linked list to store multiple items at the same index.
A hash table is a data structure that maps keys to values, allowing for efficient insertion, deletion, 
and search operations. It achieves this by using a hash function to compute an index into an array where the corresponding value is stored.
This enables fast access to data, regardless of the table's size.

'''

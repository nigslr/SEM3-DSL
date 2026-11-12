print("Enter the no of Customer accounts")
n = int(input())
              
acc_ids = []
       
for i in range(n):
        acc = int(input("Enter Account id: "))
        acc_ids.append(acc)

search_id = int(input("Enter id to search: "))
acc_ids.sort()

# Linear Search
found = False

for i in range(len(acc_ids)):
    if acc_ids[i] == search_id:
        print("Implementing Linear Search.....")
        print("Customer id found at position ",i+1)
        found = True 
        break

if not found:
    print("Customer id not found")

# Binary Search
low = 0
high = len(acc_ids)-1
found = False

while low <= high:
    mid = (low+high)//2

    if acc_ids[mid] == search_id:
        print("Implementing Binary Search.....")
        print("Customer id found in sorted list")
        found = True
        break

    elif acc_ids[mid] < search_id:
        low = mid+1

    else:
        low = mid-1

if not found:
    print("Customer id not found inside the sorted list")

print("Sorted account ID's:")
print(acc_ids)

'''
Enter the no of Customer accounts
5
Enter Account id: 12
Enter Account id: 33
Enter Account id: 14
Enter Account id: 22
Enter Account id: 74
Enter id to search: 14
Implementing Linear Search.....
Customer id found at position  2



Practical No: 2(A)

Practical Title: Customer Account ID Search using Linear and Binary Search Technique

Aim: In an e-commerce system, customer account IDs are stored in a list, and you are tasked with writing a program that implements the following:
Linear Search: Check if a particular customer account ID exists in the list.
Binary Search: Implement Binary search to find if a customer account ID exists, improving the search efficiency over the basic linear

Objectives:
Implement Linear Search on a list
of customer IDs
Implement Binary Search on a sorted list of customer IDs
Analyze time complexity and efficiency

Input: A list of customer account IDs and a target account ID to be searched

Outcome:. Students will be able to understand and implement both Linear and Binary search algorithms, and analyze their performance.

Theory:
Linear Search:
Linear search, also known as sequential search, is a fundamental algorithm used to find a specific element within a list or array. It operates by sequentially checking each element in the collection, starting from the beginning, and comparing it to the target value
Time complexity: O(n)

Binary Search works on sorted lists by dividing the list in half and reducing the search space each time.
Binary search looks for a particular key value by comparing the middle most item of the collection. If a match occurs, then the index of item is returned. But if the middle item has a value greater than the key value, the right sub-array of the middle item is searched. Otherwise, the left sub-array is searched. This process continues recursively until the size of a subarray reduces to zero.
Time complexity: O(log n)
'''









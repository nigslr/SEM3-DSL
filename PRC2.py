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
'''









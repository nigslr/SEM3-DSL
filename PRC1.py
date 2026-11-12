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
'''
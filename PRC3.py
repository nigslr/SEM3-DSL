undo = []
redo = []

document =""

while True:
    print("Document Editor!")
    print("1. Make the change in document ")
    print("2. Undo ")
    print("3. Redo ")
    print("4. View the document ")
    print("5. Exit the Program ")

    print("Enter a choice: ")
    ch = int(input())

    if ch == 1:
        undo.append(document)
        print("Enter new text to add")
        change = input()
        document += change
        redo.clear()
        print("Change done Succesfully")

    elif ch == 2:
        if len(undo) == 0:
            print("Nothing to change")
            
        else:
            redo.append(document)
            document = undo.pop()
            print("Undo operation Sucessful")

    elif ch == 3:
        if len(redo) == 0:
                print("Nothing to change")
                
        else:
            undo.append(document)
            document = redo.pop()
            print("Redo operation Sucessful")
        
    elif ch == 4:
        print("Current Document: ")
        print(document)

    elif ch == 5:
        print("Exiting Program...")
        break 

    else:
        print("Invalid Choice chosen")

'''
Document Editor!
1. Make the change in document 
2. Undo 
3. Redo 
4. View the document 
5. Exit the Program 
Enter a choice: 
1
Enter new text to add
Hey, are you using python?
Change done Succesfully
Document Editor!
1. Make the change in document 
2. Undo 
3. Redo 
4. View the document 
5. Exit the Program 
Enter a choice: 
2
Undo operation Sucessful
Document Editor!
1. Make the change in document 
2. Undo 
3. Redo 
4. View the document 
5. Exit the Program 
Enter a choice: 
3
Redo operation Sucessful
Document Editor!
1. Make the change in document 
2. Undo 
3. Redo 
4. View the document 
5. Exit the Program 
Enter a choice: 
4
Current Document: 
Hey, are you using python?
Document Editor!
1. Make the change in document 
2. Undo 
3. Redo 
4. View the document 
5. Exit the Program 
Enter a choice: 
5
Exiting Program...
'''
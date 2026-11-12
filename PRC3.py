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

Practical No. 3(B)

Practical Title: Implementing Undo and Redo Functionality in a Text Editor using Stack

Aim: Implementing a real-time undo/redo system for a text editing application using a Stack data structure. The system should support the following operations:
Make a Change: A new change to the document is made.
Undo Action: Revert the most recent change and store it for potential redo.
Redo Action: Reapply the most recently undone action.
Display Document State: Show the current state of the document after undoing or redoing an action

Objectives:
Implement stack-based undo and redo features
Track changes to document text
Understand stack push and pop operations through practical usage

Input: A sequence of user actions like "add text", "undo", and "redo"

Outcome: Students will be able to manage document state changes and understand stack-based state tracking.

Theory:
A stack is a fundamental data structure in computer science that operates on the last-in, first-out (LIFO) principle. 
Imagine a stack of plates: you can only add or remove plates from the top. 
This means the most recently added item is the first one to be removed 
The LIFO property is used for undo/redo by pushing changes to the undo stack and
popping them for redo actions. Two stacks are used: one for undo and anoth for redo.
C
Push
Pop
C
B
Top
C
A
Top
Stack Data Structure
'''

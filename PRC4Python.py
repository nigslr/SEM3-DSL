# Python Program

MAX = 10
queue = []

def add_event():
    if len(queue) == MAX:
        print("Queue is full! Cannot add event.")
        return
    event = input("Enter event name: ")
    queue.append(event)
    print("Event added successfully.")

def process_event():
    if len(queue) == 0:
        print("No pending events.")
        return
    event = queue.pop(0)
    print("Processing event:", event)

def display_events():
    if len(queue) == 0:
        print("No pending events.")
        return
    print("\nPending Events:")
    for i, event in enumerate(queue, 1):
        print(i, ".", event)

def cancel_event():
    if len(queue) == 0:
        print("No pending events.")
        return
    event = input("Enter event name to cancel: ")
    if event in queue:
        queue.remove(event)
        print("Event cancelled successfully.")
    else:
        print("Event not found.")

while True:
    print("\n===== EVENT PROCESSING SYSTEM =====")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_event()
    elif choice == 2:
        process_event()
    elif choice == 3:
        display_events()
    elif choice == 4:
        cancel_event()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

'''
===== EVENT PROCESSING SYSTEM =====
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 1
Enter event name: Hack-A-Night
Event added successfully.

===== EVENT PROCESSING SYSTEM =====
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 2
Processing event: Hack-A-Night

===== EVENT PROCESSING SYSTEM =====
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 3
No pending events.

===== EVENT PROCESSING SYSTEM =====
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 4
No pending events.

===== EVENT PROCESSING SYSTEM =====
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel an Event
5. Exit
Enter your choice: 5
Exiting...
'''
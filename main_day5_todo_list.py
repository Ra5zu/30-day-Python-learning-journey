
day = 1

score = 0
while True:
    print("TODO LIST")
    print(f"DAY {day}")
    print("MENU:\n Press the key for the function\n1.View list\n2.Add item\n3.Remove item\n4.Reset list"
          "\n5.Tick off the item\n6.End the day")
    todo_list = []

    while True:
        pos = 1
        a = int(input())
        if a == 1:
            print(todo_list)
        elif a == 2:
            todo_list.append(f"{pos}.{input('Input the item to the list:')}")

            pos +=1
        elif a == 3:
            p = int(input("Input the index of the task to remove:"))
            todo_list.pop(p-1)
            pos -=1
        elif a == 4:
            todo_list = []
        elif a == 5:
            p = int(input("Input the index of the task to tick off:"))
            todo_list.pop(p - 1)
            score +=1
            pos -=1
        elif a == 6:
            print(f"Congratulations! You have ended the day {day}. Get back to grind tomorrow.")
            print(f"Score for today is {score} total tasks done")
            break
        else:
            print("Invalid input. Try again with numbers 1-6")

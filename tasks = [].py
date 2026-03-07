tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print (f"Task '{task}' added to the list!")

def listTasks():
    if not tasks:
        ("There are currently no tasks.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else: 
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input. Please input the # to delete.")



if __name__ == "__main__":
    print("Welcome to Notebook! The all-in-one productivity app. You are in the To-Do List!")
 
    while True:   
        print("\n")
        print("Please select one of these options:")
        print("-----------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            addTask()

        elif (choice == "2"):
            deleteTask()

        elif (choice =="3"):
            listTasks()

        elif (choice == "4"):
            break
        else:
            print("Error! Invalid Input!")
            print("Please try again.") 
        
        print("Goodbye!")
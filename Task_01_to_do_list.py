from tabulate import tabulate

tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' successfully added!!")

def deleteTask():
    listTask()
    try:
        if not tasks:
            print("\nNothing to delete...")
        else:
            task_number = int(input("Enter the task number you want to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' successfully deleted from the list!!")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def listTask(): 
    if not tasks:
        print("\nNo pending tasks in the list!!")
    else:
        table = [[i + 1, task] for i, task in enumerate(tasks)]
        print("\nPending Tasks:\n")
        print(tabulate(table, headers=["Task Number", "Task"], tablefmt="pretty"))

def updateTask():
    listTask()
    try:
        if not tasks:
            print("\nNothing to update...")
        else:
            task_number = int(input("Enter the task number you want to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter a new task: ")
                tasks[task_number - 1] = new_task
                print(f"Task '{task_number}' successfully updated!!")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

if __name__ == "__main__":
    print("\n--------------To Do List Application--------------")
    while True:
        print("\nSelect any operation you want to perform:")
        print("1. Add A New Task")
        print("2. Update Task")
        print("3. Delete A Task")
        print("4. List All The Tasks")
        print("5. Quit To Do List Application")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                addTask()
            elif choice == 2:
                updateTask()
            elif choice == 3:
                deleteTask()
            elif choice == 4:
                listTask()
            elif choice == 5:
                print("Quitting To Do List Application....")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")


def add_task():
    try:
        new_task = str(input("Please enter the new task: "))
        task_status = "Incomplete"
        ToDoList.append(new_task + ": " + task_status)
        print(f"'{new_task}' has been added to the To-Do List.")
    except TypeError:
        print("Invalid input. Please try again")

def view_tasks():
    if not ToDoList:
        print("There are currently no tasks.")
    else:
        print(f"To-Do List: \n{ToDoList}")

def mark_task_complete():
    task_to_complete = input("Which task has been completed? ")
    for task in ToDoList:
        if task_to_complete in task:
            task_completed = task.replace("Incomplete", "Completed")
            index = ToDoList.index(task)
            ToDoList[index] = task_completed
            print(f"Task '{task_to_complete}' has been completed.")
        else:
            print(f"Task '{task_to_complete}' not found in list.")


def delete_task():
    try:
        del_task = input("Which task would you like to delete? ")
        ToDoList.remove(del_task)
        print(f"'{del_task}' has been removed from the To-Do List.")
    except:
        print("Task not found. Please try again.")


ToDoList = []

while True:
    try:
        print("\nWelcome to the To-Do List App!", "\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        choice = input("Select an option: (1-5) ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid input. Please try again.")     
    except ValueError:
        print("Invalid number. Please choose agian.")



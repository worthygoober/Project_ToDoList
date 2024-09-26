ToDoList = []

def add_task():
    try:
        new_task = str(input("Please enter the new task: "))
        ToDoList.append(new_task)
        print(f"'{new_task}' has been added to the To-Do List.")
    except TypeError:
        print("Invalid input. Please try again")

def view_tasks():
    if not ToDoList:
        print("There are currently no tasks.")
    else:
        print(f"To-Do List: \n{ToDoList}")

def mark_task_complete():
    pass

def delete_task():
    try:
        del_task = input("Which task would you like to delete? ")
        ToDoList.remove(del_task)
        print(f"'{del_task}' has been removed from the To-Do List.")
    except:
        print("Task not found. Please try again.")


def main():
    while True:
        print("\nWelcome to the To-Do List App!", "\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        choice = input("Select an option: (1-5) ")

        try:
            if choice == "1":
                add_task()
                
            
            elif choice == "2":
                view_tasks()
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                delete_task()
                pass
            elif choice == "5":
                print("Thank you for using the To-Do List App!")
                break
            else:
                print("Invalid input. Please try again.")     
        except ValueError:
            print("Invalid number. Please choose agian.")


main()

# Simple To-Do List Application for CodSoft Internship

def show_options():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Update a Task")
    print("4. Remove a Task")
    print("5. Exit")

def run_todo():
    tasks_list = []
    
    while True:
        show_options()
        user_choice = input("\nSelect an option (1-5): ")

        # 1. Adding a Task
        if user_choice == '1':
            new_task = input("Enter the task description: ")
            tasks_list.append(new_task)
            print("Task added successfully!")

        # 2. Displaying Tasks
        elif user_choice == '2':
            if not tasks_list:
                print("\nYour list is currently empty.")
            else:
                print("\nYour Pending Tasks:")
                for i, t in enumerate(tasks_list, 1):
                    print(f"{i}. {t}")

        # 3. Updating a Task
        elif user_choice == '3':
            if not tasks_list:
                print("Nothing to update.")
            else:
                try:
                    task_no = int(input("Enter the task number to edit: "))
                    if 1 <= task_no <= len(tasks_list):
                        updated_text = input("Enter the new task: ")
                        tasks_list[task_no - 1] = updated_text
                        print("Updated successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        # 4. Deleting a Task
        elif user_choice == '4':
            if not tasks_list:
                print("Nothing to delete.")
            else:
                try:
                    task_no = int(input("Enter the task number to remove: "))
                    if 1 <= task_no <= len(tasks_list):
                        removed_item = tasks_list.pop(task_no - 1)
                        print(f"Task '{removed_item}' removed.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a number.")

        # 5. Exit
        elif user_choice == '5':
            print("Closing the application. Goodbye!")
            break
        
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    run_todo()

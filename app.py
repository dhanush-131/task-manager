def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    with open("tasks.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    print("1. Add Task\n2. View Tasks")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
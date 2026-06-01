def add_task(task):
    print()
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    with open("tasks.txt", "r") as f:
        print(f.read())
def delete_task(index):
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    if 0 <= index < len(tasks):
        tasks.pop(index)

    with open("tasks.txt", "w") as f:
        f.writelines(tasks)

if __name__ == "__main__":
    choice="0"
    while choice!="3":
        choice = input("Enter choice: ")
        print("1. Add Task\n2. View Tasks\n3. Delete\n4. Exit")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter task index: "))
            delete_task(index)
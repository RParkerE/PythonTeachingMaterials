from task import Task
from file_manager import FileManager

def validate_choice(choice):
    if int(choice) < 1 or int(choice) > 3:
        return False
    return True

def validate_difficulty(difficulty):
    if int(difficulty) < 1 or int(difficulty) > 5:
        return False
    return True


def main():
    tasks = []

    file_manger = FileManager("tasks.csv")
    items = file_manger.load_tasks()
    for item in items:
        tasks.append(item)

    while True:
        choice = input("""What do you want to do?
        1. Add a task
        2. View all taks
        3. Complete a task
        """)
        if validate_choice(choice):
            if choice == "1":
                name = input("What is the task name? ").rstrip()
                difficulty = input("What is the task difficulty? ")
                if validate_difficulty(difficulty):
                    task = Task(name, difficulty)
                    tasks.append(task)
                    file_manger.save_tasks(task)

            elif choice == "2":
                items = file_manger.load_tasks()
                for item in items:
                    print(item)

            elif choice == "3":
                name = input("What is the name of the task you completed? ")
                for task in tasks:
                    if task.name == name:
                        task.status = "done"
        else:
            print("That is not a valid choice.")

main()

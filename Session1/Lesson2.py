from random import randint

# Get task input from user
def get_task():
    task_name = input("Enter the task name: ").rstrip()
    return task_name

# Validate difficulty
def validate_difficulty():
    try:
        difficulty = input("Enter the difficulty (1-5): ")
        difficulty = int(difficulty)
        if 1 <= difficulty <= 5:
            return difficulty
        else:
            print("Invalid difficulty. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid difficulty. Please enter a number between 1 and 5.")

# Calculate a simple score
def calculate_score(task_name, difficulty):
    return len(task_name) * int(difficulty)

# Main Loop
def main():
    while True:
        task_name = get_task()
        difficulty = validate_difficulty()
        score = calculate_score(task_name, difficulty)
        print(f"Task: {task_name.upper()}")
        print(f"Score: {score}")
        print(f"Motivation Bonus: {randint(1, 10)}")

main()
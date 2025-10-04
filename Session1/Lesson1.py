# Get task input from user
task_name = input("Enter the task name: ")
difficulty = input("Enter the difficulty (1-5): ")

# Clean up task name
task_name = task_name.strip()

# Calculate a simple score
score = len(task_name) * int(difficulty)

# Display result
print(f"Task: {task_name.upper()}")
print(f"Score: {score}")

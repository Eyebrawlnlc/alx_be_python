task = input("Enter the task description: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

if priority.lower() == "high":
    print(f"Task '{task}' is a high priority task.")
elif priority.lower() == "medium":
    print(f"Task '{task}' is a medium priority task.")
elif priority.lower() == "low":
    print(f"Task '{task}' is a low priority task.")
if time.lower() == "yes":
    print(f"Task '{task}' is time-bound.")
else:
    print(f"Task '{task}' is not time-bound.")
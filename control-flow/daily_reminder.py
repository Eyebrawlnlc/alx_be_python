# daily_reminder.py

# Prompt the user for task input
task = input("Enter your task: ").strip()

# Loop to ensure valid priority input
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ("high", "medium", "low"):
        break
    else:
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Print customized reminder using match-case (Python 3.10+)
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"

# Modify message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Output the reminder
print("\n" + message)

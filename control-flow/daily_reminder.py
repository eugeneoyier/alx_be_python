# daily_reminder.py
# A script to provide a customized reminder for a single task based on priority and time sensitivity

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"'{task}' is a {priority} priority task"

# Use Match Case to append priority-specific info (optional for extra behavior)
match priority:
    case "high":
        reminder += ""
    case "medium":
        reminder += ""
    case "low":
        reminder += ""
    case _:
        reminder += " (priority not recognized)"

# Adjust message based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Display the final reminder
print("Reminder:", reminder)

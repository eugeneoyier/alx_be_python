# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""

match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
    case 'medium':
        reminder_message = f"'{task}' is a medium priority task"
    case 'low':
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = f"'{task}' has an unrecognized priority"

if time_bound == 'yes':
    reminder_message += " that requires immediate attention today!"
else:
    if priority == 'low':
        reminder_message += ". Consider completing it when you have free time."
    else:
        reminder_message += ". Try to complete it today." # Default for non-time-bound medium/high tasks

print(f"Reminder: {reminder_message}")

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("  🚀 Click here to tweet! 🚀")
# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Reminder message
reminder = f"Reminder: '{task}' is a "

# Determine priority using Match Case
match priority:
  case "high":
    reminder += "high priority task"
  case "medium":
    reminder += "medium priority task"
  case "low":
    reminder += "low priority task"
  case _:
    reminder = "Invalid priority. Please enter high, medium, or low."

# Add time sensitivity if applicable
if time_bound == "yes":
  reminder += " that requires immediate attention today!"
else:
  reminder += ". Consider completing it when you have free time."

# Print the reminder
print(reminder)

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Ensure positive input
while size <= 0:
  print("Please enter a positive integer.")
  size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 1
while row <= size:
  # Print asterisks in a row
  for col in range(1, size + 1):
    print("*", end="")
  # Move to the next line
  print()
  row += 1

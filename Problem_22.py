# Project Euler Problem 22 - Names Scores

# Open the file containing names
with open("names.txt", "r") as file:
    names = file.read()

# Remove quotes and split names into a list
names_list = names.replace('"', '').split(',')

# Sort names alphabetically
names_list.sort()

# Function to calculate alphabetical value of a name
def name_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

# Calculate total score
total_score = 0

for index, name in enumerate(names_list, start=1):
    score = index * name_value(name)
    total_score += score

# Print final answer
print("Total Name Scores:", total_score)
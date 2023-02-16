import random

# Lists of names
first_names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte", "Elijah", "Mia", "Lucas", "Amelia", "Mason", "Harper", "Logan", "Evelyn", "Alexander", "Abigail", "Ethan", "Emily", "Jacob", "Elizabeth", "Michael", "Mila", "Daniel", "Ella", "Henry", "Avery", "Jackson", "Sofia", "Sebastian", "Camila", "Aiden", "Scarlett", "Matthew", "Victoria", "Samuel", "Luna", "Joseph", "Grace", "David", "Chloe", "Carter", "Penelope"]

last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris"]

# Generating a random name
def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

# Generating multiple names
def generate_names(num_names):
    names = []
    for i in range(num_names):
        names.append(generate_name())
    return names

# Usage example
print(generate_name())
print(generate_names(5))

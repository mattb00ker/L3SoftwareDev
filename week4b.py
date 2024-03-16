# Function to get validated integer input (e.g., age)
def get_int_input(prompt):
    while True:
        print(prompt)
        try:
            value = int(input())
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Function to get boolean input (e.g., likes swimming)
def get_boolean_input(prompt):
    while True:
        print(prompt + " (True/False)")
        input_str = input().strip().lower()
        if input_str in ['true', 'false']:
            return input_str == 'true'
        else:
            print("Invalid input. Please enter 'True' or 'False'.")

print("Welcome to the Ultimate Fitness Gym Membership Registration!")

# Collecting user information
name = input("What is your full name? ")

age = get_int_input("What is your age? ")

# Fitness goals
print("What are your fitness goals? Choose one: [Weight Loss, Muscle Gain, General Fitness]")
fitness_goal = input()

# Preferences
likes_swimming = get_boolean_input("Do you like swimming?")
requires_personal_trainer = get_boolean_input("Do you require a personal trainer?")

# Calculating membership cost (example calculation, can be more complex based on real scenarios)
base_cost = 30
if age > 60:
    discount = 10  # 10% discount for seniors
else:
    discount = 0

if likes_swimming:
    base_cost += 10  # Additional cost for swimming pool access

if requires_personal_trainer:
    base_cost += 20  # Additional cost for personal training services

final_cost = base_cost - (base_cost * discount / 100)

# Output
print(f"\nRegistration Summary for {name}:")
print(f"Age: {age}")
print(f"Fitness Goal: {fitness_goal}")
print(f"Swimming Pool Access: {'Yes' if likes_swimming else 'No'}")
print(f"Personal Trainer Required: {'Yes' if requires_personal_trainer else 'No'}")
print(f"Monthly Membership Cost: ${final_cost:.2f}")

print("\nThank you for registering with Ultimate Fitness Gym! We look forward to supporting you on your fitness journey.")

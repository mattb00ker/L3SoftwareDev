print("What is your first name?")
first_name = input()
print("What is your surname")
surname = input()
#print("What is your age?")
#age = int(input())
print("What is your age?")
try:
    age = float(input())
except ValueError:
    print("You must enter a number")
    age = float(input())
print("True or False - you like marmite")
likes_marmite = input()
marmite = "True"
decades = int((age / 10))
print(f"Well hello {initial} {surname}.")
print(f"It is {likes_marmite==marmite} that you like marmite.")
print(f"This is probably because you are {decades} decades old")

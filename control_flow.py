# pseudocode - refined user story

# - if it's cold:
#   - take jacket
# - if it's raining:
#   - rain mack
# - if it's sunny: true = next line, false = go to else
#   - let's go to beach
# - else
#   - stay inside

# weather = "sunny"

# if weather == "cold":
#     print("Wear a jacket.")
# elif weather == "sunny":
#     print("Let's go to the beach")
# elif weather == "raining":
#     print("Bring an umbrella")
# else:
#     print("No match found")

# Options task
age = int(input("Please enter you age: "))

while True:
    if age > 117:
        print("Please re-enter your age, ages above 117 not allowed: ")
        break
    elif age >= 18:
        print("You are allowed to view movies for up to 18 and above")
        break
    elif age >= 16:
        print("You are allowed to view movies for up to 16 and below")
        break
    elif age >= 15:
        print("You are allowed to view movies for up to 15 and below")
        break
    elif age >= 12:
        print("You are allowed to view movies for up to 12 and below")
        break
    elif age >= 8:
        print("You are allowed to view movies for up to 8 and below")
        break
    else:
        age = int(input("please re-enter your age, no matches found: "))


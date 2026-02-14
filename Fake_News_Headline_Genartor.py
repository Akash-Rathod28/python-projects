# step1 --- import random module
import random

# create subjects
subjects = [
    "shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Bangalore Cat",
    "A Group Of Monkeys",
    "Prime Minister Modi",
    "Auto Rikshaw Driver from abudabi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "cats",
    "Declares war on",
    "Orders",
    "Celebrates"
]

places_of_things =[
    " at red fort",
    "in bangalore local train",
    "a plote of samosa",
    "inside parliment",
    "during IPL match",
    "talking with a cow",
    "dancing with a cow",
]

# step3 ---> start the headline genartion loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_of_thing = random.choice(places_of_things)

    headline = f"BREAKING NEWS : {subject} {action} {place_of_thing}"
    print("\n" + headline)

    User_input = input("\nDo you want another headline? (YES/NO)").strip().lower()
    if User_input == "no":
        break

#print goodbye message
print("\nThanks for using the Fake News Headline Generator.have a fun day")

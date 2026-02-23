print("Welcome To computer Quiz game: ")

playing = input("Do you want to play? ")
if playing != 'yes'.lower():
    quit() # stops the program execution
print("Okay Lets play :) ")

answer = input("Waht does CPU stands for?")
if answer == "central processing unit".lower():
    print("Correct!")
else:
    print("Incorect! ")

answer = input("Who wrote constitutional assembly?")
if answer == "dr br ambedkar".lower():
    print("Correct!")
else:
    print("Incorect! ")

answer = input("Waht does GPU stands for?")
if answer == "graphic processing unit".lower():
    print("Correct!")
else:
    print("Incorect! ")

answer = input("Waht does RAM stands for?")
if answer == "random access memory".lower():
    print("Correct!")
else:
    print("Incorect! ")

print("Welcome To computer Quiz game: ")

playing = input("Do you want to play? ")
if playing != 'yes'.lower():
    quit() # stops the program execution
print("Okay Lets play :) ")
score = 0

answer = input("Waht does CPU stands for?")
if answer == "central processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorect! ")

answer = input("Who wrote constitutional assembly?")
if answer == "dr br ambedkar".lower():
    print("Correct!")
    score += 1
else:
    print("Incorect! ")

answer = input("Waht does GPU stands for?")
if answer == "graphic processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorect! ")

answer = input("Waht does RAM stands for?")
if answer == "random access memory".lower():
    print("Correct!")
    score += 1
else:
    print("Incorect! ")

print("You got" + str(score) + " questions correct!")
print("You got" + str((score/4) * 100) + "%.")


chance = 3
rainbow = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}
count = 0

for i in range(3) :
    color = input("enter color of rainbow: ")
    if color in rainbow : 
        print("Correct!!")
        break
    else : 
        if i == 2 : print("You lost")
        else : print("try again")


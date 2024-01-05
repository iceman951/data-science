
quiz = 10
answer = input("5+5=? ")

while True :
    if float(answer) == quiz : 
        print("correct!!")
        break
    else : 
        print("try again!!")
        answer = input("5+5=? ")

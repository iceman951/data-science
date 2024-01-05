sum = 0
while True:
    number = input("exit input 'q', enter number: ")
    if number == "q" : break
    elif number.isdigit() : sum += float(number)
    else : print("input just digit")

print("sum is ", sum)
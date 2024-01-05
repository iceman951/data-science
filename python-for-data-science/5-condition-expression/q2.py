# Q2: input a number (digit)
# if it is digit then show "It is number"
# if number is not digit then show "It is not number"

text = input("input a number: ")

if text.isdigit() :
    print("It is number")
else :
    print("It is not number")
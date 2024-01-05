# Q5: Butcher sell pork btw 1-7 kilograms, 40 BaTH/kg

weight = float(input("how much kilo what u want to buy: "))

min = 1
max = 7

if weight < min :
    print(weight ,"kg ,minimum is 1 kilogram")
elif weight > max :
    print(weight ,"kg ,maximum is 7 kilograms ")
else :
    total = weight * 40
    print("total price is ", total)
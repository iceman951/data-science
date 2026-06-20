# problem 2 จงเขียนสคริปต์เพื่อถามเงินต้น (principle) และ อัตราดอกเบี้ย (interest rate) แบบร้อยละจากผู้ใช้ แล้วให้ แสดงข้อความบนจอภาพว่าเมื่อฝากเงินครบ 1 ปี ผู้ใช้จะมียอดเงินฝาก (balance) เท่าใด
principle = float(input("Enter your principle: "))
interest_rate = float(input("Enter your interest rate: "))
balance = principle*(1+interest_rate/100)
print(f"Your balance after 1 year is {(balance):.2f} Baht.")
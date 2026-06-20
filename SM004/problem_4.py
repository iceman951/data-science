# problem 4 จงเขียนสคริปต์เพื่อถามเพศจากผู้ใช้ (M/F) ถ้าผู้ใช้เลือก M ให้แสดงข้อความว่า “You are a male.” แต่ถ้าผู้ใช้เลือก F ให้แสดงข้อความว่า “You are a female.”
gender = input("Enter your gender (M/F): ")
if gender == "M":
    print("You are a male.")
elif gender == "F":
    print("You are a female.")

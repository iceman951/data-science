# problem 1 จงเขียนสคริปต์เพื่อถามปีเกิด (birth year) จากผู้ใช้ เมื่อผู้ใช้ป้อนคําตอบและเคาะ enter แล้วให้แสดงข้อความแจ้งอายุของผู้ใช้บนจอภาพ 
birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)
print(f"You are {age} years old.")
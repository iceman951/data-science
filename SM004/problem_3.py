# problem 3 จงเขียนสคริปต์เพื่อตัดเกรด โดยรับค่าคะแนน (score) จากผู้ใช้ แล้วทําการตัดเกรดดังตารางตัวอย่างไปนี้แล้วแสดงเกรด (grade) ของผู้ใช้บนจอภาพ
#################
# score # grade #
#################
# 80-100 # A    #
# 70-79  # B    #
# 60-69  # C    #
# 50-59  # D    #
# 0-49   # F    #
#################
grade = ""
score = float(input("Enter your score: "))
if score > 100 or score < 0:
  grade = "Invalid score"

if score >= 80 and score <= 100:
  grade = "A"
elif score >= 70 and score < 80:
  grade = "B"
elif score >= 60 and score < 70:
  grade = "C"
elif score >= 50 and score < 60:
  grade = "D"
elif score >= 0 and score < 50:
  grade = "F"
print(f"Your grade is {grade}")
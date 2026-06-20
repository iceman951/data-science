# problem 5 จงเขียนสคริปต์เพื่อถามจํานวนชั่วโมงทํางานต่อสัปดาหกก์จากผู้ใช้ จากนั้นคํานวณค่าแรง โดยกําหนดค่าแรงปกติ ชั่วโมงละ 30 บาท แต่หากทํางานเกินกว่า 40 ชั่วโมงต่อสัปดาห์ ชั่วโมงที่เกินจะคิดค่าแรงด้วยอัตราของค่าล่วงเวลาชั่วโมงละ 50 บาท จากนั้นแสดงจํานวนค่าแรงรวมบนจอภาพ
hour = int(input("Enter your working hour: "))
ot_hour = 0
if hour > 40:
    ot_hour = hour - 40
    hour = 40
wage = (hour * 30) + (ot_hour * 50)
print(f"You work {hour} hours and {ot_hour} overtime hours.")
print(f"Your wage is {wage} Baht.")
//  problem 1 จงเขียนสคริปต์เพื่อถามปีเกิด (birth year) จากผู้ใช้ เมื่อผู้ใช้ป้อนคําตอบและเคาะ enter แล้วให้แสดงข้อความแจ้งอายุของผู้ใช้บนจอภาพ
use std::io;

fn main() {
  let mut birth_year = String::new();
  println!("Enter your birth year: ");
  io::stdin().read_line(&mut birth_year).expect("Failed to read line");
  let current_year = 2026;
  println!("You are {} years old.", current_year - birth_year.trim().parse::<i32>().expect("Please type a number!"));
}

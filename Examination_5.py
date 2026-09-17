# ==========================================
# โจทย์ข้อที่ 5: ประเมินค่าดัชนีมวลกาย (BMI)
# Input: ค่า BMI (จำนวนจริง)
# Output: "Underweight", "Normal", หรือ "Overweight"
# เงื่อนไข: น้อยกว่า 18.5 พิมพ์ "Underweight" | 18.5 ถึง 22.9 พิมพ์ "Normal" | ตั้งแต่ 23 ขึ้นไป พิมพ์ "Overweight"
# ==========================================


# นักเรียนเขียนโค้ดต่อจากบรรทัดนี้
bmi = float(input("ค่า BMI"))
if bmi < 18.5 :
    print("Underweight")
elif bmi <= 22.9 :
    print("Normal")
else :
    print("Overweight")

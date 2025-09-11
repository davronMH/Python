rom datetime import datetime, timedelta
import re
import pytz  # pip install pytz

# 1. Age Calculator
def age_calculator():
    birthdate_str = input("Tug‘ilgan kuningizni kiriting (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (today - timedelta(days=today.day)).day
    if months < 0:
        years -= 1
        months += 12

    print(f"Siz {years} yil, {months} oy, {days} kun yoshsiz.")

# 2. Days Until Next Birthday
def days_until_birthday():
    birthdate_str = input("Tug‘ilgan kuningizni kiriting (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    next_birthday = birthdate.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_remaining = (next_birthday - today).days
    print(f"Keyingi tug‘ilgan kuningizgacha {days_remaining} kun qoldi.")

# 3. Meeting Scheduler
def meeting_scheduler():
    current_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    hours = int(input("Uchrashuv davomiyligi (soat): "))
    minutes = int(input("Uchrashuv davomiyligi (minut): "))

    current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_dt = current_dt + timedelta(hours=hours, minutes=minutes)

    print("Uchrashuv tugash vaqti:", end_dt.strftime("%Y-%m-%d %H:%M"))

# 4. Timezone Converter
def timezone_converter():
    dt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    from_tz = input("Joriy timezone (masalan, Asia/Tashkent): ")
    to_tz = input("O‘tkaziladigan timezone: ")

    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    local_dt = from_zone.localize(dt)
    converted_dt = local_dt.astimezone(to_zone)

    print("Natija:", converted_dt.strftime("%Y-%m-%d %H:%M"))

# 5. Countdown Timer
import time
def countdown_timer():
    future_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
    future = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        if now >= future:
            print("Vaqt tugadi!")
            break
        remaining = future - now
        print("Qolgan vaqt:", remaining, end="\r")
        time.sleep(1)

# 6. Email Validator
def email_validator():
    email = input("Email kiriting: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Email manzil yaroqli ✅")
    else:
        print("Email manzil yaroqsiz ❌")

# 7. Phone Number Formatter
def phone_formatter():
    num = input("Telefon raqam kiriting (faqat raqamlar, masalan 1234567890): ")
    if len(num) == 10 and num.isdigit():
        formatted = f"({num[:3]}) {num[3:6]}-{num[6:]}"
        print("Formatlangan raqam:", formatted)
    else:
        print("Noto‘g‘ri raqam!")

# 8. Password Strength Checker
def password_checker():
    pwd = input("Parol kiriting: ")
    if (len(pwd) >= 8 and
        any(c.isupper() for c in pwd) and
        any(c.islower() for c in pwd) and
        any(c.isdigit() for c in pwd)):
        print("Parol kuchli ✅")
    else:
        print("Parol kuchsiz ❌")

# 9. Word Finder
def word_finder():
    text = "Python is great. Python is easy. I love Python."
    word = input("Qidiriladigan so‘zni kiriting: ")
    occurrences = [m.start() for m in re.finditer(word, text)]
    print(f"So‘z '{word}' {len(occurrences)} marta topildi. Pozitsiyalar: {occurrences}")

# 10. Date Extractor
def date_extractor():
    text = input("Matn kiriting: ")
    pattern = r'\d{4}-\d{2}-\d{2}'
    dates = re.findall(pattern, text)
    if dates:
        print("Topilgan sanalar:", dates)
    else:
        print("Sana topilmadi.")

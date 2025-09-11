#ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    result = num/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
  #ValueError
try:
    num = int(input("Enter an integer:"))
    print(f'You entered {num}')
except ValueError:
    print('Error:That is not valid integer')
# 3. FileNotFoundError
try:
    with open("nofile.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: Fayl topilmadi!")

# 4. TypeError (faqat sonlar bo‘lishi kerak)
try:
    a = input("Birinchi son: ")
    b = input("Ikkinchi son: ")
    a, b = float(a), float(b)
    print("Natija:", a + b)
except ValueError:
    raise TypeError("Faqat raqam kiriting!")
# 5. PermissionError
try:
    with open("/salom.txt", "w") as f:
        f.write("Hello")
except PermissionError:
    print("Error:")
# 6. IndexError
nums = [1,2,3]
try:
    print(nums[5])
except IndexError:
    print("Error: Indeks diapazondan tashqarida!")


# 7. KeyboardInterrupt
try:
    n = input("Son kiriting (Ctrl+C bosib ko‘ring): ")
except KeyboardInterrupt:
    print("\nError: Foydalanuvchi kiritishni bekor qildi.")
# 8. ArithmeticError
try:
    x = 1/0
except ArithmeticError:
    print("Error: Arifmetik xato yuz berdi!")

# 9. UnicodeDecodeError
try:
    with open("test.txt", encoding="ascii") as f:
        data = f.read()
except UnicodeDecodeError:
    print("Error: Faylni kodlashda muammo!")
# 10. AttributeError
nums = [1,2,3]
try:
    nums.push(4)   # listda push() yo‘q
except AttributeError:
    print("Error: Bu obyekt uchun bunday atribut mavjud emas!")

# 1. Read entire text file
with open("sample.txt", "r") as f:
    print(f.read())

# 2. Read first n lines
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline().strip())

# 3. Append text to file and display it
with open("sample.txt", "a") as f:
    f.write("\nThis is appended text.")
with open("sample.txt", "r") as f:
    print(f.read())

# 4. Read last n lines
n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# 5. Read line by line into list
with open("sample.txt", "r") as f:
    lines_list = f.readlines()
print(lines_list)

# 6. Read line by line into variable
with open("sample.txt", "r") as f:
    text_data = f.read()
print(text_data)

# 7. Read line by line into array (same as list in Python)
with open("sample.txt", "r") as f:
    arr = [line.strip() for line in f]
print(arr)

# 8. Find longest words
with open("sample.txt", "r") as f:
    words = f.read().split()
    max_len = max(len(w) for w in words)
    longest = [w for w in words if len(w) == max_len]
print("Longest words:", longest)

# 9. Count number of lines
with open("sample.txt", "r") as f:
    line_count = sum(1 for _ in f)
print("Line count:", line_count)

# 10. Count word frequency
from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)

# 11. Get file size
import os
print("File size:", os.path.getsize("sample.txt"), "bytes")

# 12. Write a list to file
mylist = ["Apple", "Banana", "Cherry"]
with open("list.txt", "w") as f:
    for item in mylist:
        f.write(item + "\n")

# 13. Copy file contents
with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())

# 14. Combine each line from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

# 15. Read a random line from file
import random
with open("sample.txt") as f:
    lines = f.readlines()
    print(random.choice(lines).strip())

# 16. Assess if file is closed
f = open("sample.txt", "r")
print("Closed?", f.closed)
f.close()
print("Closed?", f.closed)

# 17. Remove newline characters
with open("sample.txt") as f:
    cleaned = [line.strip() for line in f]
print(cleaned)

# 18. Count words in a file
with open("sample.txt") as f:
    text = f.read().replace(",", " ")
    word_count = len(text.split())
print("Word count:", word_count)

# 19. Extract characters into list
chars = []
for filename in ["file1.txt", "file2.txt"]:
    with open(filename) as f:
        chars.extend(list(f.read()))
print(chars)

# 20. Generate 26 text files A.txt ... Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")

# 21. Create alphabet file with n letters per line
n = 5
alphabet = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), n):
        f.write(alphabet[i:i+n] + "\n")

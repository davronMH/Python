#1.Age Calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

a=(input("Ismingizni kiriting"))
b=int(input("Tug'ilgan yilingizni kiriting"))
c=2025-b
a,c
  # 2. Extract Car Names txt = 'LMaasleitbtui'

txt = "LMaasleitbtui"
txt[::2]
  # 2.Extract Car Names
# Extract car names from the following text:

txt[1::2]
# 3.Extract Car Names
# Extract car names from the following text:

txt = "MsaatmiazD"
txt[::2]
# 3.Extract Car Names
# Extract car names from the following text:

txt[9::-2]
# 4.Extract Residence Area
# Extract the residence area from the following text:

txt = "I'm John. I am from London"
txt[20::]
  # 5.Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

ls = [1,2,3,4,5]
ls[::-1]
# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

matn = "Uzbekiston"
unlilar = ["a", "o", "i", "u", "o'", "e"]
natija = [harf for harf in matn.lower() if harf in unlilar]
print("Unli harflar:", natija)
# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

sonlar = list(map(int, input("4 15 7 2 10").split()))
eng_katta = sonlar[0]

for son in sonlar:
    if son > eng_katta:
        eng_katta = son
print("Eng katta qiymat:", eng_katta)
  # 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

soz = input("Aziza")

if soz == soz[::-1]:
    print("Bu so'z palindrom!")
else:
    print("Bu so'z palindrom emas.")
  

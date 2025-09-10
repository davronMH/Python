# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.

ls = [5,3,1,2,4]
ls.sort()
print(ls)

ls = [5,3,1,2,4]
ls.sort(reverse=True)
print(ls)
#2. Add a Key to a Dictionary
#Write a Python script to add a key to a dictionary.

#Sample Dictionary:

#{0: 10, 1: 20}

key = {0: 10, 1: 20}
key[2] = 30
print(key)
# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

natijalar = {}

for d in (dic1, dic2, dic3):
    natijalar.update(d)
print(natijalar)
#4. Generate a Dictionary with Squares
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5
squares = {}

for i in range(1, n+1):
    squares[i] = i * i

print(squares)
#5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

squares = {i: i*i for i in range(1, 16)}

print(squares)
# 1. Create a Set
# Write a Python program to create a set.

s = {1,2,3,4}
s
# 2. Iterate Over a Set
# Write a Python program to iterate over sets.

s1 = {"Akmal","Anvar","Dilshod"}

for item in s1:
    print(s1)
  # 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.

s1 = {"Akmal","Anvar","Dilshod"}
s1.add("Hasan")
s1
# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.

s1 = {"Akmal","Anvar","Dilshod","Hasan"}
s1.remove("Hasan")
s1

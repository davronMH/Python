#1.def is_leap(year): """ Determines whether a given year is a leap year.

year = int(input('Yilni kiriting'))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print('kabisa yili')
        else:
            print('kabisa yili emas')
    else:
        print('kabisa yili')
else:
    print('kabisa yili emas')

#2. Conditional Statements Exercise
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

#Input Format
#A single line containing a positive integer, n.

#Constraints
#1 <= n <= 100
#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

n = int(input('Juft yoki toq').strip())

if n % 2 == 1:
    print("Toq")
elif n % 2 == 0 and 2<= n <= 5:
    print("Juft")
elif n % 2 == 0 and 6<= n <= 20:
    print("Toq")
elif n % 2 == 0 and n > 20:
    print("Juft")

#3
#Sample Output 0
#Weird
#Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#Give two solutions.

#Solution 1 with if-else statement.

#Solution 2 without if-else statement.

a = int(input("a"))
b = int(input("b"))

events = list(filter(lambda i: i % 2 == 0))

if events:
    print('events')
else:
    print('No even numbers')

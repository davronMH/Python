# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n):
    if n <= 1:   
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True
print(is_prime(3))

# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    s = 0
    for digit in str(abs(k)):
        s += int(digit)
    return s

print(digit_sum(1234))

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def powers_of_two(N):
    k = 0
    while 2 ** k <= N:
        print(2 ** k)
        k += 1
powers_of_two(20)

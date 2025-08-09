txt = 'MsaatmiazD'
txt[::2]
txt = 'MsaatmiazD'
txt[9::-2]
txt = "I'm John. I am from London"
txt[20::]
txt = "Davron"
txt[5::-1]
mevalar = ["olma", "anor", "shaftoli", "o'rik", "gilos"]
print(mevalar[2])
sonlar1 = [1,2,3]
sonlar2 = [4,5,6]
birlashtirilgan = sonlar1+sonlar2
print(birlashtirilgan)
sonlar = [10,20,30,40,50]
yangi_royxat = [sonlar[0], sonlar[len(sonlar)//2], sonlar[-1]]
print(yangi_royxat)
shaharlar = ["London", "New York", "Toshkent", "Paris", "Tokyo"]
if "Paris" in shaharlar:
    print("Paris ro'yxatda bor")
else:
    print("Paris ro'yxatda yo'q")    
sonlar = [1, 2, 3]
yangi_royxat = sonlar * 2
print(yangi_royxat)
sonlar = [10, 20, 30, 40, 50]
sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]
print(sonlar)

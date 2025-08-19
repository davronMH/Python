# 1. Создайте список, содержащий пять различных фруктов, и выведите третий фрукт.
fruits = ["olma", "banan", "shaftoli", "o'rik"]
print(fruits[2])
# 2. Создайте два списка чисел и объедините их в один список.
fruits = ["olma", "anor"]
fruits.extend(["orik","banan"])
print(fruits)
# 3. Из списка чисел извлечь первый, средний и последний элементы и сохранить их в новом списке.
sonlar = [10, 20, 30, 40, 50, 60, 70]
middle_indexs = len(sonlar)//2
new_list = [sonlar[0], sonlar[middle_indexs], sonlar[-1]]
print(new_list)
# 4. Создайте список из пяти ваших любимых фильмов и преобразуйте его в кортеж.
Sevimli_fimlar = ["Mahallad duv-duv gap", "Kelinlar qo'zg'oloni", "Abdullajon", "Chinor ostidagi duel"]
filmlar_tuple = tuple(Sevimli_fimlar)
print(filmlar_tuple)
# 5. По списку городов проверьте, есть ли в списке «Париж», и выведите результат.
cities = input("London", "New York", "Paris")
if "Paris" in cities:
    print("Paris ro'yxatda bor")
else:
    print("Paris ro'yxatda yo'q")
# 6. Создайте список чисел и продублируйте его без использования циклов.
  sonlar = [1,2,3,4,5]
qaytalansin = sonlar * 2
print(qaytalansin)
# 7.Поменять местами первый и последний элементы списка
sonlar = [10,20,30,40]
sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]
print(sonlar)
# 8. Создайте кортеж чисел от 1 до 10 и выведите срез с индексом от 3 до 7.
sonlar = [1,2,3,4,5,6,7,8,9,10]
print(sonlar[2::4])
# 9. Составьте список цветов и подсчитайте, сколько раз в нем встречается слово «синий».
fruits = ["qizil", "ko'k", "sariq", "ko'k"]
print(fruits.count("ko'k"))
# 10. Для заданного кортежа животных найдите индекс «льва».
hayvonlar = ("sher", "ilon", "yo'lbars", "timsoh")
if "sher" in hayvonlar:
    index_sher = hayvonlar.index("sher")
    print("sher bor")
else:
    print("sher yo'q")
# 11. Создайте два кортежа чисел и объедините их в один кортеж.
fruits = ["olma", "anor"]
fruits.extend(["orik","banan"])
print(fruits)
# 12. Дан список и кортеж. Найдите и выведите их длины.
my_list = [10, 20, 30, 40, 50]
my_tuple = ("olma", "banan", "uzum", "gilos")
print("List uzunligi:", len(my_list))
print("Tuple uzunligi:", len(my_tuple))
# 13. Создайте кортеж из пяти чисел и преобразуйте его в список.
numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print("Tuple:", numbers_tuple)
print("List:", numbers_list)
# 14. Для заданного кортежа чисел найдите и выведите максимальное и минимальное значения.
numbers = (12, 45, 7, 89, 3, 56)
max_value = max(numbers)
min_value = min(numbers)
print("Tuple:", numbers)
print("Maximum qiymat:", max_value)
print("Minimum qiymat:", min_value)

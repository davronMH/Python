# input: list1 = [1, 1, 2], list2 = [2, 3, 4]
list1 = [1, 1, 2]
list2 = [2, 3, 4]

common = set(list1) & set(list2)

result = [x for x in list1 if x not in common] + [y for y in list2 if y not in common]
print(result)
# input: list1 = [1, 2, 3], list2 = [4, 5, 6]
s1 = {1,2,3,4}
s2 = {3,4,5,6}

s1.union(s2)

def process(txt):
    unli = "aeiouAEIOU"
    result = ""
    count = 0
    delay = False   

    for i, ch in enumerate(txt):
        result += ch
        count += 1

        if i == len(txt) - 1:
            continue

        if delay:
            result += "_"
            delay = False
            continue

        if count % 3 == 0:
            if ch in unli:     
                delay = True   
            else:
                result += "_"

    return result



print(process("hello"))          
print(process("assalom"))        
print(process("abcabcdabcdeabcdefabcdefg"))

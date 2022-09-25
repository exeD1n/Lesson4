"""Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов."""

one = []

with open("one.txt", "r") as f:
    text = f.read()
    l = text.split("+")
    mapped_numbers = list(map(lambda x: x.split('x'), l))
    for i in mapped_numbers:
        one.append(int(i[0]))
        
        
two = []        
with open("two.txt", "r") as r:
    text_two = r.read()
    ltwo = text_two.split("+")
    mapped_numbers_two = list(map(lambda x: x.split('x'), ltwo))
    for i in mapped_numbers_two:
        two.append(int(i[0]))
        
    
print(sum(two) + sum(one))
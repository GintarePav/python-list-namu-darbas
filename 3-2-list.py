# 3.2. Duoti du masyvai A(n) ir B(m). Sudaryti masyvą C(x) kuris gaunamas iš masyvo A ir B teigiamų elementų. 
import random

list1 = random.sample(range(-100, 101), 10)
print("Pirmas sarasas:", list1)
list2 = random.sample(range(-100, 101), 10)
print("Antras sarasas:", list2)
list3 = []

for i in list1 + list2:
    if i > 0:
        list3.append(i)
print("Sujungtas sarasas:", list3)
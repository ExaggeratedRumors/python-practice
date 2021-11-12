# 2. Wypełnij mailową listę adresową 10 adresami
# i posortuj ją rosnąco po nazwie.
import random


def init_list(n=10):
    address_list = []
    for i in range(0, n):
        address_list.append("Adress" + f"{random.randint(1, 100):3.0f}")
    return address_list


print(sorted(init_list()))

# 1. Podaj listę adresową kilku użytkowników i wylosuj jeden z nich.
import random

address_list = {"John": "Address 1", "Jane": "Address 2", "Jerard": "Address 3"
    , "Timothee": "Address 4", "Thomasin": "Address 5"}

(random_name, random_address) = random.choice(list(address_list.items()))
print(random_name, ":", random_address)

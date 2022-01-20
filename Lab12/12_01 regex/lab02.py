# sprawdź czy adres email jest poprawny

# >>> regex test

import re

email = 'a1_f@wp.pl'

wynik = re.match('^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$', email, re.IGNORECASE)

print(wynik)
if wynik:
    print('ok')
else:
    print('No')

# sprawdzić czy email postaci student@p.lodz.pl oraz student@p..pl
# jest poprawny (jeśli nie to poprawić wyrażenie regularne)

mail = "student@p.lodz.pl"
mail2 = "student@p..pl"

# ^ - szukanie od początku
# $ - chyba sygnalizuje koniec
if re.match('^[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}$', mail, re.IGNORECASE):
    print("mail 1 ok")
if re.match('^[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}$', mail2, re.IGNORECASE):
    print("mail 2 ok")
# sprawdź czy kod pocztowy jest poprawny

# >>> search & match

import re

kod = '45-517'

wynik = re.search('[0-9][0-9]-[0-9][0-9][0-9]', kod)
wynik = re.search('[0-9]{2}-[0-9]{3}', kod)
wynik = re.match('\d{2}-\d{3}', kod)

print(wynik)
if wynik:
    print('ok')
else:
    print('No')

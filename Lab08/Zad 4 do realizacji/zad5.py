# 5. Czytanie danych z internetu z pliku tekstowego (wykorzystać moduł urllib.request) i wyświetlamy w programie wszystkie dane.
#Plik znajduje się w lokalizacji:      
#http://www.imsi.pl/imsi/api/download.php?file=user/u23/Programowanie%20skryptowe/CAL.TXT

import urllib.request

lista = urllib.request.urlopen('http://www.imsi.pl/imsi/api/download.php?file=user/u23/Programowanie%20skryptowe/CAL.TXT')
for i in lista:
    print(i.decode("utf-8"), end = ' ')





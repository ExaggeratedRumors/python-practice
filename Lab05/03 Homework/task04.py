# Wykorzystaj moduł calendar do wyświetlenia kalendarza na dany miesiąc i na cały rok.

import calendar

y = int(input("input year: "))
for month in range(1, 12 + 1):
    print(calendar.month(y, month))

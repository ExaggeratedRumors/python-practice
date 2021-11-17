# Wykorzystaj moduł datetime do podania w osobnych
# linijkach roku, miesiąca, dnia oraz godziny, minuty
# i sekundy w danym momencie.

import datetime

today = datetime.datetime.today()

print("year:", today.year)
print("month:", today.month)
print("day:", today.day)
print("hour:", today.hour)
print("minute:", today.minute)
print("second:", today.second)

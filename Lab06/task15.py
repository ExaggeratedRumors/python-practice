# 15. Wyświetl kalendarz za rok 2019 i zobacz
# czy układ świąt Bożego Narodzenia wygląda atrakcyjnie czy nie

import calendar

for month in range(1, 12 + 1):
    print(calendar.month(2019, month))

print(f"24.12 to {calendar.weekday(2019, 12, 24)} dzień tygodnia")
print(f"25.12 to {calendar.weekday(2019, 12, 25)} dzień tygodnia")
print(f"26.12 to {calendar.weekday(2019, 12, 26)} dzień tygodnia")

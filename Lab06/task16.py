# 16. Do bieżącej daty dadaj 3 tygodni
# lub 21 dni (datetime.timedelta(...))

import datetime

today = datetime.datetime.today() + datetime.timedelta(21)
print(today)
# 6. Podaj w jaki dzień tygodnia urodził się Adam Małysz

import datetime

adam_malysz_bd = datetime.datetime(1977, 12, 3)
print("Adam Małysz urodził sie w ",
    adam_malysz_bd, "\n był to ", adam_malysz_bd.isoweekday(),
      "dzień tygodnia")



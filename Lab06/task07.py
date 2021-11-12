# 7. Ile aktualnie lat ma Adam Małysz
import datetime
from math import floor

adam_malysz_bd = datetime.datetime(1977, 12, 3)
today = datetime.datetime.today()
difference = today - adam_malysz_bd
print("Adam Małysz ma: ", floor(difference.days/365), "lat")



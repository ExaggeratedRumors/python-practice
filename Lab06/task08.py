# 8. Podaj ile dni upłyneło od 1.01.2000 roku do teraz
import datetime

then = datetime.datetime(2000, 1, 1)
today = datetime.datetime.today()
difference = today - then

print("upłynęło :", difference.days, "dni")
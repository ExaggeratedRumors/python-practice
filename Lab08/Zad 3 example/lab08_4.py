# Dla pliku dane.dat obliczyć sumaryczny czas ruchu, sumaryczną przebytą drogę oraz
# prędkość średnią.
with open('dane.dat') as file1:
	data = [[float(val) for val in l.split()] for l in file1 if l[0] != "#"]

czas = 0
droga = 0

for i in data:
	czas += i[0]
	droga += i[1]

szybkosc = droga/czas
print(f"czas: {czas}\ndroga: {droga}\nszybkosc: {szybkosc}")

# 4. Zapisujemy do pliku kąt, sinus i consinus z przedziału 0,360 co 1 stopień oraz czytamy te dane.
# przy zapisie stosujemy różne sposoby formatowania łańcucha znaków ( %, .format() oraz f'') ale efekt ma być taki sam.

import math

start_point = 0
end_point = 360

with open("sinus_cosinus.txt", "w") as file:
    for i in range(start_point, end_point + 1):
        file.write('%3d ' % i)
        file.write("{0:0.5f} ".format(math.sin(math.radians(i))))
        file.write(f"{round(math.cos(math.radians(i)), 5)}")
        file.write("\n")

with open("sinus_cosinus.txt", "r") as file:
    result = [[float(val) for val in line.split()] for line in file]

for i in result:
    print(i)

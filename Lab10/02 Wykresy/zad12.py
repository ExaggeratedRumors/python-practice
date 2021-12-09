# Podaj jako parametr wejsciowy dowolny wielomian, oraz granice x i narysuj wykres (eval)

# Rysujemy funkcję f(x) = 1/(x+1) z wybranego zakresu,
# który przynajmniej obejmuję zakres (-5,5). Uwaga na wartość x = -1.
import pylab
y1=[]
x = pylab.arange(-5, 5, 0.01)
y = 1/(x+1)
for i in y:
    if -10<i<10:
        y1.append(i)
    else:
        y1.append(pylab.NaN)
y = y1[:]
pylab.axhline(0, color='#555')
pylab.axvline(0, color='#555')
pylab.plot(x, y, 'r')
pylab.grid(True)
pylab.show()
import math
a = float(input("Podaj liczbę ujemną:  "))
print("")
if a == 0:
    print ("Wartość bezwzględna z:", int(a), "wynsi: ", int(a))
    print("")
elif a < 0:
    a = math.floor(a)
    print ("Wartość bezwzględna z:", a, "wynsi: ", int(math.fabs(a)))
    print("")
else:
    a = math.ceil(a)
    print("Wartość bezwzględna z:", a, "wynsi: ", int(math.fabs(a)))
    print("")

import math
def vypocet_korena:
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)

a=int(input("zadaj cislo a: "))
b=int(input("zadaj cislo b: "))
c=int(input("zadaj cislo c: "))

d=(b*b)-(4*a*c)

if d > 0:
    d= math.sqrt(d)
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    print("vypocty kvadratickej rovnice su:", int(x1), ",", int(x2))
elif

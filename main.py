# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math

print("Lab NR1 PI Murafa Dan")
print("-----------------------Ex1-------------------------------")
print()
print("a)  2/5 = ", 2/5)  #float
print("b) 7.9+1.1= ", 7.9+1.1)  # float + float  chiar daca raspunsul este 9 oricum este 9.0 (float)
print("c) 6-2= ", 6-2)  #int-int  ramane int
print("d) 8+1= ", 8+1)   #int + int = int
print("e) 9+1.1= ", 9+1.1)
print("f) 2*7= ", 2*7)
print("g) 3.2/6= ", 3.2/6)
print("h) 5*8.0= ", 5*8.0)
print("i) 3.4-1.1= ", 3.4-1.1)
print("j) 9%2= ", 9 % 2)
print("k) 9%-2= ", 9 % -2)
print("l) -9 % 2= ", -9 % 2)
print()
print("-----------------------Ex2-------------------------------")
print()
print("a) bool(-30) = ", bool(-30))
print("b) bool(0.2) = ", bool(0.2))
print("c) bool(0) = ", bool(0))
print("a) bool(s) = ", bool('s'))
print()
print("-----------------------Ex3-------------------------------")
print()
print("a) type(5.8e+3) = ", type(5.8e+3))
print("b) type(1+4.0+2) = ", type(1+4.0+2))
print("c) type(None) = ", type(None))
print("d) type('float') = ", type('float'))
print("e) type(4+2j) = ", type(4+2j))
print()
print("-----------------------Ex4-------------------------------")
print()
def ex4 (x=32 , y=6 ):
    print(" X = 32  Y = 6")
    print("a) z=x % y + y  z=", x % y + y)
    print("c) y = x//y z=x//y  z=", x//(x//y))
    print("d) y = x//y+y z=x//y  z=", x//(x//y+y))
    print("e) y = x % y + 2 , z = x % y + x   z=", x % (x % y + 2) + x)
    print("f) y = x // y  , z = x % (y + 2)    z=", x % ((x // y) + 2))
    print("g) y = x % y , z = x // (y + 2)  z=", x // ((x % y)+2))

ex4()

print()
print("-----------------------Ex5-------------------------------")
print()
num1 = 12.5/2.5
# pyton automat declara variabila daca nu o declaram deci este float
num2 = int(12.5)/int(2.5)
# odata ce declaram variabila si inautrul ei introducem valoare de tip float
#  pyton va socoti doar valoarea intreaga  (12.5) = 12    (2.5) = 2   12/2=6
num3 = int(12.5/2.5)
#chiar daca am declarat valoarea int  oepratia din inautrul ei se va calcula dupa float / float
print("num1= ", num1)
print("num2= ", num2)
print("num3= ", num3)
#comparam care ecuatie este cea mai mare
if(num1>num2 and num1>num3):
    print("Numarul 1 este cel mai mare")
elif(num2>num1 and num2>num3):
    print("Numarul 2 este cel mai mare")
else:
    print("Numarul 3 este cel mai mare")
del num1 , num2 , num3
# del elibereaza memoria alocata pentru variabilele pentru a rula programul mai efectiv
print()
print("-----------------------Ex6-------------------------------")
print()
print("a) ", str(6)*int('5'))
print("b) ", int("6") + float("6.1"))
#  linie de cod invalida   string nu poate fi scris de (float) ori .
#  print("c) ", str(6) * float("6.1"))
print("d) ", str(6/4) * 2)
print()
print("-----------------------Ex7-------------------------------")
print()
def ex7 (x=3 , y=4):
    print("a) ", x ,"+", y ,"= ?")  #metoda 1
    print(f"a) {x} + {y} = ?")      #metoda 2
    print(f"b) ({x})({y})")         #metoda 1
    print("b) (",x,")(",y,")")      #metoda 2
    print("x=",x,"; y=",y)
    print(f"Raspuns:({x};{y})")
ex7()
print()
print("-----------------------Ex8-------------------------------")
print()
x=int (input("Introduceti x:"))
y= int (input("Introduceti y:"))
print("z=", (x **2 + y **2)*((x-y)**2))
print()
print("-----------------------Ex9-------------------------------")
print()
x=float (input("Introduceti x:"))

if(x<0):
    print("x=",x)
elif(0<=x<10):
    print("x=",2*x)
elif(10<=x<100):
    print("x=",3*x)
elif(x>=100):
    print("x=",4*x)
print()
print("-----------------------Ex10-------------------------------")
print()
x = int(input("Introduceți valoarea pentru x: "))
y = int(input("Introduceți valoarea pentru y: "))
z = int(input("Introduceți valoarea pentru z: "))
m = int(input("Introduceți valoarea pentru m: "))

if(x==y or x==z or x==m):
    print("Nu sunt Distincte")
elif(y==z or y==m or z==m):
    print("Nu sunt Distincte")
else:
    print("Sunt Distincte")

print()
print("-----------------------Ex11-------------------------------")
print()
x = int(input("Introduceți valoarea pentru x: "))
y = int(input("Introduceți valoarea pentru y: "))
z = int(input("Introduceți valoarea pentru z: "))
if(x == y + z):
    print("X este suma la Y si Z")
elif(y == z + x):
    print("Y este suma la X si Z")
elif(z == x + y):
    print("Z este suma la X si Y")

print()
print("-----------------------Sarcina Individuala-------------------------------")
print("---------------------------Varianta 7 ------------------------------------")
print()
w = 1.23; e =5.11; qfirst = 0.5; qlast = 3.1; qpas = 0.1 ; n = 1
q = qfirst
while q <= qlast:
    a= ( 3 * math.tan(5 * (math.exp(e) - w**2)) - math.sqrt(q) / w)
    print(f"a{n}=", a )
    print(f"b{n}= ", (a ** 3) / q - math.sin(a-q*q)** 3)
    q +=qpas
    n=n+1

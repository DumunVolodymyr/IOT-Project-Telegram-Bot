import sys
x1 = int (input("Введіть координату х першої вершини   "))
y1 = int (input("Введіть координату у першої вершини   "))
z1 = int (input("Введіть координату z першої вершини   "))

x2 = int (input("Введіть координату х другої вершини   "))
y2 = int (input("Введіть координату у другої вершини   "))
z2 = int (input("Введіть координату z другої вершини   "))

x3 = int (input("Введіть координату х третьої вершини  "))
y3 = int (input("Введіть координату y третьої вершини  "))
z3 = int (input("Введіть координату z третьої вершини  "))

x4 = int (input("Введіть координату х четвертої вершини  "))
y4 = int (input("Введіть координату y четвертої вершини  "))
z4 = int (input("Введіть координату z четвертої вершини  "))

b1=x2-x1
b2=y2-y1
b3=z2-z1
c1=x3-x1
c2=y3-y1
c3=z3-z1
d1=x4-x1
d2=y4-y1
d3=z4-z1

print("Знайдемо вектор AB (", b1, ",", b2, ",", b3,")")
print("Знайдемо вектор AC (", c1, ",", c2, ",", c3,")")
print("Знайдемо вектор AD (", d1, ",", d2, ",", d3,")")

vector1 = []
vector1.append(b1)
vector1.append(b2)
vector1.append(b3)
vector2 = []
vector2.append(c1)
vector2.append(c2)
vector2.append(c3)
vector3 = []
vector3.append(d1)
vector3.append(d2)
vector3.append(d3)

matrix = []
matrix = [[vector1], [vector2], [vector3]]
print("Отримаємо матрицю вигляду: ")

for i in range(3):
     print(matrix[i], end = "\n")

print("Знайдемо детермінант матриці ")
det = (b1*c2*d3)+(b2*c3*d1)+(b3*c1*d2)-(b3*c2*d1)-(b1*c3*d2)-(b2*c1*d3)
print(b1, "*", c2, "*", d3, "+",b2,"*",c3,"*",d1,"+",b3,"*",c1,"*",d2, "-", b3, 
"*", c2, "*", d1, "-",b1,"*",c3,"*",d2,"-",b2,"*",c1,"*",d3, "=" ,b1*c2*d3, "+", b2*c3*d1, "+",
b3*c1*d2, "-", b3*c2*d1, "-",b1*c3*d2,"-", b2*c1*d3, "=", det)

###################################################################################
def V(det):
    V = abs(det)/6
    print("Об'єм вектора знайдемо за формулою:\n", "V = 	(1/6	|a · [b × c]|)")
    print(V)

V(det)










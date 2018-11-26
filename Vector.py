x1 = int (input("Введіть координату х першого вектора "))
y1 = int (input("Введіть координату y першого вектора "))
z1 = int (input("Введіть координату z першого вектора "))
vector1 = []
vector1.append(x1)
vector1.append(y1)
vector1.append(z1)
x2 = int (input("Введіть координату х другого вектора "))
y2 = int (input("Введіть координату y другого вектора "))
z2 = int (input("Введіть координату z другого вектора "))
vector2 = []
vector2.append(x2)
vector2.append(y2)
vector2.append(z2)
x3 = int (input("Введіть координату х третього вектора  "))
y3 = int (input("Введіть координату y третього вектора  "))
z3 = int (input("Введіть координату z третього вектора  "))
vector3 = []
vector3.append(x3)
vector3.append(y3)
vector3.append(z3)
det = (x1 * y2 * z3) + (x2 *y3 * z1) + (x3 * y1 * z2) - (x3 * y2 * z1) -(y3*z2*x1) - (x2*y1*z3)
matrix = []
matrix = [[vector1], [vector2], [vector3]]

print("Отримаєм матрицю вигляду: ")

for i in range(3):
     print(matrix[i], end = "\n")
print("Знайдемо детермінант матриці:  ")

print(x1, "*", y2, "*", z3, "+",x2,"*",y3,"*",z1,"+",x3,"*",y1,"*",z2, "-", x3, 
"*", y2, "*", z1, "-",y3,"*",z2,"*",x1,"-",x2,"*",y1,"*",z3, "=" ,x1*y2*z3, "+", x2*y3*z1, "+",
x3*y1*z2, "-", x3*y2*z1, "-", x2*y1*z3, "=", det)

print("Об'єм піраміди розрахуємо по формулі: \n", "V = 	(1/6	|a · [b × c]|)")


#######################################################################################################
def V(det):
    V = abs(det)/6
    print(V)

V(det)
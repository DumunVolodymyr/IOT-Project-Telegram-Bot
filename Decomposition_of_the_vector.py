import sys
import math

dimension_of_the_vector = 0
while True:
      dimension_of_the_vector = int(input("Вкажіть розмірність вектора. Введіть '2', якщо розмірність два і '3', якщо розмірність три "))
      if dimension_of_the_vector == 2 or dimension_of_the_vector == 3:
         break
      if dimension_of_the_vector != 2 or dimension_of_the_vector != 3:
         print("Помилка. Перевірте введене значення")

form_of_the_vector = 0 
while True:
      form_of_the_vector = int (input("Як заданий вектор? Введіть '1', якщо точками, і '2', якщо координатами "))
      if form_of_the_vector == 1 or form_of_the_vector == 2:
         break
      if form_of_the_vector != 1 or form_of_the_vector != 2:
         print("Помилка. Перевірте введене значення")
      

def Сoordinates_2():
    x = int (input("Введіть координату x "))
    y = int (input("Введіть координату y "))

    vector = math.sqrt((x*x) + (y*y))

    print("Знайдемо модуль вектора:\n", "|a| = ",vector)

    cos1 = x/vector
    cos2 = y/vector

    print("Розрахуємо косинуси за формулами: ")
    print("Косинус альфа дорівнює координата х поділити на модуль вектора: cos(a) = ", x, "/", vector, "=", cos1)
    print("Косинус бета дорівнює координату y поділити на модуль вектора: cos(b) = ", y, "/", vector, "=", cos2)

def Сoordinates_3():
    x = int (input("Введіть координату x "))
    y = int (input("Введіть координату y "))
    z = int (input("Введіть координату z "))

    vector = math.sqrt((x*x) + (y*y) + (z*z))

    print("Знайдемо модуль вектора:\n", "|a| = ",vector)

    cos1 = x/vector
    cos2 = y/vector
    cos3 = z/vector
    print("Розрахуємо косинуси за формулами: ")
    print("Косинус альфа дорівнює координата х поділити на модуль вектора: cos(a) = ", x, "/", vector, "=", cos1)
    print("Косинус бета дорівнює координату y поділити на модуль вектора: cos(b) = ", y, "/", vector, "=", cos2)
    print("Косинус гама дорівнює координата z поділити на модуль вектора: cos(c) = ", z, "/", vector, "=", cos3)

def Points_2():
    x1 = int (input("Введіть координату х точки A "))
    y1 = int (input("Введіть координату y точки A "))
    x2 = int (input("Введіть координату х точки B "))
    y2 = int (input("Введіть координату y точки B "))

    b1=x2-x1
    b2=y2-y1

    print("Знайдемо вектор АВ: ")
    print("Знайдемо координату x: х =", x2, "-", x1, "=", b1)
    print("Знайдемо координату y: у =", y2, "-", y1, "=", b2)

    vector = math.sqrt((b1*b1) + (b2*b2))
    print("Знайдемо модуль вектора:\n", "|a| = ", vector)

    cos1 = b1/vector
    cos2 = b2/vector
   
    print("Розрахуємо косинуси за формулами: ")
    print("Косинус альфа дорівнює координата х поділити на модуль вектора: cos(a) = ", b1, "/", vector, "=", cos1)
    print("Косинус бета дорівнює координату y поділити на модуль вектора: cos(b) = ", b2, "/", vector, "=", cos2)

def Points_3():
    x1 = int (input("Введіть координату х точки A "))
    y1 = int (input("Введіть координату y точки A "))
    z1 = int (input("Введіть координату z точки A "))
    x2 = int (input("Введіть координату х точки B "))
    y2 = int (input("Введіть координату y точки B "))
    z2 = int (input("Введіть координату z точки B "))

    b1=x2-x1
    b2=y2-y1
    b3=z2-z1

    print("Знайдемо вектор АВ:")
    print("Знайдемо координату x: х =", x2, "-", x1, "=", b1)
    print("Знайдемо координату y: х =", y2, "-", y1, "=", b2)
    print("Знайдемо координату z: х =", z2, "-", z1, "=", b3)

    vector = math.sqrt((b1*b1) + (b2*b2) + (b3*b3))
    print("Знайдемо модуль вектора:\n", "|a| = ",vector)

    cos1 = b1/vector
    cos2 = b2/vector
    cos3 = b3/vector
    print("Розрахуємо косинуси за формулами: ")
    print("Косинус альфа дорівнює координата х поділити на модуль вектора: cos(a) = ", b1, "/", vector, "=", cos1)
    print("Косинус бета дорівнює координату y поділити на модуль вектора: cos(b) = ", b2, "/", vector, "=", cos2)
    print("Косинус гама дорівнює координата z поділити на модуль вектора: cos(c) = ", b3, "/", vector, "=", cos3)

if dimension_of_the_vector == 2:
    if form_of_the_vector == 1: 
        Points_2()
    if form_of_the_vector == 2:
        Сoordinates_2()

if dimension_of_the_vector == 3:
    if form_of_the_vector == 1: 
        Points_3()
    if form_of_the_vector == 2:
       Сoordinates_3()
 


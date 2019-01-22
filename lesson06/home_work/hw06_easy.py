# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    # Определяем длины сторон
    def dist1_2(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** (1 / 2)

    def dist1_3(self):
        return ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** (1 / 2)

    def dist2_3(self):
        return ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** (1 / 2)

    # Определяем площадь
    def area(self):
        return abs(0.5*(self.x1*(self.y2-self.y3)+self.x2*(self.y3-self.y1)+self.x3*(self.y1-self.y2))) 

    # Определяем периметр
    def perimetr(self):
        return self.dist1_2() + self.dist1_3() + self.dist2_3()

    # Находим длины высот - возвращает кортеж из 3-х высот
    def height(self):
        height_1 = 2 * self.area() / self.dist2_3()
        height_2 = 2 * self.area() / self.dist1_3()
        height_3 = 2 * self.area() / self.dist1_2()
        return (height_1, height_2, height_3)


# Проверка
tr1 = Triangle(0,0,1,1,2,0)
print(tr1.area())
print(tr1.perimetr())
print(tr1.height())
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(Triangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3)
        self.x4 = x4
        self.y4 = y4

    # Определяем длины сторон
    def dist3_4(self):
        return ((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2) ** (1 / 2)
 
    def dist1_4(self):
        return ((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2) ** (1 / 2)   

    # Проверка на равносторонность
    def is_equal(self):
        if (self.dist1_2() == self.dist3_4() and self.dist2_3() != self.dist1_4()) or (self.dist1_2() != self.dist3_4() and self.dist2_3() == self.dist1_4())  :
          is_eq = True
        else:
            is_eq = False    
        return is_eq
        
    # Определяем площадь
    def area(self):
        a = self.dist2_3()
        b = self.dist1_4()
        c = self.dist1_2()
        d = self.dist3_4()
        s = 1/2 * (a + b) * (c ** 2 * (((b-a)**2 + c**2 - d**2)/(2*(b-a)))) ** 1/2
        return s


    # Определяем периметр
    def perimetr(self):
        return self.dist1_2() + self.dist2_3() + self.dist3_4() + self.dist1_4()


# Проверка
tr2 = Trapezium(0,0,1,1,3,1,4,0)
print(tr2.area())
print(tr2.perimetr())
print(tr2.is_equal())

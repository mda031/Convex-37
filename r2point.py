from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    # Поиск точек пересечения отрезка [a,b] с положительными частями осей x и y
    @staticmethod
    def intersection2(a, b):
        with_x = R2Point(-1, -1)
        with_y = R2Point(-1, -1)
        arr2 = []
        arr3 = []
        # случай, когда прямая, содержащая отрезок ab, не параллельна осям
        if a.y != b.y and a.x != b.x:
            with_x.x = ((a.y * (a.x - b.x)) / (b.y - a.y)) + a.x
            with_x.y = 0
            with_y.x = 0
            with_y.y = ((a.x * (a.y - b.y)) / (b.x - a.x)) + a.y
        # случай, когда прямая параллельна оси у (но не совпадает)
        elif a.x == b.x:
            if a.x != 0:
                with_x.x = ((a.y * (a.x - b.x)) / (b.y - a.y)) + a.x
                with_x.y = 0
        # случай, когда прямая параллельна оси х (но не совпадает)
        elif a.y == b.y:
            if a.y != 0:
                with_y.x = 0
                with_y.y = ((a.x * (a.y - b.y)) / (b.x - a.x)) + a.y

        # проверяем, лежат ли точки пересечения с осями на отрезке
        # если лежат, то добавляем в массив с точками пересечения
        if ((a.x <= with_x.x <= b.x or b.x <= with_x.x <= a.x) and
                (a.y <= with_x.y <= b.y or b.y <= with_x.y <= a.y)):
            arr2.append(with_x)
        if ((a.x <= with_y.x <= b.x or b.x <= with_y.x <= a.x) and
                (a.y <= with_y.y <= b.y or b.y <= with_y.y <= a.y)):
            arr2.append(with_y)

        # оставляем в массиве только те точки пересечения,
        # которые лежат на положительных частях осей
        for i in range(len(arr2)):
            if arr2[i].x >= 0 and arr2[i].y >= 0:
                arr3.append(arr2[i])

        return arr3

    # Определяет, лежат ли в первой четверти начало и конец отрезка
    @staticmethod
    def intersection1(a, b):
        arr1 = []
        zero = R2Point(0.0, 0.0)
        if a.x >= 0 and a.y >= 0:
            arr1.append(a)
        if b.x >= 0 and b.y >= 0:
            arr1.append(b)
        # отрезок лежит на оси y
        if a.x == 0 and b.x == 0:
            if a.y * b.y < 0:
                arr1.append(zero)
        # отрезок лежит на оси x
        if a.y == 0 and b.y == 0:
            if a.x * b.x < 0:
                arr1.append(zero)

        return arr1

    # Находит длину отрезка в первом квадранте
    @staticmethod
    def len_of_segment(a, b):
        arr1 = R2Point.intersection1(a, b)
        arr2 = R2Point.intersection2(a, b)
        len1 = len(arr1)
        len2 = len(arr2)
        if len2 == 0:
            if len1 == 2:
                return R2Point.dist(arr1[0], arr1[1])
            else:
                return 0
        elif len2 == 1:
            if len1 == 1:
                return R2Point.dist(arr1[0], arr2[0])
            elif len1 == 2:
                return R2Point.dist(arr1[0], arr1[1])
        elif len2 == 2:
            if len1 == 0:
                return R2Point.dist(arr2[0], arr2[1])
            elif len1 == 2:
                return R2Point.dist(arr1[0], arr1[1])
            elif len1 == 1:
                return R2Point.dist(arr2[0], arr2[1])


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))

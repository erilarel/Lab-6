# Вариант 6
class Figure:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self):
        # Метод 1
        Valuee = self.a * self.b * self.c
        return Valuee


class Empty_figure(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def Value_of_emptyfigure(self):
        # Метод 2.1 (объём тела за вычетом пустоты)
        V = Figure.value(self) - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
        return V


class Massiv_figures(Figure):
    def __init__(self, a, b, c, count_shapes):
        super().__init__(a, b, c)
        self.count_shapes = count_shapes

    def sum_values(self):
        # Метод 2.2 (суммарный объём нескольких одинаковых фигур)
        ans = Figure.value(self) * self.count_shapes
        return ans


#Пример использования:
if __name__ == "__main__":
    kub = Empty_figure(10, 2, 7, 1)
    sphere = Massiv_figures(10, 2, 5, 5)
    print(f"Объём куба:  {kub.value()}")
    print(f"Объём куба с внутренней полостью: {kub.Value_of_emptyfigure()}"'\n')
    print(f"Объём {sphere.count_shapes} фигур: {sphere.sum_values()}")
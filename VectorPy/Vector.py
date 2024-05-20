class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Aby dodać wektory, muszą mieć tę samą długość")
        result = [a + b for a, b in zip(self.values, other.values)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Aby wektory mogły się pomnożyć, muszą być tej samej długości")
        result = sum(a * b for a, b in zip(self.values, other.values))
        return result

    def get_vals(self):
        return self.values

v1 = Vector([1, 2, 1, 5])
v2 = Vector([2, 3, 1, 4])

v3 = v1 + v2
print(v3.get_vals())  

result = v1 * v2
print(result)





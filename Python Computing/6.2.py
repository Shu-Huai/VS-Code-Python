class Vecter:
    def __init__(self, x=0, y=0, z=0):
        self.x_ = x
        self.y_ = y
        self.z_ = z

    def __add__(self, V):
        result = Vecter()
        result.x_ = self.x_ + V.x_
        result.y_ = self.y_ + V.y_
        result.z_ = self.z_ + V.z_
        return result

    def __sub__(self, V):
        result = Vecter()
        result.x_ = self.x_ - V.x_
        result.y_ = self.y_ - V.y_
        result.z_ = self.z_ - V.z_
        return result

    def __mul__(self, number):
        result = Vecter()
        result.x_ = self.x_ * number
        result.y_ = self.y_ * number
        result.z_ = self.z_ * number
        return result

    def __truediv__(self, number):
        result = Vecter()
        result.x_ = self.x_ / number
        result.y_ = self.y_ / number
        result.z_ = self.z_ / number
        return result


v1 = Vecter(1, 2, 3)
v2 = Vecter(4, 5, 6)
v3 = v1 + v2
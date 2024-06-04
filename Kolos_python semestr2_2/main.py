class Trojkat:
    H = 1

    def __init__(self, A_user = 100):
        self.A = A_user

    def poletrojkata(self):
        return self.A * self.H * 0.5

    def __sub__(self, other):
        return self.poletrojkata() - other.poletrojkata()


class GraniastoslupTrojkatny(Trojkat):
    def __init__(self, wysokosc_user, A_user):
        super().__init__(A_user)
        if A_user <= 0:
            raise ValueError("Wrong value")
        try:
            self._wysokosc = float(wysokosc_user)
        except TypeError as e:
            raise TypeError(e)

    def polegraniastoslupa(self):
        return ((3 * self._wysokosc * self.A) + (2 * self.poletrojkata()))



t1 = Trojkat(10)
t2 = Trojkat(20)
print(t2-t1)

g1 = GraniastoslupTrojkatny(10, 10)
print("pole g1: ", g1.polegraniastoslupa())

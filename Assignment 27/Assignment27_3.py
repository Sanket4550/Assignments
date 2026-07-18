class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total == self.Value

    def Factors(self):
        print("Factors:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i
        return total


obj1 = Numbers(int(input("Enter Number: ")))

print("Prime :", obj1.ChkPrime())
print("Perfect :", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors :", obj1.SumFactors())

print()

obj2 = Numbers(int(input("Enter Number: ")))

print("Prime :", obj2.ChkPrime())
print("Perfect :", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors :", obj2.SumFactors())
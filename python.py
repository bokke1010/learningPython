class Fibonatie:
    cash = {}
    def calculate(self, index):
        if index < 2:
            return index
        else:
            return self.__getFib__(index-1) + self.__getFib__(index-2)

    def __getFib__(self, index):
        if str(index) in self.cash:
            return self.cash[str(index)]
        else:
            val = self.calculate(index)
            self.cash[str(index)] = val
            return val

fibie = Fibonatie()
i = 0
while True:
    print(fibie.calculate(i))
    i += 1

class Difference:
    def __init__(self, a):
        self.maximumDifference = self.computeDifference()
        self.__elements = a

    def computeDifference(self):
        maximum = 0
        size = len(self.__elements)
        for i in range(size - 1):
            for j in range(i + 1, size):
                if abs(self.__elements[i] - self.__elements[j]) > maximum:
                    maximum = abs(self.__elements[i] - self.__elements[j])

        return maximum




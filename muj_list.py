class MujList():

    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str(self.list)

    def __add__(self, other):
        if len(self.list) != len(other.list):
            raise ValueError("Operace nelze provést")
        temp = []
        for i in range(len(self.list)):
            temp.append(self.list[i] + other.list[i])
        return temp

    def __sub__(self, other):
        if len(self.list) != len(other.list):
            raise ValueError("Operace nelze provést")
        temp = []
        for i in range(len(self.list)):
            temp.append(self.list[i] - other.list[i])
        return temp

    def __mul__(self, other):
        if len(self.list) != len(other.list):
            raise ValueError("Operace nelze provést")
        temp = []
        for i in range(len(self.list)):
            temp.append(self.list[i] * other.list[i])
        return temp

    def __truediv__(self, other):
        if len(self.list) != len(other.list):
            raise ValueError("Operace nelze provést")
        temp = []
        for i in range(len(self.list)):
            temp.append(self.list[i] / other.list[i])
        return temp
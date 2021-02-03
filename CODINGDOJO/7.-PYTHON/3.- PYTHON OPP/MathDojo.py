class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        if len(nums)>0:
            for i in nums:  #for de objeto, recorremos nums para ver que hay algo
                self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        if len(nums)>0:
            for i in nums:
                self.result -= i
        return self
# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
x=md.add(2,4,4,4).add(4,4,4).add(2,2).subtract(8,8,8).result
print(x)

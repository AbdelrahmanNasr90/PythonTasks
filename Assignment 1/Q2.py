def getNumberFromFunc():
    X=Y=Z=10
    return X,Y,Z
print(getNumberFromFunc())


# 2)

 
def sum(num):
    def add(x):
        return num + x
    return add
print(sum(12)(5))
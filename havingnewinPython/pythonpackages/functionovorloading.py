from functools import singledispatch
from decimal import Decimal

@singledispatch
def add(a,b):
    raise NotImplementedError('unsupported type')

@add.register(float)
@add.register(Decimal)
def _(a,b):
    print("first argument of type ",type(a))
    print(a+b)

if __name__=="__main__":
    add(1.23,5.5)
    add(Decimal(100.5),Decimal(10.789))



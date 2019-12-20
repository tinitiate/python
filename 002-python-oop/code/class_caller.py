from class_test import Test as t1

Obj1 = t1()
Obj1.num1 = 100
Obj1.num2 = 200

Obj2 = t1()
Obj2.num1 = 1000
Obj2.num2 = 2000

print(Obj1.__sizeof__() + Obj2.__sizeof__())

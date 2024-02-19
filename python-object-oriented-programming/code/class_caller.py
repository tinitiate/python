from class_test import OOP as t1

# Create Obj1 of class OOP
Obj1 = t1()
Obj1.num1 = 100
Obj1.num2 = 200
Obj1.add1(N1=100, N2=200)
Obj1.mul1(N1=200, N2=300)
Obj1.print_class_vars()


# Create Obj2 of class OOP
Obj2 = t1()
Obj2.num1 = 1000
Obj2.num2 = 2000
Obj2.add1(N1=400, N2=500)
Obj2.mul1(N1=600, N2=700)
Obj2.print_class_vars()

# Print the Object Sizes of both objects
print(Obj1.__sizeof__() + Obj2.__sizeof__())

import func_test as f1
import func_test as f2

# Create Obj1 of class OOP
f1.num1 = 100
f1.num2 = 200
f1.add1(N1=100, N2=200)
f1.mul1(N1=200, N2=300)
f1.print_class_vars()

# Create Obj2 of class OOP
f2.num1 = 1000
f2.num2 = 2000
f2.add1(N1=400, N2=500)
f2.mul1(N1=600, N2=700)
f2.print_class_vars()

# Print the Object Sizes of both objects
print(f1.__sizeof__() + f2.__sizeof__())

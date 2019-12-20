import func_test as f1
import func_test as f2

f1.num1 = 100
f1.num2 = 200

f2.num1 = 1000
f2.num2 = 2000

print(f1.__sizeof__() + f2.__sizeof__())

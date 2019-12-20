# Call Module using Relative path
from MathCalc import add2nums, mul2nums, sub2nums

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)
sub2nums.sub2nums(40,10)


# Call Module using Absolute Path
from .code.tinitiate.source.python.python-advanced.code.MathCalc import add2nums, mul2nums

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)

# Convert Tuple of tuples to Dict using dict() Function
tuple1 = ((1, 'a'),(2, 'b'))
dict1 = dict( (y, x) for x, y in tuple1 )
print(dict1)
# {'a': 1, 'b': 2}
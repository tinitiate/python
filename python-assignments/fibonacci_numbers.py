
max=10
ctr=0
fib_output = [0,1]
while len(fib_output)<=max:
    fib_output.append(fib_output[-1]+fib_output[-2])

print(fib_output)


prime_nums=[]
ctr=0
prime=1
while ctr<=max:
    for c in range(ctr):
        if c not in [0,1,ctr]:
            if ctr%c == 0:
                prime=0
                break
    if prime==1:        
        prime_nums.append(ctr)
    else:
        prime=1
    ctr+=1

    # prime_nums.append()
print(prime_nums)



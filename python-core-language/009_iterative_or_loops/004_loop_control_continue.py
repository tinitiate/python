for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue 
    print('Run:', c,'step2')
    print('Run:', c,'step3')

# OUTPUT
#        Run: 0 step1
#        Run: 0 step2
#        Run: 0 step3
#        Run: 1 step1    # Didnt print step2 and step3
#        Run: 2 step1
#        Run: 2 step2
#        Run: 2 step3
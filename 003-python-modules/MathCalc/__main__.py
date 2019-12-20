if __name__ == '__main__':
    import sys
    import add2nums as a2
    import mul2nums as m2

    if len(sys.argv) != 4:
        print("Enter the Operation Name and values")
        print("add2nums Num1 Num2")
        print("-- OR --")
        print("mul2nums Num1 Num2")
    else:    
        if sys.argv[1] == "add2nums":
            a2.add2nums(int(sys.argv[2]), int(sys.argv[3]))
        elif sys.argv[1] == "mul2nums":
            m2.mul2nums(int(sys.argv[2]), int(sys.argv[3]))

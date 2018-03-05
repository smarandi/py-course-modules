def problem1_7():
    b1=float(input("Enter the length of one of the bases: "))
    b2=float(input("Enter the length of the other base: "))
    h=float(input("Enter the height: "))


    area = (1/2) * (b1 + b2) * h

    print("The area of a trapezoid with bases {} and {} and height {} is {}".format(b1,b2, h, area))

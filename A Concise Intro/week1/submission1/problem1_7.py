def problem1_7():
    base_1 = input("Enter the length of one of the bases: ")
    base1 = float(base_1)
    base_2 = input("Enter the length of the other base: ")
    base2 = float(base_2)
    height_ = input("Enter the height: ")
    height = float(height_)
    area_ = (1/2)*(base1+base2)*height
    print("The area of a trapezoid with bases", base1, "and", base2,end=' ')
    print("and height", height,"is", area_)
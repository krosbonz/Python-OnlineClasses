def problem2_7():
    """ computes area of triangle using Heron's formula. """
    sidea = input("Enter length of side one: ")
    sideb = input("Enter length of side two: ")
    sidec = input("Enter length of side three: ")
    sidea1 = float(sidea)
    sideb1 = float(sideb)
    sidec1 = float(sidec)
    perim = .5*(sidea1 + sideb1 + sidec1)
    prearea = perim*(perim-sidea1)*(perim-sideb1)*(perim-sidec1)
    area = prearea**.5
    print("Area of a triangle with sides", sidea1, sideb1, sidec1, "is", area)
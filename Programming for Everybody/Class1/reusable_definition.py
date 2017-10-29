def computepay(h,r):
    return h * r
    

h = input("Enter Hours:")
r = input("Enter Rate:")
hrs = float(h)
rate = float(r)

if h > 40:
    p = (hrs - 40) * 15.75 + 40 * 10.50
else:
    p = computepay(h,r)
    
print(p)

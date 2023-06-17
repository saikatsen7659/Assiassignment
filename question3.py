def simpleInterest(p,r,t):
    print("the principle value", p)
    print("the rate of interest value", r)
    print("the time value", t)
    
    i = (p*r*t)/100
    print("the value of: ", i)
    
p = int(input("enter the value of p: "))
r = float(input("enter the value of r: "))
t = int(input("enter the value of t: "))
simpleInterest(p,r,t)


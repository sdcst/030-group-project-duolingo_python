#calculate the "volume" of a multidimensional square or sphere
#factor a polynomial
#turn polynomial into apq form
#Calculate compound interest


def multidim(length,Type,dimensions=2):
    if Type == "Square":
        V = length**dimensions
    elif Type == "Circle":
        if dimensions >= 5:
            V = "Error"
        elif dimensions == 1:
            V = length
        elif dimensions == 2:
            V = 3.14159*length**2
        elif dimensions == 3:
            V = (4/3)*3.14159*length**3
        elif dimensions == 4:
            V = 0.5*(3.14159**2)*length**4
    V = round(V,2)
    return V

def factor(a,b,c):
    if (b**2 - 4*a*c) < 0:
        factor = "No solution"
    elif (b**2 - 4*a*c) == 0:
        ans = (-1*b)/2*a
        ans = 
        if ans >= 0:
            factor = f"(x - {ans})"
        if ans < 0:
            factor = f"(x + {ans})"
    elif (b**2 - 4*a*c) > 0:
        ans = ((-1*b)*((b**2 - 4*a*c)**0.5))/(2*a)
            if ans 
        
    return factor

def APQ(a,b,c):


def Com_Int():

assert multidim("Square") == 
assert factor() ==
assert Com_Int() ==
assert 



















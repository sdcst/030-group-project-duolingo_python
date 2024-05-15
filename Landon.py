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
        ans = round
        if ans >= 0:
            factor = f"(x - {ans})^2"
        elif ans < 0:
            factor = f"(x + {ans})^2"
    elif (b**2 - 4*a*c) > 0:
        ans1 = ((-1*b)+((b**2 - 4*a*c)**0.5))/(2*a)
        ans2 = ((-1*b)-((b**2 - 4*a*c)**0.5))/(2*a)
        if ans1 >= 0:
            factor1 = f"(x - {ans1})"
        elif ans1 < 0: 
            factor1 = f"(x - {ans1})"
        if ans2 >= 0:
            factor2 = f"(x + {ans2})"
        elif ans2 < 0:
            factor2 = f"(x + {ans2})"
        factor = factor1 + factor2
    return factor 



def APQ(a,b,c):
    p = b/(-2*a)
    q = c - (a*(p**2))
    if a == 1:
        a = None
    elif a == -1:
        a == "-"
    if p >= 0:
        ans1 = f"{a}(x - {p})^2"
    elif p < 0:
        ans2 = f"{a}(x + {p})^2"
    if q >= 0:
        ans2 = f" + {q}"
    elif q < 0:
        ans2 = f" - {q}"
    ans = ans1 + ans2
    return ans
    #y = ax^2+bx+c    y = a(x-p)^2+q

def Com_Int():

assert multidim(1,"Square",4) == 1
assert multidim(1,"Circle",4) == 4.93
assert factor(1,-5,6) == "(x+5)(x+2)"
assert APQ(1,1,1) == "(x + 2)^2 - 3"
assert Com_Int() = 



















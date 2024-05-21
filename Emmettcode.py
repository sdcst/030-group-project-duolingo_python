#sufacearea of a cone
#hypotenuse of a triangle
#area of a icosahedron 
#simplie intest






def SurfaceAreaOfACone():
    r = int(input("Enter the Raduis of Your Cone: "))
    h = int(input("Enter the Height of Your Cone: "))
    if r < 0 :
        print("Enter in a valid povtitve number: ")
    elif h < 0 :
        print("Enter in a valid povtitve number: ")
    elif r > 0 and h > 0:
        A = (3.14159*r*(r + (r**2 + h**2)**0.5))
        A = round(A,2)
        print(f"The surface area of your cone is : {A}")
def HypotenuseOfATriangle(): 
    A = int(input("Enter the A value of Your triangle: "))
    B = int(input("Enter the B value of Your triangle: "))
    if A < 0 :
        print("Enter in a valid povtitve number: ")
    elif B < 0 :
        print("Enter in a valid povtitve number: ")
    elif A > 0 and B > 0:
        C =((A**2 + B**2)**0.5)
        C = round(C,2)
        print(f"The hypotenuse of your triangel is: {C}")
def EdgeOfAIcosahedronUsingVolume(): 
    e = int(input("Enter the Surface area of your icosahedron: "))
    if e < 0 :
        print ("Enter in a valid povtitve number: ")
    elif e > 0:
        E =(((9*e/5)-(3*(5**0.5)*e/5))**(1/3))
        E = round(E,2)
        print(f"The Edge of your icosahedron is : {E}")      
def EdgeOfAIcosahedronUsingSurfaceArea(): 
    e = int(input("Enter the Surface area of your icosahedron: "))
    if e < 0 :
        print ("Enter in a valid povtitve number: ")
    elif e > 0:
        E =((3**0.75)*((e/45)**0.5))
        E = round(E,2)
        print(f"The Edge of your icosahedron is : {E}")
def SurfaceAreaOfAIcosahedron():
    e = int(input("Enter the Edge lengeth of your icosahedron: "))
    if e < 0 :
        print ("Enter in a valid povtitve number: ")
    elif e > 0:
        SA =(5*(3**0.5)*(e**2))
        SA = round(SA,2)
        print(f"The surface area of your icosahedron is : {SA}")
def VolumeOfAIcosahedron():
    e = int(input("Enter the Edge lengeth of your icosahedron: "))
    if e < 0 :
        print ("Enter in a valid povtitve number: ")
    elif e > 0:
        V =(5*(3+(5**0.5))/12)*(e**3)
        V = round(V,2)
        print(f"The volume of your icosahedron is : {V}")
def SimplieInterst():
    P = int(input("Enter the principal amount of Your simple interst: "))
    R = float(input("Enter the rate of interest per Year as a percentence of Your simple interst: "))
    T = int(input("Enter the Time Period involved in months of Your simple interst: "))
    if P < 0 :
        print ("Enter in a valid povtitve number: ")
    elif R < 0 :
        print ("Enter in a valid povtitve number: ")
    elif T < 0 :
        print ("Enter in a valid povtitve number: ")
    elif P > 0 and R > 0 and T > 0:
        p = (R / 100)
        r = (p / 12 )
        A = (P * (1 + r*T))
        A = round(A,2)
        print(f"Your simple intest is : {A}")
def AreaOfAdecagon():
    e = int(input("Enter the length of the side of the dodecagon: "))
    if e < 0 :
        print ("Enter in a valid povtitve number: ")
    elif e > 0:
        V =(3*(2+3**0.5)*(e**2))
        V = round(V,2)
        print(f"The area of your decagon is : {V}")
def VolumeOfAdecagon():
    s = int(input("Enter the length of the side of the dodecagon: "))
    h = int(input("Enter the Height of the column of the dodecagon: "))
    if s < 0 :
        print ("Enter in a valid povtitve number: ")
    if h < 0 :
        print ("Enter in a valid povtitve number: ")
    elif s > 0 and h > 0: 
        V = ((5/2)*(s**2)*(((5+2*(5**0.5))**0.5)*h))
        V = round(V,2)
        print(f"The volume of your decagon is : {V}")
def AlienCivilizationCalculator():
    R = 7
    fp = 0.35
    n = 2.5
    f1 = 0.515
    f2 = 10**-24
    f3 = 0.15
    L = int(input("Enter somewhere between 1000 and 100,000,000 years in which you want to know how many Alien Civilizations may form: "))
    if L < 1000:
        print ("Enter in a valid number between 1000 and 100,000,000: ")
    if L > 100000000:
        print ("Enter in a valid number between 1000 and 100,000,000: ")
    elif L > 1000 and L < 100000000: 
        V = (R*fp*n*f1*f2*f3*L)
        V = round(V,2)
        print(f"The volume of your decagon is : {V}")

AlienCivilizationCalculator()

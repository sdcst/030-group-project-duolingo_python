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

def SurfaceAreaOfAIcosahedron():
    e = int(input("Enter the Edge lengeth of your icosahedron: "))
    if e < 0 :
        print ("Enter in a valid povtitve number: ")
    PAIN = int(input("Would you like the Sufacearea or the Volume of your icosahedron? If you want the volume please enter the number 2. If you want the Surfacearea please enter the number 1: "))
    if PAIN != 1 or PAIN != 2 :
        print ("Enter in a valid number")
    elif e > 0 and PAIN == 1:
        SA =(5*(3**0.5)*(e**2))
        SA = round(SA,2)
        print(f"The surface area of your icosahedron is : {SA}")
    elif e > 0 and PAIN == 2:
        V =(5*(3+(5**0.5))/12)*(e**3)
        V = round(V,2)
        print(f"The volume of your icosahedron is : {V}")

def SimplieIntest():
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




SurfaceAreaOfAIcosahedron()
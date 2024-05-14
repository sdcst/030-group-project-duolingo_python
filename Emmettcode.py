#sufacearea of a cone
#hypotenuse of a triangle
#area of a icosahedron 
#simplie intest






def SurfaceAreaOfACone():
    r = int(input("Enter the Raduis of Your Cone: "))
    h = int(input("Enter the Height of Your Cone: "))
    while r < 0 :
        print("Enter in a valid povtitve number: ")
    while h < 0 :
        print("Enter in a valid povtitve number: ")
    if r > 0 and h > 0:
        A = (3.14159*r*(r + (r**2 + h**2)**0.5))
        A = round(A,2)
        print(f"The surface area of your cone is : {A}")

def HypotenuseOfATriangle(): 
    A = int(input("Enter the A value of Your triangle: "))
    B = int(input("Enter the B value of Your triangle: "))
    while A < 0 :
        print("Enter in a valid povtitve number: ")
    while B < 0 :
        print("Enter in a valid povtitve number: ")
    if A > 0 and B > 0:
        C =((A**2 + B**2)**0.5)
        C = round(C,2)
        print(f"The hypotenuse of your triangel is: {C}")

def SurfaceAreaOfAIcosahedron():
    e = int(input("Enter the Edge lengeth of your icosahedron: "))
    while e < 0 :
        print ("Enter in a valid povtitve number: ")
    PAIN = input("Would you like the Sufacearea or the Volume of your icosahedron? If you want the volume please enter the capital letter V. If you want the Surfacearea please enter capital letter S: ")
    if e > 0 and PAIN == "S":
        SA =(5*(3**0.5)*(e**2))
        SA = round(SA,2)
        print(f"The surface area of your icosahedron is : {SA}")
    elif e > 0 and PAIN == "V":
        V =(5*(3+(5**0.5))/12)*(e**3)
        V = round(V,2)
        print(f"The volume of your icosahedron is : {V}")

HypotenuseOfATriangle()
        

        
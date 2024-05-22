#!python3
# Volume Calculator
# Feel free to rename your variables
import Landon
import Emmettcode

def title():
    print("   ______      __           __      __")
    print("  / ____/___ _/ /______  __/ /___ _/ /_____  _____ TM")
    print(" / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/")
    print("/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    ")
    print("\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/\n\n")
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Landon
    # Modified:
    # title
    return None

def instructions():
    print("Hello! Welcome to the calculator. Please enter a number based on the operation you'd like to use, or press enter to end the program.\n")
    print("*****************************************\n")
    print("Interest:\n -Compound: 1\n -Simple: 2\nPolynomials: \n -Factor a polynomial: 3\n -APQ form: 4")
    print("Geometry:\n -Calculate 'volume' of a multidimensional square or circle: 5\n -Isocehedrons:\n  *Edge using volume: 6\n  *Edge using surface area: 7\n  *Surface area: 8\n  *Volume: 9")
    print(" -Surface area of a cone: 10\n -Hypotenuse of a triangle: 11\n -Area of a dodecagon: 12\nAstro-physics:\n -Number of alien civilizations based on input: 13")
    print("\nTo close the program, press enter.")
    print("\n*****************************************\n")
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Landon
    # Modified:
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    Continue = True
    while Continue != False:
        x = input("Input: ")
        if x == "1":
            Landon.Com_Int()
        if x == "2":
            Emmettcode.SimplieInterst()
        if x == "3":
            Landon.Factor()
        if x == "4":
            Landon.APQ()
        if x == "5":
            Landon.Multidim()
        if x == "6":
            Emmettcode.EdgeOfAIcosahedronUsingVolume()
        if x == "7":
            Emmettcode.EdgeOfAIcosahedronUsingSurfaceArea()
        if x == "8":
            Emmettcode.SurfaceAreaOfAIcosahedron()
        if x == "9":
            Emmettcode.VolumeOfAIcosahedron()
        if x == "10":
            Emmettcode.SurfaceAreaOfACone()
        if x == "11":
            Emmettcode.HypotenuseOfATriangle()
        if x == "12":
            Emmettcode.AreaOfAdecagon()
        if x == "13":
            Emmettcode.AlienCivilizationCalculator()
        if x == "":
            break  


    print("Thankyou for using: ")
    print("   ______      __           __      __")
    print("  / ____/___ _/ /______  __/ /___ _/ /_____  _____ TM")
    print(" / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/")
    print("/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    ")
    print("\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/\n\n")

#if __name__ == "__main__":
#    main()
title()
instructions()
main()
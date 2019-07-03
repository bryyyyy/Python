import math

def main():
    radius = input("What is the radius of the circle? ")
    while radius.isalpha() == True: #check to see if the value input is alphabetical or not
        print("Please enter a number\n")
        radius = input("What is the radius of the circle? ")
    area = math.pi * float(radius)**2
    print(area)
    

    
main()
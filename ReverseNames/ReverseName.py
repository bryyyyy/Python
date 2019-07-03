def main():
    firstName = input("Enter your first name ")
    while firstName.isalpha() == False:
        print("Please use only letters")
        firstName = input("Enter your first name ")    
    lastName = input("Enter your last name ")
    while lastName.isalpha() == False:
        print("Please use only letters")
        firstName = input("Enter your last name ")            
    print(firstName[::-1] + " " + lastName[::-1])
    
main()
    
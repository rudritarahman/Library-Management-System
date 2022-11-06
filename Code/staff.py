def get__staff__info():
    # staff name
    print("\n")
    firstName = input("Enter Your First Name:\t")
    lastName = input("Enter Your Last Name:\t")
    name(firstName, lastName)

    # staff gender
    print("\n")
    print("Press 1 for Male")
    print("Press 2 for Female")
    print("Press 3 for Other")
    staffGender = int(input("Please Choose Your Gender: "))
    sex(staffGender)

    # staff e-mail address
    print("\n")
    staffEmail = input("Enter Your E-mail Address: \t")
    validateEmail(staffEmail)

    # staff e-mail password
    print("\n")
    print("Password shoud have: \n1. At least one capital letter \n2. At least one number \n3. At least one special character \n4. Length of the password should be between 8 and 18")
    password = input("\nEnter Your E-mail Account Password:\t")
    pswd(password) 

    # staff mobile number
    print("\n")
    staffMobileNumber = input("Enter your Mobile Number: \t") # must string; not int
    validateNumber(staffMobileNumber)
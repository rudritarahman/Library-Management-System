def member_info():
    # name
    import re # re module provides support for regular expressions
    #print(dir(re))

    def name(firstName, lastName):
        fullName = firstName + " " + lastName
        #print(fullName)
        validateName(fullName)
            
    regexName = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$'
    def validateName(fullname):
        namePattern = re.compile(regexName, re.IGNORECASE)
        checkName = re.search(namePattern, fullname) # search -> returns a match object if there is a match anywhere in the string
            
        if not checkName: 
            print("\nInvalid Name Syntax!!! \nPlease Use Alphabets Only")
        else:  
            print("\nHello," , fullname)

    # user input name
    firstName = input("\nEnter Your First Name:\t")
    lastName = input("\nEnter Your Last Name:\t")
    name(firstName, lastName)

    # calculate age in years
    from datetime import date # import date class from the datetime module

    def calculateAge(born):
        current = date.today() # date object of today's date
        try: # try -> test a block of code for errors
            birthday = born.replace(year = current.year) # replace() -> change a specified condition with another specified condition
    
        # execute if birth date is February 29 and the current year is not a leap year
        except ValueError: # except -> handle the error
            birthday = born.replace(year = current.year, month = born.month + 1, day = 1) # replace() -> change a specified condition with another specified condition

        if (birthday > current):
            return (current.year - born.year - 1)
        else:
            return (current.year - born.year)

    # user input birth date to get age
    print("\n1: January 2: February 3: March  4: April 5: May 6: June 7: July \n8: August 9: September  10: October 11: November  12: December")
    while True:
        birthYear = int(input("\nEnter Your Birth Year:\t"))
        if(birthYear < 1900 or birthYear > 2021):
            print("\nPlease, re-check your input.")
            continue
        else:
            break

    while True:
        birthMonth = int(input("\nEnter Your Birth Month:\t"))
        if(birthMonth < 1 or birthMonth > 12):
            print("\nPlease, re-check your input.")
            continue
        else:
            break

    while True:
        birthDate = int(input("\nEnter Your Birth Date:\t"))
        if(birthMonth == 1 or birthMonth == 3 or birthMonth == 5 or birthMonth == 7 or birthMonth == 8 or birthMonth == 10 or birthMonth == 12):
            if(birthDate < 1 or birthDate > 31):
                print("\nPlease, re-check your input.")
                continue
            else:
                break
        elif(birthMonth == 4 or birthMonth == 6 or birthMonth == 9 or birthMonth == 11):
            if(birthDate < 1 or birthDate > 30):
                print("\nPlease, re-check your input.")
                continue
            else:
                break
        elif(birthMonth == 2):
            if((birthYear % 4) == 0):
                if((birthYear % 100) == 0):
                    if((birthYear % 400) == 0):
                        #print("{0} is a leap year".format(year))
                        if(birthDate < 1 or birthDate > 29):
                            print("\nPlease, re-check your input.")
                            continue
                        else:
                            break
                    else:
                        #print("{0} is not a leap year".format(year))
                        if(birthDate < 1 or birthDate > 28):
                            print("\nPlease, re-check your input.")
                            continue
                        else:
                            break
                else:
                    #print("{0} is a leap year".format(year))
                    if(birthDate < 1 or birthDate > 29):
                        print("\nPlease, re-check your input.")
                        continue
                    else:
                        break
            else:
            #print("{0} is not a leap year".format(year))
                if(birthDate < 1 or birthDate > 28):
                    print("\nPlease, re-check your input.")
                    continue
                else:
                    break

    print("\nBirth Date: ", str(birthYear), "/", str(birthMonth), "/", str(birthDate))
    age = calculateAge(date(birthYear, birthMonth, birthDate))
    print("\nAge: ", age, "years old")

    # gender information
    print("\nPress 1 for Male")
    print("Press 2 for Female")
    print("Press 3 for Other")

    while True:
        gender = int(input("\nPlease Choose Your Gender: ")) # user input gender
        if(gender != 1 and gender != 2 and gender != 3):
            print("\nPlease choose the correct option.")
            continue
        else:
            if(gender == 1):
                print("\nGender: Male")
                break
            if(gender == 2):
                print("\nGender: Female")
                break
            if(gender == 3):
                print("\nGender: Other")
                break

    # e-mail validation
    import re # re module provides support for regular expressions
    #regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    regexMail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # regular expression for email validation
    while True:
        mail = input("\nEnter Your E-mail Address: \t") # user input e-mail address
        if not (re.search(regexMail, mail)): # search -> returns a match object if there is a match anywhere in the string
            print("\nInvalid E-mail!!! \nPlease Check Again")
            continue
        else:  
            print("\nThank You!")
            break

    # password validation
    regexPass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$" # regular expression for password validation
    def pswd(password):
        pattern = re.compile(regexPass) # compile -> compiling regex
        matchPass = re.search(pattern, password) # search -> searching regex
        if(matchPass):
            print("\nValid Password :)")
        else:
            print("\nInvalid Password :( \nTry Again!")

    # user input password
    print("Password shoud have: \n1. At least one capital letter \n2. At least one number \n3. At least one special character \n4. Length of the password should be between 8 and 18")
    password = input("\nEnter Your Account Password:\t")
    pswd(password)

    # mobile number validation
    regexNum = r"(^(?:\+88|88)?(01[0-9]\d{8})$)" # regular expression for mobile number validation
    while True:
        number = input("\nEnter Your Mobile Number: \t") # user input mobile number
        if not (re.search(regexNum, number)): # search -> returns a match object if there is a match anywhere in the string
            print("\nInvalid Mobile Number!!! \nPlease Check Again")
            continue
        else:  
            print("\nThank You!")
            break
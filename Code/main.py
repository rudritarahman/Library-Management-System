# New Member Registration
def member_info():
    # name
    while True:
        firstName = input("\nEnter Your First Name:\t")
        if firstName.isalpha():
            break
        print("\nPlease Input Alphabets Only")

    while True:
        lastName = input("\nEnter Your Last Name:\t")
        if firstName.isalpha():
            break
        print("\nPlease Input Alphabets Only")

    fullName = firstName + " " + lastName
    print("\nHello!", fullName)

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

# Display Book List
def book_display():
    bookList_dir = "./gdrive/My Drive/CSC101_Project/bookList.txt"
    with open(bookList_dir, "r") as f:
        lines = f.read()
        print(lines)
        print()

# Search Book ISBN (Using Book Title)
#!pip install isbntools 
from isbntools.app import *
def search_isbn(bookTile):
    print("\nPlease Enter the Book Title Properly to Get the ISBN of Your Required Book :)")
    bookTitle = input("\nEnter the Book Title:\t")
    book_isbn = isbn_from_words(bookTitle)
    print("Book Name: ", bookTitle, "\nISBN: ", book_isbn)

# Check Book Information (Using Book ISBN)
#!pip install isbntools
import sys # sys module provides information about constants, functions and methods of the Python interpreter
from isbntools.app import *
def book_info(bookISBN):
    print("Please Enter the Book ISBN-13 or ISBN-10 Properly to Get the Information of Your Required Book. :) \nKeep in mind that if you give ISBN-10 then book information in return you get ISBN-13.")
    bookISBN = input("Enter the Book ISBN:\t")
    print(registry.bibformatters['labels'](meta(bookISBN)))

# Check Book Availabilty in Library (Using Book ISBN)
def book_locator():
    bookISBN_list = [9780425268148, 9781643750255, 9780593136300, 9780385344142, 9780316735735, 9781728232744, 9781501173219, 9781250074133, 9781416590293, 9781616201340, 9781250167026, 9780385527156, 9781487503727, 9781250149060, 9781590515525, 9780062670847, 9780345470614, 9780865478015, 9781616206901, 9780345528681, 9781503215153, 9780385721790, 9780312358334, 9780486280615, 9780307455871,9780224097284, 9780307388995, 9781524763138, 9780062134578, 9781250002532, 9780698411616, 9780802117793, 9781742612829, 9781408800874, 9780241441510, 9780990694977, 9780316010733, 9780099468196, 9780241413210, 9780571276639, 9780743298858, 9780375842207, 9781594483295, 9781250014528, 9780525575238, 9780618593941, 9780312422912, 9781594634734, 9780425252963, 9780312305543, 9780062491794, 9780141040745, 9784130611268, 9780871407771, 9780007342600, 9781501134517, 9780393312836, 9780590557153, 9780099422686, 9781400034710, 9780060560379, 9780679603351, 9780670896769, 9789026349256, 9781908434425, 9780307408877, 9780307743725, 9780345533661, 9780340980934, 9781476798172, 9780099284826, 9780525949978, 9780307474278, 9780060740436, 9780375505294, 9780060957353, 9781786893253, 9781587888144, 9780385346856, 9781481463706, 9781984801487, 9780349142111, 9780460041515, 9780141439846, 9781250012579, 9780735220690, 9781250010124, 9781935554042, 9781501124389, 9780143127550, 9780061782213, 9780140186390, 9780062103222, 9781786486448, 9781473614444, 9780374909819, 9780199537150, 9781473676718, 9781492635222, 9780316260633, 9789036635769, 9780307588371, 9780066620992, 9781728228723, 9781476738918, 9780778308737, 9781524711764, 9780062285539, 9780399103421, 9780375707285, 9780375707285, 9781857990829, 9780062034601, 9781476799407, 9789401471947, 9789463413992, 9780312428549, 9781101971062, 9780062207517, 9781250005144, 9789021676272, 9780375703768, 9781503312753, 9780751554168, 9781250078407, 9780755331420, 9780385021746, 9780385486804, 9780385494786, 9781473217980, 9780670022458, 9780143038092, 9780812976731, 9781779502698, 9780545000109, 9781594631931, 9781473581739, 9781681195919, 9780743261982, 9781788169011, 9781786891686, 9781416589648, 9781509826582, 9780500251652, 9789026125690, 9780062914125, 9781101982266, 9781728215723, 9780316185905, 9780349142135, 9780448060194, 9780593332733, 9781402281945, 9780060518509, 9780143130154, 9780763680886, 9781476756554, 9780553418026, 9780393330342, 9780375704444, 9781400076093, 9789076542935, 9780241338322, 9780345441300, 9780141040080, 9781400078776, 9780061990625, 9780618485222, 9780307388971, 9780385537070, 9781250080400, 9780446520805, 9781481481731, 9781416954132, 9781447201809, 9780141197715, 9780393314366, 9780812996548, 9781416971719, 9789461740021, 9780140177398, 9780141377094, 9780743227445, 9780593101537, 9780307739513, 9780141439686, 9780141442464, 9781932416244, 9781611177220, 9781408418055, 9780307352156, 9781608198085, 9780316098335, 9780804165891, 9780307387899, 9780679781486, 9780312593315, 9780812985429, 9780545846608, 9780307700315, 9780393333091, 9781250207418, 9780142001745, 9780525656159, 97803853487135, 9781400096534, 9780062259318, 9781594485015, 9781250255617, 9781393248507, 9780500014981, 9781400033430, 9781473203280, 9780061769092, 9781596912939, 9789078641322, 9781594483851, 9781400033201, 9781420946888, 9780752881676, 9780316034005, 9780061984037, 9781400032808, 9780307947475, 9781416562603, 9781250130945, 9780307277183, 9780593191415, 9781542017022, 9780307720665, 9780141199085, 9781400078431, 9781635575361, 9781891729225]
    #print(len(bookISBN_list))

    def bookSearch(bookISBN_list, bookSearch_ISBN):
        for i in range (len(bookISBN_list)):
            if (bookISBN_list[i] == bookSearch_ISBN):
                return True
        return False

    # user input book ISBN
    while True:
        bookISBN = int(input("\nEnter Book ISBN:\t"))
        if not (bookSearch(bookISBN_list, bookISBN)):
            print("\nSorry, the book is unavailable in the library.")
            continue
        else:
            print("\nThe book is available in the library. \nDo you want to borrow this book?")
            break

# Borrow Book
def borrow_book():
    from datetime import datetime
    current = datetime.now() # current date and time

    date_time = current.strftime("%d/%m/%Y, %H:%M:%S")

    while True:
        firstName = input("\nEnter Your First Name:\t")
        if firstName.isalpha():
            break
        print("\nPlease Input Alphabets Only")

    while True:
        lastName = input("Enter Your Last Name:\t")
        if firstName.isalpha():
            break
        print("\nPlease Input Alphabets Only")

    fullName = firstName + " " + lastName

    #bookISBN_list = [9780425268148, 9781643750255, 9780593136300, 9780385344142, 9780316735735, 9781728232744, 9781501173219, 9781250074133, 9781416590293, 9781616201340, 9781250167026, 9780385527156, 9781487503727, 9781250149060, 9781590515525, 9780062670847, 9780345470614, 9780865478015, 9781616206901, 9780345528681, 9781503215153, 9780385721790, 9780312358334, 9780486280615, 9780307455871,9780224097284, 9780307388995, 9781524763138, 9780062134578, 9781250002532, 9780698411616, 9780802117793, 9781742612829, 9781408800874, 9780241441510, 9780990694977, 9780316010733, 9780099468196, 9780241413210, 9780571276639, 9780743298858, 9780375842207, 9781594483295, 9781250014528, 9780525575238, 9780618593941, 9780312422912, 9781594634734, 9780425252963, 9780312305543, 9780062491794, 9780141040745, 9784130611268, 9780871407771, 9780007342600, 9781501134517, 9780393312836, 9780590557153, 9780099422686, 9781400034710, 9780060560379, 9780679603351, 9780670896769, 9789026349256, 9781908434425, 9780307408877, 9780307743725, 9780345533661, 9780340980934, 9781476798172, 9780099284826, 9780525949978, 9780307474278, 9780060740436, 9780375505294, 9780060957353, 9781786893253, 9781587888144, 9780385346856, 9781481463706, 9781984801487, 9780349142111, 9780460041515, 9780141439846, 9781250012579, 9780735220690, 9781250010124, 9781935554042, 9781501124389, 9780143127550, 9780061782213, 9780140186390, 9780062103222, 9781786486448, 9781473614444, 9780374909819, 9780199537150, 9781473676718, 9781492635222, 9780316260633, 9789036635769, 9780307588371, 9780066620992, 9781728228723, 9781476738918, 9780778308737, 9781524711764, 9780062285539, 9780399103421, 9780375707285, 9780375707285, 9781857990829, 9780062034601, 9781476799407, 9789401471947, 9789463413992, 9780312428549, 9781101971062, 9780062207517, 9781250005144, 9789021676272, 9780375703768, 9781503312753, 9780751554168, 9781250078407, 9780755331420, 9780385021746, 9780385486804, 9780385494786, 9781473217980, 9780670022458, 9780143038092, 9780812976731, 9781779502698, 9780545000109, 9781594631931, 9781473581739, 9781681195919, 9780743261982, 9781788169011, 9781786891686, 9781416589648, 9781509826582, 9780500251652, 9789026125690, 9780062914125, 9781101982266, 9781728215723, 9780316185905, 9780349142135, 9780448060194, 9780593332733, 9781402281945, 9780060518509, 9780143130154, 9780763680886, 9781476756554, 9780553418026, 9780393330342, 9780375704444, 9781400076093, 9789076542935, 9780241338322, 9780345441300, 9780141040080, 9781400078776, 9780061990625, 9780618485222, 9780307388971, 9780385537070, 9781250080400, 9780446520805, 9781481481731, 9781416954132, 9781447201809, 9780141197715, 9780393314366, 9780812996548, 9781416971719, 9789461740021, 9780140177398, 9780141377094, 9780743227445, 9780593101537, 9780307739513, 9780141439686, 9780141442464, 9781932416244, 9781611177220, 9781408418055, 9780307352156, 9781608198085, 9780316098335, 9780804165891, 9780307387899, 9780679781486, 9780312593315, 9780812985429, 9780545846608, 9780307700315, 9780393333091, 9781250207418, 9780142001745, 9780525656159, 97803853487135, 9781400096534, 9780062259318, 9781594485015, 9781250255617, 9781393248507, 9780500014981, 9781400033430, 9781473203280, 9780061769092, 9781596912939, 9789078641322, 9781594483851, 9781400033201, 9781420946888, 9780752881676, 9780316034005, 9780061984037, 9781400032808, 9780307947475, 9781416562603, 9781250130945, 9780307277183, 9780593191415, 9781542017022, 9780307720665, 9780141199085, 9781400078431, 9781635575361, 9781891729225]
    borrowBook_list = []

    print("\nWhich book do you want to borrow? You can borrow 5 books at a time.")
    bookNum_Borrow = int(input("How many books do you want to borrow? "))
    for i in range (bookNum_Borrow):
        borrowBook_ISBN = input("\nPlease, Enter Book ISBN:\t")
        borrowBook_list.append(borrowBook_ISBN)
        
    print("\nDate & Time: ", date_time) # dd/mm/YY, hour: minute: second format
    print("Borrower Name: ", fullName)
    print("Borrow Book List: ", borrowBook_list)

# Return Book
def return_book():
    from datetime import datetime
    current = datetime.now() # current date and time

    date_time = current.strftime("%d/%m/%Y, %H:%M:%S")

    while True:
        firstName = input("\nEnter Your First Name:\t")
        if firstName.isalpha():
            break
        print("\nPlease Input Alphabets Only")

    while True:
        lastName = input("Enter Your Last Name:\t")
        if firstName.isalpha():
            break
        print("\nPlease Input Alphabets Only")

    fullName = firstName + " " + lastName

    returnBook_list = []
    bookNum_Return = int(input("\nHow many books do you want to return?\t"))
    for i in range (bookNum_Return):
        returnBook_ISBN = input("\nPlease, Enter Book ISBN:\t")
        returnBook_list.append(returnBook_ISBN)
    
    lateReturn = input("\nReturning book late? \nIf YES Press 1 \nIf NO Press 0 \n")
    if(lateReturn == "1"):
        delayDay_Num = int(input("\nDelay for how many days?\t"))
        delayFine = ((10 * delayDay_Num) * bookNum_Return)
        print("\nDate & Time: ", date_time) # dd/mm/YY, hour: minute: second format
        print("Borrower Name: ", fullName)
        print("Borrow Book List: ", returnBook_list)
        print("Late Return Fine: ", delayFine, "Taka")
    else:
        print("\nDate & Time: ", date_time) # dd/mm/YY, hour: minute: second format
        print("Borrower Name: ", fullName)
        print("Borrow Book List: ", returnBook_list)
        print("\nThank You!!! Come Again :)")

# Book Management Menu (Only Allowed for Library Authority & Staff)
def manage_book():
    identify_person = input("\nThis system is only allowed for Library Authority & Staff. Do you belong any one of those? \nIf YES Press 1 \nIf No Press 0 \n")
    if(identify_person == "1"):
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

        # extract ISBN from book list
        def extract_isbn():
            string = input("\nEnter Book List to Extract Book ISBN:\t")
            numbers = []
            for word in string.split(): # string.split() -> to split string into a list of words
                if(word.isdigit()): # word.isdigit() -> each word as string to check if it is a digit
                    numbers.append(int(word)) # list.append(object) -> the integer as object to append it to an output list
            print(numbers)

        # add new book in the book ISBN list
        def add_book():
            bookISBN_list = [9780425268148, 9781643750255, 9780593136300, 9780385344142, 9780316735735, 9781728232744, 9781501173219, 9781250074133, 9781416590293, 9781616201340, 9781250167026, 9780385527156, 9781487503727, 9781250149060, 9781590515525, 9780062670847, 9780345470614, 9780865478015, 9781616206901, 9780345528681, 9781503215153, 9780385721790, 9780312358334, 9780486280615, 9780307455871,9780224097284, 9780307388995, 9781524763138, 9780062134578, 9781250002532, 9780698411616, 9780802117793, 9781742612829, 9781408800874, 9780241441510, 9780990694977, 9780316010733, 9780099468196, 9780241413210, 9780571276639, 9780743298858, 9780375842207, 9781594483295, 9781250014528, 9780525575238, 9780618593941, 9780312422912, 9781594634734, 9780425252963, 9780312305543, 9780062491794, 9780141040745, 9784130611268, 9780871407771, 9780007342600, 9781501134517, 9780393312836, 9780590557153, 9780099422686, 9781400034710, 9780060560379, 9780679603351, 9780670896769, 9789026349256, 9781908434425, 9780307408877, 9780307743725, 9780345533661, 9780340980934, 9781476798172, 9780099284826, 9780525949978, 9780307474278, 9780060740436, 9780375505294, 9780060957353, 9781786893253, 9781587888144, 9780385346856, 9781481463706, 9781984801487, 9780349142111, 9780460041515, 9780141439846, 9781250012579, 9780735220690, 9781250010124, 9781935554042, 9781501124389, 9780143127550, 9780061782213, 9780140186390, 9780062103222, 9781786486448, 9781473614444, 9780374909819, 9780199537150, 9781473676718, 9781492635222, 9780316260633, 9789036635769, 9780307588371, 9780066620992, 9781728228723, 9781476738918, 9780778308737, 9781524711764, 9780062285539, 9780399103421, 9780375707285, 9780375707285, 9781857990829, 9780062034601, 9781476799407, 9789401471947, 9789463413992, 9780312428549, 9781101971062, 9780062207517, 9781250005144, 9789021676272, 9780375703768, 9781503312753, 9780751554168, 9781250078407, 9780755331420, 9780385021746, 9780385486804, 9780385494786, 9781473217980, 9780670022458, 9780143038092, 9780812976731, 9781779502698, 9780545000109, 9781594631931, 9781473581739, 9781681195919, 9780743261982, 9781788169011, 9781786891686, 9781416589648, 9781509826582, 9780500251652, 9789026125690, 9780062914125, 9781101982266, 9781728215723, 9780316185905, 9780349142135, 9780448060194, 9780593332733, 9781402281945, 9780060518509, 9780143130154, 9780763680886, 9781476756554, 9780553418026, 9780393330342, 9780375704444, 9781400076093, 9789076542935, 9780241338322, 9780345441300, 9780141040080, 9781400078776, 9780061990625, 9780618485222, 9780307388971, 9780385537070, 9781250080400, 9780446520805, 9781481481731, 9781416954132, 9781447201809, 9780141197715, 9780393314366, 9780812996548, 9781416971719, 9789461740021, 9780140177398, 9780141377094, 9780743227445, 9780593101537, 9780307739513, 9780141439686, 9780141442464, 9781932416244, 9781611177220, 9781408418055, 9780307352156, 9781608198085, 9780316098335, 9780804165891, 9780307387899, 9780679781486, 9780312593315, 9780812985429, 9780545846608, 9780307700315, 9780393333091, 9781250207418, 9780142001745, 9780525656159, 97803853487135, 9781400096534, 9780062259318, 9781594485015, 9781250255617, 9781393248507, 9780500014981, 9781400033430, 9781473203280, 9780061769092, 9781596912939, 9789078641322, 9781594483851, 9781400033201, 9781420946888, 9780752881676, 9780316034005, 9780061984037, 9781400032808, 9780307947475, 9781416562603, 9781250130945, 9780307277183, 9780593191415, 9781542017022, 9780307720665, 9780141199085, 9781400078431, 9781635575361, 9781891729225]
            addBook_list = int(input("\nEnter Book ISBN to Add in the List:\t"))
            bookISBN_list.append(addBook_list) # list.append() -> add element in of the list
            updatedISBN_list = bookISBN_list.copy() # list.copy() -> copy list elements one to another
            print("Updated Book ISBN List: ", updatedISBN_list)

        # remove book from the book ISBN list
        def remove_book():
            bookISBN_list = [9780425268148, 9781643750255, 9780593136300, 9780385344142, 9780316735735, 9781728232744, 9781501173219, 9781250074133, 9781416590293, 9781616201340, 9781250167026, 9780385527156, 9781487503727, 9781250149060, 9781590515525, 9780062670847, 9780345470614, 9780865478015, 9781616206901, 9780345528681, 9781503215153, 9780385721790, 9780312358334, 9780486280615, 9780307455871,9780224097284, 9780307388995, 9781524763138, 9780062134578, 9781250002532, 9780698411616, 9780802117793, 9781742612829, 9781408800874, 9780241441510, 9780990694977, 9780316010733, 9780099468196, 9780241413210, 9780571276639, 9780743298858, 9780375842207, 9781594483295, 9781250014528, 9780525575238, 9780618593941, 9780312422912, 9781594634734, 9780425252963, 9780312305543, 9780062491794, 9780141040745, 9784130611268, 9780871407771, 9780007342600, 9781501134517, 9780393312836, 9780590557153, 9780099422686, 9781400034710, 9780060560379, 9780679603351, 9780670896769, 9789026349256, 9781908434425, 9780307408877, 9780307743725, 9780345533661, 9780340980934, 9781476798172, 9780099284826, 9780525949978, 9780307474278, 9780060740436, 9780375505294, 9780060957353, 9781786893253, 9781587888144, 9780385346856, 9781481463706, 9781984801487, 9780349142111, 9780460041515, 9780141439846, 9781250012579, 9780735220690, 9781250010124, 9781935554042, 9781501124389, 9780143127550, 9780061782213, 9780140186390, 9780062103222, 9781786486448, 9781473614444, 9780374909819, 9780199537150, 9781473676718, 9781492635222, 9780316260633, 9789036635769, 9780307588371, 9780066620992, 9781728228723, 9781476738918, 9780778308737, 9781524711764, 9780062285539, 9780399103421, 9780375707285, 9780375707285, 9781857990829, 9780062034601, 9781476799407, 9789401471947, 9789463413992, 9780312428549, 9781101971062, 9780062207517, 9781250005144, 9789021676272, 9780375703768, 9781503312753, 9780751554168, 9781250078407, 9780755331420, 9780385021746, 9780385486804, 9780385494786, 9781473217980, 9780670022458, 9780143038092, 9780812976731, 9781779502698, 9780545000109, 9781594631931, 9781473581739, 9781681195919, 9780743261982, 9781788169011, 9781786891686, 9781416589648, 9781509826582, 9780500251652, 9789026125690, 9780062914125, 9781101982266, 9781728215723, 9780316185905, 9780349142135, 9780448060194, 9780593332733, 9781402281945, 9780060518509, 9780143130154, 9780763680886, 9781476756554, 9780553418026, 9780393330342, 9780375704444, 9781400076093, 9789076542935, 9780241338322, 9780345441300, 9780141040080, 9781400078776, 9780061990625, 9780618485222, 9780307388971, 9780385537070, 9781250080400, 9780446520805, 9781481481731, 9781416954132, 9781447201809, 9780141197715, 9780393314366, 9780812996548, 9781416971719, 9789461740021, 9780140177398, 9780141377094, 9780743227445, 9780593101537, 9780307739513, 9780141439686, 9780141442464, 9781932416244, 9781611177220, 9781408418055, 9780307352156, 9781608198085, 9780316098335, 9780804165891, 9780307387899, 9780679781486, 9780312593315, 9780812985429, 9780545846608, 9780307700315, 9780393333091, 9781250207418, 9780142001745, 9780525656159, 97803853487135, 9781400096534, 9780062259318, 9781594485015, 9781250255617, 9781393248507, 9780500014981, 9781400033430, 9781473203280, 9780061769092, 9781596912939, 9789078641322, 9781594483851, 9781400033201, 9781420946888, 9780752881676, 9780316034005, 9780061984037, 9781400032808, 9780307947475, 9781416562603, 9781250130945, 9780307277183, 9780593191415, 9781542017022, 9780307720665, 9780141199085, 9781400078431, 9781635575361, 9781891729225]
            removeBook_list = int(input("\nEnter Book ISBN to Remove from the List:\t"))
            bookISBN_list.remove(removeBook_list)
            newISBN_list = bookISBN_list.copy()
            print("Updated Book ISBN List: ", newISBN_list)

        def validBook_menu():
            bookManage_Options = ["1", "2", "3", "exit", "Exit", "eXit", "exIt", "exiT", "EXit", "EXIt", "EXIT"]
            while True:
                book_choices = input("\nPlease Select from the Following Menu: \n"
                                  " 1. Extract ISBN from Book List \n"
                                  " 2. Add New Book in the Book ISBN List \n"
                                  " 3. Remove Book from the Book ISBN List \n"
                                  "\nType exit to Leave the Program \n"
                                  "\nEnter Your Choice: ")

                if book_choices in bookManage_Options:
                    if(book_choices == "exit" or "Exit" or "eXit" or "exIt" or "exiT" or "EXit" or "EXIt" or "EXIT"):
                        print("\nThank you for using library management system.")
                        break
                    else:
                        continue
                else:
                    print("\nPlease, Choose Option from the Given Menu.")
                    continue

            return book_choices

        def bookListManage_Calls():
                book_choices = validBook_menu()
                if(book_choices == '1'):
                    extract_isbn()
                elif(book_choices == '2'):
                    add_book()
                elif(book_choices == '3'):
                    remove_book()

        bookListManage_Calls()    
    else:
        print("Sorry, you are not allowed.")

manage_book()

# Staff ID Registration
def staff_info():
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

    # designation
    while True:
        designation = input("\nPlease Enter What's Your Designation:\t")
        if designation.isalpha():
            break
        print("\nPlease Input Alphabets Only")

# Main Menu
def validate_menu():
    message = print("\nWelcome to the Library Management System. \n")
    valid_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "exit", "Exit", "eXit", "exIt", "exiT", "EXit", "EXIt", "EXIT"]

    while True:
        choices = input("\nPlease Select from the Following Menu: \n"
                          " 1. New Member Registration \n"
                          " 2. Display Book List \n"
                          " 3. Search Book ISBN (Using Book Title) \n"
                          " 4. Check Book Information (Using Book ISBN) \n"
                          " 5. Check Book Availabilty in Library (Using Book ISBN) \n"
                          " 6. Borrow Book \n"
                          " 7. Return Book \n"
                          " 8. Book Management Menu (Only Allowed for Library Authority & Staff) \n"
                          " 9. Staff Member Registration \n"
                          "\nType exit to Leave the Program \n"
                          "\nEnter Your Choice: ")
            
        if choices in valid_options:
            if(choices == "exit" or "Exit" or "eXit" or "exIt" or "exiT" or "EXit" or "EXIt" or "EXIT"):
                print("\nThank you for using library management system.")
                break
            else:
                continue
        else:
            print("\nPlease, Choose Option from the Given Menu.")
            continue
                          
    return choices

def selection_calls():
        choices = validate_menu()
        if(choices == '1'):
            member_info()
        elif(choices == '2'):
            book_display()
        elif(choices == '3'):
            search_isbn(bookTile ="")
        elif(choices == '4'):
            book_info(bookISBN = "")
        elif(choices == '5'):
            book_locator()
        elif(choices == '6'):
            borrow_book()
        elif(choices == '7'):
            return_book()
        elif(choices == '8'):
            manage_book()
        elif(choices == '9'):
            staff_info()

selection_calls()
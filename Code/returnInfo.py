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
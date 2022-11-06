import member
import staff

member.get__member__info()
staff.get__staff__info()

import re # re module provides support for regular expressions
#print(dir(re))
from datetime import date # import date class from the datetime module

# name  
def name(firstName, lastName):
  fullName = firstName + " " + lastName
  #print(fullName)
  validateName(fullName) 

def validateName(fullname):
  regexName = r'^([a-z]+)( [a-z]+)*( [a-z]+)*$'

  namePattern = re.compile(regexName, re.IGNORECASE)
  checkName = re.search(namePattern, fullname)
  
  if(checkName): # search -> returns a match object if there is a match anywhere in the string
    print("Hello," , fullname)  
  else:  
    print("Invalid Name Syntax!!! \nPlease Use Alphabets Only")

# calculate age in years
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

# gender information
def sex(gender):
  if(gender == 1):
    print("Gender: Male")
  elif(gender == 2):
    print("Gender: Female")
  elif(gender == 3):
    print("Gender: Other")
  else:
    print("Please choose the correct option.")

# e-mail validation
#regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def validateEmail(mail):  
  regexMail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # regular expression for email validation

  if(re.search(regexMail, mail)): # search -> returns a match object if there is a match anywhere in the string
    print("Thank You!")  
  else:  
    print("Invalid E-mail!!! \nPlease Check Again") 

# mobile number validation
def validateNumber(number):
  regexNum = r"(^(?:\+88|88)?(01[0-9]\d{8})$)" # regular expression for mobile number validation

  if(re.search(regexNum, number)): # search -> returns a match object if there is a match anywhere in the string
    print("Thank You!")  
  else:  
    print("Invalid Mobile Number!!! \nPlease Check Again")

# password validation
def pswd(password):
  regexPass = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$" # regular expression for password validation

  pattern = re.compile(regexPass) # compile -> compiling regex
  
  matchPass = re.search(pattern, password) # search -> searching regex

  if(matchPass):
    print("Valid Password :)")
  else:
    print("Invalid Password :( \nTry Again!")
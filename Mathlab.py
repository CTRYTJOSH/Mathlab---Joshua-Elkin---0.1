import random
import csv
import os
def ensure_csv_exists():
    if not os.path.exists("Mathlab.csv"):
        with open("Mathlab.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Password", "Normal","Hardcore"])
def login ():
    ensure_csv_exists()
    print("_____________________________________________________________________________________________________")
    print("")
    print("███╗   ███╗ █████╗ ████████╗██╗  ██╗██╗      █████╗ ██████╗ ██╗")
    print("████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██║     ██╔══██╗██╔══██╗██║")
    print("██╔████╔██║███████║   ██║   ███████║██║     ███████║██████╔╝██║")
    print("██║╚██╔╝██║██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██╗╚═╝")
    print("██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████╗██║  ██║██████╔╝██╗")
    print("╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝")                                                         
    print("_____________________________________________________________________________________________________")
    print("")
    print ("Please Login In")
    global username
    global password
    create = input("Do you have a Mathlab account (yes or no)? ")
    create = create.lower()
    if create in ["yes", "y"]:
      username = input("Username(Case Senstive): ")
      password = input("Password(Case Senstive): ")

      with open('Mathlab.csv', mode='r', newline='') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        
        for lines in csvFile:
            if len(lines) >= 2:
                if username == lines[0] and password == lines[1]:
                    print(f"Welcome {username}")
                    menu()
                    return  
        
        print("Incorrect Username or Password\nTry Again")
        login()  
    else:
      create_account()     
def create_account ():
    print("")
    account = input("Would you like to create a account? (yes or no)")
    account = account.lower()
    print("")

    if account in ['yes','y']:
        username = input("Username(Case Senstive): ")
        password = input("Password(Case Senstive): ") 
        existing_usernames = []
        with open("Mathlab.csv", 'r', newline='') as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    if row and len(row) > 0:
                        existing_usernames.append(row[0])     
        if username in existing_usernames:
            num = 1
            while f"{username}{num}" in existing_usernames:
                num += 1
            username = f"{username}{num}"
        with open("Mathlab.csv", 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([username, password])
        print("Done!")
        print(f"Your Username is: {username}")
        print(f'Your Password is: {password}')
        print("")
        login()
    elif account in ['no','n']:
        login()
        print("")
    else:
        print("Please enter yes or no")
        create_account()
        print("")
def menu():
    print("_____________________________________________________________________________________________________")
    print("")
    print("███╗   ███╗███████╗███╗   ██╗██╗   ██╗██╗")
    print("████╗ ████║██╔════╝████╗  ██║██║   ██║██║")
    print("██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║██║")
    print("██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║╚═╝")
    print("██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝██╗")
    print("╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    print("What Would you like to do?")
    print("")
    print("Calculator")
    print("Triangle Finder")
    print("Times Table Quiz")
    print("Exit App")
    print("")
    program = input("What do you want to use? ")
    program = program.lower()
    if program in ['calculator', 'c']:
        calculator()
    elif program in ['triangle finder', 't']:
        triangle()
    elif program in ['times table quiz', 'q']:
        quiz()
    elif program in ['exit app','exit','e']:
        exit()
    else:
        menu_fail()
def menu_fail():
    print("")
    print("Please enter one of the following:")
    print("Calculator")
    print("Triangle Finder")
    print("Times Table Quiz")
    print("Exit App")
    print("")
    program = input("What do you want to use? ")
    program = program.lower()
    if program in ['calculator', 'c']:
        calculator()
    elif program in ['triangle finder', 't']:
        triangle()
    elif program in ['times table quiz', 'q']:
        quiz()
    elif program in ['exit app','exit','e']:
        exit()
    else:
        menu_fail()
def calculator(): 
    print("")
    print("_____________________________________________________________________________________________________")
    print("")
    print(" ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ██╗")
    print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██║")
    print("██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝██║")
    print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗╚═╝")
    print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║██╗")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    operation = input("What operation do you want (plus, minus, multiply, divide)? ")
    operation = operation.lower()
    if operation in ['+', 'plus']:
        plus()
        print("")
    elif operation in ['-', 'minus']:
        minus()
        print("")
    elif operation in ['*','multiply']:
        multiply()
        print("")
    elif operation in ['/', 'divide']:
        divide()
        print("")
    else:
        calculator_fail()
        print("")
def calculator_fail():
    print("Please enter a valid input")
    operation = input("What operation do you want (plus, minus, multiply, divide)? ")
    operation = operation.lower()
    if operation in ['+', 'plus']:
        plus()
        print("")
    elif operation in ['-', 'minus']:
        minus()
        print("")
    elif operation in ['*','multiply']:
        multiply()
        print("")
    elif operation in ['/', 'divide']:
        divide()
        print("")
    else:
        calculator_fail()
        print("")
def returnC():
    returnA = input("Would you like to return to the menu(yes or no)? ")
    returnA = returnA.lower()
    if returnA in ['yes','y']: 
        menu()
        print("")
    elif returnA in ['no','n']:
        calculator()
        print("")
    else:
        print("Please enter yes or no")
        returnC()
        print("")
def returnT():
    returnA = input("Would you like to return to the menu(yes or no)? ")
    returnA = returnA.lower()
    if returnA in ['yes','y']: 
        menu()
        print("")
    elif returnA in ['no','n']:
        triangle()
        print("")
    else:
        print("Please enter yes or no")
        returnT()
        print("")
def returnTable():
    returnA = input("Would you like to return to the menu(yes or no)? ")
    returnA = returnA.lower()
    if returnA in ['yes','y']: 
        menu()
        print("")
    elif returnA in ['no','n']:
        quiz()
        print("")
    else:
        print("Please enter yes or no")
        returnTable()
        print("")
def plus():
    print("_____________________________________________________________________________________________________")
    print("")
    print("██████╗ ██╗     ██╗   ██╗███████╗██╗")
    print("██╔══██╗██║     ██║   ██║██╔════╝██║")
    print("██████╔╝██║     ██║   ██║███████╗██║")
    print("██╔═══╝ ██║     ██║   ██║╚════██║╚═╝")
    print("██║     ███████╗╚██████╔╝███████║██╗")
    print("╚═╝     ╚══════╝ ╚═════╝ ╚══════╝╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    while True:
      try:
        NumA = float(input("Please enter a number: "))
        NumB = float(input("Please enter a number: "))
        NumA = NumA + NumB
        print(f"The Answer is {NumA}")
        wait = input("type anything to exit")
        wait = wait.lower()
        if wait == '':
          print("")
          plus()
        else:
          print("")
          returnC()
      except:
        print("Invalid input. Please enter numbers only.")
        plus()
def multiply():
    print("_____________________________________________________________________________________________________")
    print("")
    print("███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗  ██╗   ██╗██╗")
    print("████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║  ╚██╗ ██╔╝██║")
    print("██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║   ╚████╔╝ ██║")
    print("██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║    ╚██╔╝  ╚═╝")
    print("██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗██║   ██╗")
    print("╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚═╝   ╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    while True:
      try:
        NumA = float(input("Please enter a number: "))
        NumB = float(input("Please enter a number: "))
        NumA = NumA * NumB
        print(f"The Answer is {NumA}")
        wait = input("type anything to exit")
        wait = wait.lower()
        if wait == '':
          print("")
          multiply()
        else:
          print("")
          returnC()
      except:
          print("Invalid input. Please enter numbers only.")
          multiply()
def minus():
    print("_____________________________________________________________________________________________________")
    print("")
    print("███╗   ███╗██╗███╗   ██╗██╗   ██╗███████╗██╗")
    print("████╗ ████║██║████╗  ██║██║   ██║██╔════╝██║")
    print("██╔████╔██║██║██╔██╗ ██║██║   ██║███████╗██║")
    print("██║╚██╔╝██║██║██║╚██╗██║██║   ██║╚════██║╚═╝")
    print("██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝███████║██╗")
    print("╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    while True:
      try:
        NumA = float(input("Please enter a number: "))
        NumB = float(input("Please enter a number: "))
        if NumA > NumB:
            NumA = NumA - NumB
        elif NumA == NumB:
            NumA = NumA - NumB
        else:
            NumA = NumB - NumA
        print(f"The Answer is {NumA}")
        wait = input("type anything to exit")
        wait = wait.lower()
        if wait == '':
            print("")
            minus()
        else:
            print("")
            returnC()
      except:
        print("Invalid input. Please enter numbers only.")
        minus()         
def divide():
    print("_____________________________________________________________________________________________________")
    print("")
    print("██████╗ ██╗██╗   ██╗██╗██████╗ ███████╗██╗")
    print("██╔══██╗██║██║   ██║██║██╔══██╗██╔════╝██║")
    print("██║  ██║██║██║   ██║██║██║  ██║█████╗  ██║")
    print("██║  ██║██║╚██╗ ██╔╝██║██║  ██║██╔══╝  ╚═╝")
    print("██████╔╝██║ ╚████╔╝ ██║██████╔╝███████╗██╗")
    print("╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚═════╝ ╚══════╝╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    while True:
      try:
        NumA = float(input("Please enter a number: "))
        NumB = float(input("Please enter a number: "))
        if NumA > NumB:
            NumA = NumA / NumB
        elif NumA == NumB:
             NumA = NumA / NumB
        else:
            NumA = NumB / NumA

        print(f"The Answer is {NumA}")
        wait = input("type anything to exit")
        wait = wait.lower()
        if wait == '':
            print("")
            divide()
        else:
            print("")
            returnC()
      except:
          print("Invalid input. Please enter numbers only.")
          divide()
def triangle():
    print("_____________________________________________________________________________________________________")
    print("")
    print(" ███████╗██████╗ ██╗ █████╗ ███╗   ██╗ ██████╗ ██╗     ███████╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ ██╗")
    print("╚══██╔══╝██╔══██╗██║██╔══██╗████╗  ██║██╔════╝ ██║     ██╔════╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗██║")
    print("   ██║   ██████╔╝██║███████║██╔██╗ ██║██║  ███╗██║     █████╗      █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝██║")
    print("   ██║   ██╔══██╗██║██╔══██║██║╚██╗██║██║   ██║██║     ██╔══╝      ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗╚═╝")
    print("   ██║   ██║  ██║██║██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║██╗")
    print("   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")
    global SideA
    global SideB
    global SideC
    SideA = 0
    SideB = 0
    SideC = 0
    try:
        SideA = float(input("Please enter a number for one of the sides: "))
        SideB = float(input("Please enter a number for one of the sides: "))
        SideC = float(input("Please enter a number for one of the sides: "))
        if SideA < 1 or SideB < 1 or SideC < 1:
            print("Please enter number above 1")
            triangle()
        valid_triangle(SideA,SideB,SideC)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        triangle()    
def valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        calculate_triangle()
    else:
        print("Please try again")
        triangle()
def calculate_triangle():
    if SideA == SideB == SideC:
        print("You got a equalateral")
    elif SideA == SideB != SideC or SideB == SideC != SideA or SideC == SideA != SideB:
        print("You got a Isosceles")
    elif SideA**2 + SideB**2 == SideC**2 or SideB**2 + SideC**2 == SideA**2 or SideC**2 + SideA**2 == SideB**2:
        print("You got a Right Angle")
    else:
        print("You got a Scalene")
    print("")
    wait = input("type anything to exit")
    wait = wait.lower()
    if wait == '':
        print("")
        triangle()
    else:
        print("")
        returnT()
def quiz():
    print("______________________________________________________________________________________________________________________________")
    print("")
    print("████████╗██╗███╗   ███╗███████╗███████╗    ████████╗ █████╗ ██████╗ ██╗     ███████╗     ██████╗ ██╗   ██╗██╗███████╗██╗")
    print("╚══██╔══╝██║████╗ ████║██╔════╝██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝██║")
    print("   ██║   ██║██╔████╔██║█████╗  ███████╗       ██║   ███████║██████╔╝██║     █████╗      ██║   ██║██║   ██║██║  ███╔╝ ██║")
    print("   ██║   ██║██║╚██╔╝██║██╔══╝  ╚════██║       ██║   ██╔══██║██╔══██╗██║     ██╔══╝      ██║▄▄ ██║██║   ██║██║ ███╔╝  ╚═╝")
    print("   ██║   ██║██║ ╚═╝ ██║███████╗███████║       ██║   ██║  ██║██████╔╝███████╗███████╗    ╚██████╔╝╚██████╔╝██║███████╗██╗")
    print("   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝")
    print("_____________________________________________________________________________________________________________________________")
    print("")
    def read_csv():
        users = {}
        try:
            with open("Mathlab.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    username = row.get("Username", "Unknown")
                    normal_score = row.get("Normal", "No Score")
                    users[username] = normal_score
        except FileNotFoundError:
            print("CSV file not found.")
        return users 
    users = read_csv()
    print("What would u like to do?")
    print("Start The Quiz")
    print("View High Score")
    print("Go Back to Menu")
    print("")
    start = input("What would You like to do? ")
    start = start.lower()
    if start in ["start the quiz", "start"]:
        Go()
    elif start in ["go back to menu", "menu"]:
        returnTable()
    elif start == "pain":
        hardcore()
    elif start in ["view high score", "hs"]:
        print(f"Your High score is: {users[username]}")
        print("")
        wait = input("Press enter to contiue")
        wait = wait.lower()
        if wait == 'yes':
            quiz()
        else:
            quiz()
    else:
        print("Please enter a valid input")
        quiz()
def hardcore():
    print("_____________________________________________________________________________________________________")
    print("")
    print("███████╗ █████╗ ███████╗████████╗███████╗██████╗     ███████╗ ██████╗  ██████╗ ██╗")
    print("██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██╔════╝ ██╔════╝ ██║")
    print("█████╗  ███████║███████╗   ██║   █████╗  ██████╔╝    █████╗  ██║  ███╗██║  ███╗██║")
    print("██╔══╝  ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██║   ██║╚═╝")
    print("███████╗██║  ██║███████║   ██║   ███████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝██╗")
    print("╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝")
    print("_____________________________________________________________________________________________________")
    print("")                                                                             
    points = 0
    pain = random.randint(50,400)
    for i in range(pain+1):
      RanA = random.randint(1,12)
      RanB = random.randint(1,12)
      RanC = RanA*RanB
      while True:
        try: 
          answer = int(input(f"{RanA} X {RanB} = ")) 
          break
        except:
          print("please enter a number")
          
      if answer == RanC:
         print("Correct!")
         points = points + 1
      else: 
        print("Wrong :(")    
    percentage = points / 10 * 100
    print(f"You got {percentage}%")
    updated = False
    rows = []
    header = []
    with open('Mathlab.csv', mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        if "Hardcore" not in header:
            header.append("Hardcore") 
        for row in csv_reader:
            if len(row) >= 2 and row[0] == username and row[1] == password:
                if len(row) < len(header):
                    row.extend(["" for _ in range(len(header) - len(row))]) 
                current_score = row[header.index("Hardcore")]
                if current_score:
                    current_score = float(current_score)
                else:
                    current_score = 0.0
                if percentage > current_score:
                    row[header.index("Hardcore")] = str(percentage)
                updated = True
            rows.append(row)
    if not updated:
        print("Error: User not found in the CSV file.")
        exit()
    with open('Mathlab.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)  
        csv_writer.writerows(rows)  
        
    wait = input("type anything to exit: ")
    wait = wait.lower()
    if wait == '':
        print("")
        Go()
    else:
        print("")
        returnTable()
def Go():
    points = 0
    for i in range(11):
      print(i)
      RanA = random.randint(1,12)
      RanB = random.randint(1,12)
      RanC = RanA*RanB
      while True:
        try: 
          answer = int(input(f"{RanA} X {RanB} = ")) 
          break
        except:
          print("please enter a number")
      if answer == RanC:
         print("Correct!")
         points = points + 1
      else: 
        print("Wrong :(")    
    percentage = points / 10 * 100
    print(f"You got {percentage}%")
    updated = False
    rows = []
    header = []
    with open('Mathlab.csv', mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        if "Normal" not in header:
            header.append("Normal")
        for row in csv_reader:
            if len(row) >= 2 and row[0] == username and row[1] == password:
                if len(row) < len(header):
                    row.extend(["" for _ in range(len(header) - len(row))]) 
                current_score = row[header.index("Normal")]
                if current_score:
                    current_score = float(current_score)
                else:
                    current_score = 0.0
                if percentage > current_score:
                    row[header.index("Normal")] = str(percentage) 
                updated = True
            rows.append(row)
    if not updated:
        print("Error: User not found in the CSV file.")
        exit()
    with open('Mathlab.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)  
        csv_writer.writerows(rows)   
    wait = input("type anything to exit: ")
    wait = wait.lower()
    if wait == '':
        print("")
        Go()
    else:
        print("")
        returnTable()
login()
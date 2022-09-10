email = input(" Enter You E-Mail Address : ")
k, j, d = 0 , 0 , 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print(" Wrong Email, Might You Have Used Invalid Symbols In Email Id ")
                    print(" Valid Symbols To Use In Email Id's Are : '_' , '.' , '@' ")
                else:
                    print(" Right Email ")
            else:
                print(" Wrong Email , Please Check The Domain of The Mail (.com or .in")
        else:
            print(" Wrong Email , Either Missing '@' or Count of '@' is More Then One ")

    else:
        print(" Wrong Email , As First Letter of Email Can't Be Any Digit")
else:
    print(" Wrong Email Entered , As Length of Your Email Is Shorter Then Valid Email Length Criteria. Please Enter Email of Minimum 6 Letters ")

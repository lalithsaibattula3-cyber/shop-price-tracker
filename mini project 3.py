#student grades according to marks 

marks =int(input("enter the marks: "))                 #enter the marks 

if marks>100 or marks< 0:                                  #invalid marks
    print("invalid marks ")
else:
    print ("valid marks")                               #valid marks
    if marks>=90:
        print("GRADE A")                                  # A grade
    
    elif marks>=80:
        print("GRADE B")                                   # B grade

    elif marks>=70:                    
        print("GRADE C")                                    # C grade

    elif marks>=60:
        print("GRADE D")                                    # D grade

    elif marks >= 50:
        print("pass")                                       #PASS

    else:
        print("fail")                                       # FAIL
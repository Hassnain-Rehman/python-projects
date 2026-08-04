def  calculator():
    x = int(input("what's x? "))
    y = int(input("what's y? "))
    operator = input("what's the operator? ")

    if operator  ==  "+":
        print( x + y )
    elif operator  ==  "-":
        print( x - y )
    elif operator ==  "*":
        print( x * y )
    elif operator == "/":
        print( x / y )
    else:
        print("invalid operator")            

calculator()
        

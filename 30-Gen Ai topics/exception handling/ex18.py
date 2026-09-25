

while True:
    try:
        a=int(input("Enter numerator:"))
        b=int(input("Enter denominator:"))
        if a<=0 or b<0:
            raise Exception("Negative value or zero is not allowed")
        div=a/b
        print("Division of",a,"and",b,"is",div)
    except (ValueError)as ex1:
            print("Only int input allowed")
    except (ZeroDivisionError)as ex2:
            print("Denominator must be 0")
    except (Exception)as ex3:
        print(ex3)
    else:
        break
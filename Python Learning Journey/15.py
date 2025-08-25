# match case statements

x=int(input("Enter the value of x"))
match x:
    #case if x is zero
    case 0:
        print("x is zero.")
    #case with if condition
    case 20 if x%2==0:
        print("x is 20 and it is even number.")
    #empty case but with if condition
    case _ if x%2!=0:
        print("x is something else. and it is odd number")
    #default case
    case _:
        print("This number is not match with any condition in this program.")

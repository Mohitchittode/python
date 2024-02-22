# match case is like a switch case  statement in c language 
x = int(input("enter the value of X \n "))
# X is the variable to match 

match x :
    # if x is 0 
    case 0 : 
        print('x is zero ')

    case 4: 
        print("case is 4") 

    case _ if x!=90:
        print("x is not eqal to 90")
    case _ if x!=80:
        print("x is not eqal to 80")
    case _ :
        print (" it is a default case x : " , x )

#defalut case ke liye under score ( _ ) use hota he 

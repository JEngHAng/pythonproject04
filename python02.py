#function_Python
#function type 2 : HAVE Parameter / No Return
#Parameter ตัวแปรเก็บข้อมูล

def FuncA( x , y) :
    print ("Hi....")
    z = int(x) + int(y)
    print (f"{x} + {y} = {z}\n")
    #No Return
def FuncB( x ) :
    print (f"X is {x} mai ruu.\n")

FuncA(27 , 10)
FuncA(10 , 2003)
FuncB("The Best")
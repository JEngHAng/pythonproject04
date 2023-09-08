#function_Python
#Function type 4 : HAVE Parameters / HAVE Returns *****
def FuncA( n1 , n2 ):
    print (f"N1 is {n1}") 
    print (f"N2 is {n2}")
    return n1 + n2

def FuncB( name , year ) :
    return f"Halo {name}" , 2023 - year 

#n1 = input("Input n1 : ")
#n2 = input("Input n2 : ")
#name = input("Input name : ")
#year = int(input("Input Year : "))

print (f"Sum is {FuncA(20 , 30)}")
x , y = FuncB("JEng" , 2003)

print (f"{x} year {y} old")

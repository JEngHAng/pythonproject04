#function_Python
#Function type 3 : NO Parameter / HAVE Return *****
def FuncA():
    print ("AAAA")
    print ("BBBB")
    return "HI HI HI HaLO"

def FuncB():
    return 696 , True , 10 + 18

# FuncA() เขียนได้แต่ไม่ทำงาน
print (FuncA())
print (FuncB())

x = FuncA()
a , b , c = FuncB() #******

print (x)
print (f"{a} , {b} , {c}")
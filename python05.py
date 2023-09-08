#หาพื้นที่สี่เหลี่ยม และสามเหลี่ยม input ยาว / ฐาน สูง output
#Feature ทำงานอะไรบ้าง
#1.input  /// 2.com /// 3.output
def inputwitdlong() :
    wi = float(input("Input Witd : "))
    lo = float(input("Input Long : "))
    return wi , lo
def inputBaseHigh() :
    ba = float(input("Input Base : "))
    hi = float(input("Input High : "))
    return ba , hi
def calAndShowAreaSquare( wi , lo ) :
    area = wi * lo
    print (f"สี่เหลี่ยม กว้าง {wi} ยาว {lo} มีพี้นที่ {area}")
def calAndShowAreaTrianble( ba , hi ) :
    area = ba * hi / 2
    print (f"สามเหลี่ยม ฐาน {ba} สูง {hi} มีพี้นที่ {area}")

wi , lo = inputwitdlong()
calAndShowAreaSquare( wi , lo )
print ("--------------------------------------")
ba , hi = inputBaseHigh()
calAndShowAreaTrianble( ba , hi )
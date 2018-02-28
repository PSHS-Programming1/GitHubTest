from Rational import *

def enterData(str):
    num = ""
    den = ""

    while num == "" or den == "" or den == "0":
        print(str)
        num = input("Please enter the numerator   ---> ")
        den = input("Please enter the denominator ---> ")
    num = int(num)
    den = int(den)
    return num, den

def main():
    num, den = enterData("Enter data for r1")
    r1 = Rational(num, den)
    num, den = enterData("Enter data for r2")
    r2 = Rational(num, den)
    print()
    r3 = Rational.multiply(r1, r2)
    print(r1.getOriginal() + " * " + r2.getOriginal() + " = " + r3.getRational())
    r3 = Rational.divide(r1, r2)
    print(r1.getOriginal() + " / " + r2.getOriginal() + " = " + r3.getRational())


##    REMOVE COMMENTS BELOW TO TEST THE 100 POINT VERSION    ##
    
##    r3 = Rational.add(r1, r2)
##    print(r1.getOriginal() + " + " + r2.getOriginal() + " = " + r3.getRational())
##    r3 = Rational.subtract(r1, r2)
##    print(r1.getOriginal() + " - " + r2.getOriginal() + " = " + r3.getRational())
##
main()
input("\npress enter to quit")

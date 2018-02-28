class Rational():
    """This creates a rational number (fraction)"""

    def __init__(self, numerator=0, denominator=1):
        """Constructor for a rational number with a numerator and denominator"""
        self.originalNumerator = numerator
        self.originalDenominator = denominator
        self.reducedNumerator = None
        self.reducedDenominator = None
        self.reduce()

    def __getGCF(self,num1:int, num2:int):
        """returns the greatest common factor of 2 integer values"""
        rem = None
        gcf = None
        while (rem != 0):
            rem = num1 % num2
            if (rem == 0):
                gcf = num2
            else:
                num1 = num2
                num2 = rem
        return gcf

    def getDecimal(self):
        """returns the decimal version of the rational number"""
        return str(self.originalNumerator / str(self.originalDenominator))

    def reduce(self):
        """reduces the rational number """
        gcf = self.__getGCF(self.originalNumerator, self.originalDenominator)
        self.reducedNumerator = self.originalNumerator // gcf
        self.reducedDenominator = self.originalDenominator // gcf

    def getOriginal(self):
        """returns a string representation of the original rational number"""
        return str(self.originalNumerator) + "/" + str(self.originalDenominator)

    def getRational(self):
        """return a string representation of the reduced rational number"""
        return str(self.reducedNumerator) + "/" + str(self.reducedDenominator)

    def displayData(self):
        """Displays the data of the object in different forms"""
        print()
        print(self.getOriginal() + " equals " + self.getDecimal() + " and ")
        print(self.getOriginal() + " reduces to " + self.getRational())
        print()

    @staticmethod
    def multiply(r1, r2):
        """returns the product of r1 and r2"""
        pass #remove this pass when you start your code

    @staticmethod
    def divide(r1, r2):
        """returns the quotient of r1 and r2"""
        pass #remove this pass when you start your code




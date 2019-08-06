import math
import time

class Number:

    def __init__(self, in_num):
        self.num = in_num
        self.factors = self.factors()
        self.MersenneN = -1

        if (self.isCompliant()) == False:
            print("This number isn't supported: %", self.num)
            print ("Only Natural numbers are supported")

    def isCompliant(self):
        if (self.num < 0): return False
        ## if (math.isfinite(self.num) <> True): return False
        return True

    def factors(self):
        factors = []
        for i in range (1, self.num):
            if (self.num % i) == 0: (factors).append(i)
        
        '''
        print ("Factors of %", self.num)
        print factors
        '''

        return factors

    def isPerfect(self):
        total = 0
        for i in self.factors:
            total += i
        if total == self.num: return True
        else: return False

    def isPrime(self):
        print self.factors
        print [1]
        if self.factors == [1]: return True
        else: return False

    def isMersennePrime(self):
            if self.isPrime() == False: return (False, -1)

            for i in range (1, self.num):
                if 2**i - 1 == self.num: 
                    self.MersenneN = i
                    return (True, i)

            else: return (False, -1)

    def printPerfectNatural(self):
        print("*************************** Whoooo, Found Perfect Natural Number % ***************************", self.num)


    def printPrimeNatural(self):
        print("*************************** Whoooo, Found Prime Natural Number % ***************************", self.num)

    def printMersennePrime(self):
        print("*************************** Whoooo, Found Mersenne Prime Natural Number % where n = %", self.num, self.MersenneN)

####################  DRIVER TEST CODE #################

'''
print ("Enter a Natural Number - https://www.mathsisfun.com/definitions/natural-number.html")
testNum = input()
test = Number(testNum)
print ("Is % a Mersenne Prime number? %", testNum, test.isMersennePrime())
'''


## Now let's try to find as many perfect natural numbers as possible
## this is NP-hard problem done with a much simplified loop

''' 
print ("Now let's try to find as many perfect natural numbers as possible..")
i = 1
for i in range (1, 100000):
    print ("Processing % ... ", i)
    test = Number(i)
    if test.isPerfect() == True: 
        test.printPerfectNatural()
        time.sleep (5)
    i += 1
''' 

'''
print ("Now let's try to find as many prime natural numbers as possible..")
i = 1
for i in range (1, 1000000):
    print ("Processing % ... ", i)
    test = Number(i)
    if test.isPrime() == True: 
        test.printPrimeNatural()
        time.sleep (2)
    i += 1

''' 

print ("Now let's try to find as many Mersenne Prime numbers as possible..")
i = 1
for i in range (1, 10000):
    print ("Processing % ... ", i)
    test = Number(i)
    if test.isMersennePrime()[0] == True: 
        test.printMersennePrime()
        time.sleep (5)
    i += 1


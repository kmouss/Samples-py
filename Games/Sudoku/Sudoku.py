class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = [[-1]*9]*9
        self.sudokuPrime = [[]]

        sudokuPrimeIndexMax = 9
        rowMax = 3
        colMax = 3
        for sudokuPrimeIndex in range (0, sudokuPrimeIndexMax):
            for row in range (0, rowMax):
                for col in range (0, colMax):
                    self.sudokuPrime[sudokuPrimeIndex].append (self.sudoku[row][col])

        print (self.sudokuPrime) 

    def isListValid(self, aList):
        for i in range (len(aList)):
            if aList[i] < 1 or aList[i] > 9: return False
            for j in range (i+1, len(aList)):
               if aList[i] == aList[j]: return False
        return True   

    def PrintGame (self):
        print ("\n---------------------------------------------")
        for i in range (0, len(self.sudoku)):
            for j in range (0, len(self.sudoku[i])):
               print ("|", self.sudoku[i][j], end =" ")
            print ("|")
            print ("---------------------------------------------")


l = [[]]
test = Sudoku(l)
test.PrintGame()

testList = [0,1,2,3,4,5,6,7,8]
print (test.isListValid(testList))


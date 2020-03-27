################################################
##Final Project COM313
##Date: 2019-12-02
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file is basically made to run tests on the various game.
##    It checks for convergence rate and absorbing sets number over multiple rounds with a variance in the number of agents 
#################################################


## Some important files for the tests to run ##
from Game1_Functions import *
from Game2_Functions import *
from Game3_Functions import *
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy


### Pre-determined important parameters ###
N = 1000
C = 1/4
U = 100
Composition = 50
EquilibriumRound = 0
abset1 = 0
abset2 = 0
abset3 = 0

def Convergence(N, C, U, abset1, abset2, abset3, Composition, EquilibriumRound):

    ## Loop for the number of variations wanted in agents (change N)
    for j in range(5,(N+1), 100):

        TotalConvergence1 = 0
        TotalAbsorbingSet1 = 0
        TotalConvergence2 = 0
        TotalAbsorbingSet2 = 0
        TotalConvergence3 = 0
        TotalAbsorbingSet3 = 0
        Range = 1000 ## Set the number of rounds the game will play by a specified amount of agents

        ## Loop that execute the number of rounds wanted  ##
        ## It finds the equilibrium and number of sub absorbing sets for each game over and over again ##
        for i in range(Range):

            ## GAME 1 ##
            array = RandomGenerate(j, Composition)
            scorearray1 = ScoreCalc(array,C) 
            eqround1 = Equilibrium_Round(array, C, U, EquilibriumRound)
            abset1 = AbsorbingSet1(array, scorearray1, N, C, U, abset1, eqround1)
            TotalConvergence1 += eqround1
            TotalAbsorbingSet1 += abset1

            ## GAME 2 ##
            eqround2 = Equilibrium_Round2(array, C, U, EquilibriumRound)
            abset2 = AbsorbingSet2(array, scorearray1, N, C, U, abset2, eqround2)
            TotalConvergence2 += eqround2
            TotalAbsorbingSet2 += abset2

            ## GAME 3 ##
            scorearray3 = ScoreCalc3(array,C) 
            eqround3 = Equilibrium_Round3(array, C, U, EquilibriumRound)
            abset3 = AbsorbingSet3(array, N, C, U, abset3, eqround3)
            TotalConvergence3 += eqround3
            TotalAbsorbingSet3 += abset3


        ## Averaging out the number of rounds it took and the number of absorbing sets
        AvgConvergence1 = TotalConvergence1 / Range
        AvgAbsorbingSet1 = TotalAbsorbingSet1 / Range

        AvgConvergence2 = TotalConvergence2 / Range
        AvgAbsorbingSet2 = TotalAbsorbingSet2 / Range

        AvgConvergence3 = TotalConvergence3 / Range
        AvgAbsorbingSet3 = TotalAbsorbingSet3 / Range


        ## Open existing workbook ##
        book = open_workbook("Database.xls")

        ## Get the first sheet inside the workbook ##
        r_sheet = book.sheet_by_index(0)


        ## Copy the workbook read over into a workbook we can write into ##
        wb = copy(book)
        ## Get the sheet to write to within the writable copy ##
        w_sheet = wb.get_sheet(0)

        w_sheet.write(0, 0, 'Number of Individuals(N)')
        w_sheet.write(0, 1, 'Average Convergence Rate 1')
        w_sheet.write(0, 2, 'Average Absorbing Sets 1')
        w_sheet.write(0, 3, 'Average Convergence Rate 2')
        w_sheet.write(0, 4, 'Average Absorbing Sets 2')
        w_sheet.write(0, 5, 'Average Convergence Rate 3')
        w_sheet.write(0, 6, 'Average Absorbing Sets 3')
        
        number_rows = r_sheet.nrows
        
        ## Write to writable sheet ##
        w_sheet.write(number_rows, 0, j)
        w_sheet.write(number_rows, 1, AvgConvergence1)
        w_sheet.write(number_rows, 2, AvgAbsorbingSet1)
        w_sheet.write(number_rows, 3, AvgConvergence2)
        w_sheet.write(number_rows, 4, AvgAbsorbingSet2)
        w_sheet.write(number_rows, 5, AvgConvergence3)
        w_sheet.write(number_rows, 6, AvgAbsorbingSet3)

        ## save the writable workbook 
        wb.save("Database.xls")


## Call the function to execute it right away in the shell ##
Convergence(N, C, U, abset1, abset2, abset3, Composition, EquilibriumRound)

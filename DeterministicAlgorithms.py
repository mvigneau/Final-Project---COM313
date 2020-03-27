################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file contains all the different deterministic algorithms for all the different games. 
#################################################

from random import *

def ChangeAttitude1(array, U, scorearray):

    newarray = [0] * len(array)
    Avalue = 0
    Bvalue = 0
    Acount = 0
    Bcount = 0

    for i in range(len(newarray)):
        value = randrange(1,100)
        if(value <= U):
    
            for i in range(len(array)):
                Avalue = 0
                Bvalue = 0
                Acount = 0
                Bcount = 0
                if(i == 0):
                    if(array[len(array)-1] == "A"):
                        Avalue += scorearray[len(array)-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[len(array)-1]
                        Bcount += 1
                    if(array[i] == "A"):
                        Avalue += scorearray[i]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i]
                        Bcount += 1
                    if(array[i+1] == "A"):
                        Avalue += scorearray[i+1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i+1]
                        Bcount += 1
                elif(i == (len(array)-1)):
                    if(array[i-1] == "A"):
                        Avalue += scorearray[i-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-1]
                        Bcount += 1
                    if(array[i] == "A"):
                        Avalue += scorearray[i]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i]
                        Bcount += 1
                    if(array[0] == "A"):
                        Avalue += scorearray[0]
                        Acount += 1
                    else:
                        Bvalue += scorearray[0]
                        Bcount += 1
                else:
                    if(array[i-1] == "A"):
                        Avalue += scorearray[i-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-1]
                        Bcount += 1
                    if(array[i] == "A"):
                        Avalue += scorearray[i]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i]
                        Bcount += 1
                    if(array[i+1] == "A"):
                        Avalue += scorearray[i+1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i+1]
                        Bcount += 1

                if(Acount != 0):
                    Avalue = Avalue / Acount
                else:
                    Avalue = Avalue
                if(Bcount != 0):
                    Bvalue = Bvalue / Bcount
                else:
                    Bvalue = Bvalue

                if(Avalue > Bvalue):
                    newarray[i] = "A"
                elif(Bvalue > Avalue):
                    newarray[i] = "E"
                else:
                    newarray[i] = array[i]

        else:
            newarray[i] = array[i]

    
    return newarray




def ChangeAttitude2(array, U, scorearray):

    newarray = [0] * len(array)
    Avalue = 0
    Bvalue = 0
    Acount = 0
    Bcount = 0

    for i in range(len(newarray)):
        value = randrange(1,100)
        if(value <= U):
            
            for i in range(len(array)):
                Avalue = 0
                Bvalue = 0
                Acount = 0
                Bcount = 0
                if(i == (len(array)-2)):
                    if(array[len(array)-2] == "A"):
                        Avalue += scorearray[i-2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-2]
                        Bcount += 1
                    if(array[len(array)-1] == "A"):
                        Avalue += scorearray[i-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-1]
                        Bcount += 1
                    if(array[i] == "A"):
                        Avalue += scorearray[i]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i]
                        Bcount += 1
                    if(array[i+1] == "A"):
                        Avalue += scorearray[i+1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i+1]
                        Bcount += 1
                    if(array[0] == "A"):
                        Avalue += scorearray[0]
                        Acount += 1
                    else:
                        Bvalue += scorearray[0]
                        Bcount += 1
                        
                elif(i == (len(array)-1)):
                    if(array[i-2] == "A"):
                        Avalue += scorearray[i-2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-2]
                        Bcount += 1
                    if(array[i-1] == "A"):
                        Avalue += scorearray[i-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-1]
                        Bcount += 1
                    if(array[i] == "A"):
                        Avalue += scorearray[i]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i]
                        Bcount += 1
                    if(array[0] == "A"):
                        Avalue += scorearray[0]
                        Acount += 1
                    else:
                        Bvalue += scorearray[0]
                        Bcount += 1
                    if(array[1] == "A"):
                        Avalue += scorearray[1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[1]
                        Bcount += 1
                        
                else:
                    if(array[i-2] == "A"):
                        Avalue += scorearray[i-2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-2]
                        Bcount += 1
                    if(array[i-1] == "A"):
                        Avalue += scorearray[i-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-1]
                        Bcount += 1
                    if(array[i] == "A"):
                        Avalue += scorearray[i]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i]
                        Bcount += 1
                    if(array[i+1] == "A"):
                        Avalue += scorearray[i+1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i+1]
                        Bcount += 1
                    if(array[i+2] == "A"):
                        Avalue += scorearray[i+2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i+2]
                        Bcount += 1

                if(Acount != 0):
                    Avalue = Avalue / Acount
                else:
                    Avalue = Avalue
                if(Bcount != 0):
                    Bvalue = Bvalue / Bcount
                else:
                    Bvalue = Bvalue

                if(Avalue > Bvalue):
                    newarray[i] = "A"
                elif(Bvalue > Avalue):
                    newarray[i] = "E"
                else:
                    newarray[i] = array[i]

        else:
            newarray[i] = array[i]

    
    return newarray



def ChangeAttitude3(array, U, scorearray):

    newarray = [0] * len(array)
    Avalue = 0
    Bvalue = 0
    Acount = 0
    Bcount = 0

    for i in range(len(newarray)):
        value = randrange(1,100)
        if(value <= U):
            Avalue = 0
            Bvalue = 0
            Acount = 0
            Bcount = 0

            if(i == (len(array)-1)):
                if(array[i-1] == "A"):
                    Avalue += scorearray[i-1]
                    Acount += 1
                else:
                    Bvalue += scorearray[i-1]
                    Bcount += 1
                if(array[i] == "A"):
                    Avalue += scorearray[i]
                    Acount += 1
                else:
                    Bvalue += scorearray[i]
                    Bcount += 1
                if(array[0] == "A"):
                    Avalue += scorearray[0]
                    Acount += 1
                else:
                    Bvalue += scorearray[0]
                    Bcount += 1

                ##Checking for front and back neighborgs
                result = (i % 12)
                if(result >= 6):
                    value = ((12 - result) - 1)
                else:
                    value = result
                total = 11
                for j in range(value):
                    total -= 2
                    
                if(result >= 6):
                    if((i-total >= 0) and (array[(i-total)] == "A")):
                        Avalue += scorearray[i-total]
                        Acount += 1
                    elif((i-total >= 0) and (array[(i-total)] == "E")):
                        Bvalue += scorearray[i-total]
                        Bcount += 1

                    if(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "A")):
                        Avalue += scorearray[i+(12-total)]
                        Acount += 1
                    elif(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "E")):
                        Bvalue += scorearray[i+(12-total)]
                        Bcount += 1
                else:
                    if((i-(12-total) >= 0) and (array[i-(12-total)] == "A")):
                        Avalue += scorearray[i-(12-total)]
                        Acount += 1
                    elif((i-(12-total) >= 0) and (array[i-(12-total)] == "E")):
                        Bvalue += scorearray[i-(12-total)]
                        Bcount += 1

                    if(((i+total) < len(array)) and (array[i+total] == "A")):
                        Avalue += scorearray[i+total]
                        Acount += 1
                    elif(((i+total) < len(array)) and (array[i+total] == "E")):
                        Bvalue += scorearray[i+total]
                        Bcount += 1
                    

            else:
                if(array[i-1] == "A"):
                    Avalue += scorearray[i-1]
                    Acount += 1
                else:
                    Bvalue += scorearray[i-1]
                    Bcount += 1
                if(array[i] == "A"):
                    Avalue += scorearray[i]
                    Acount += 1
                else:
                    Bvalue += scorearray[i]
                    Bcount += 1
                if(array[i+1] == "A"):
                    Avalue += scorearray[i+1]
                    Acount += 1
                else:
                    Bvalue += scorearray[i+1]
                    Bcount += 1

                ##Checking for front and back neighborgs
                result = (i % 12)
                if(result >= 6):
                    value = ((12 - result) - 1)
                else:
                    value = result
                total = 11
                for j in range(value):
                    total -= 2
                    
                if(result >= 6):
                    if((i-total >= 0) and (array[(i-total)] == "A")):
                        Avalue += scorearray[i-total]
                        Acount += 1
                    elif((i-total >= 0) and (array[(i-total)] == "E")):
                        Bvalue += scorearray[i-total]
                        Bcount += 1

                    if(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "A")):
                        Avalue += scorearray[i+(12-total)]
                        Acount += 1
                    elif(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "E")):
                        Bvalue += scorearray[i+(12-total)]
                        Bcount += 1
                else:
                    if((i-(12-total) >= 0) and (array[i-(12-total)] == "A")):
                        Avalue += scorearray[i-(12-total)]
                        Acount += 1
                    elif((i-(12-total) >= 0) and (array[i-(12-total)] == "E")):
                        Bvalue += scorearray[i-(12-total)]
                        Bcount += 1

                    if(((i+total) < len(array)) and (array[i+total] == "A")):
                        Avalue += scorearray[i+total]
                        Acount += 1
                    elif(((i+total) < len(array)) and (array[i+total] == "E")):
                        Bvalue += scorearray[i+total]
                        Bcount += 1
                
                if(Acount != 0):
                    Avalue = Avalue / Acount
                else:
                    Avalue = Avalue
                if(Bcount != 0):
                    Bvalue = Bvalue / Bcount
                else:
                    Bvalue = Bvalue

                if(Avalue > Bvalue):
                    newarray[i] = "A"
                elif(Bvalue > Avalue):
                    newarray[i] = "E"
                else:
                    newarray[i] = array[i]

        else:
            newarray[i] = array[i]

    return newarray

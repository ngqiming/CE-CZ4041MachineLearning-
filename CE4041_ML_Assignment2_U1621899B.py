# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:23:33 2020

@author: NG QI MING U1621899B
"""

output = []
allData = []
def readDataFile():
    #Read data instances
    infile = open('data.txt','r')
    
    #Create an 1D array and store it
    tempList = []
    global totalRows 
    for line in infile:
       tempList.append(line)

    
    #Remove all n with nothing
    for row in range (len(tempList)):
        #Split the list  
        tempList[row]= tempList[row].replace('\n', '')
   
    #Store it into a 2d List
    for row in tempList:
        #split the data into 1 column
        buffer = row.split(" ")
        for i in range(len(buffer)):
            #Convert to string
            buffer[i] = float(buffer[i])
        #add all data into 2D array
        allData.append(buffer)    
 
    print("Data input from txt file: ")
    print(allData)
    
    
    
def wFunction(x, pts):
    #initialize h, 
    h = 2
    #for each row in the data structure
    for i in range(len(x)):
        #Calculate the value of u 
        u = (x[i]- pts[i])/h
        u = abs(u)
        #Condition checking for u
        if u < 1/2:
            return 1
        else:
            return 0
             
            
    
    
def sumOfXi(pts):
    totalNumerator = 0
    for x in allData:
        totalNumerator = totalNumerator + wFunction(x,pts)      
    
    return totalNumerator
    
def nEstimator():
    #initialize h and V 
    #Two dimensional volume
    h = 2
    V = pow(h,2)
    #declare n
    n = 5
   
    #Calulate the number of xi in the same hypercube as x 
    for pts in allData:
       
        #Get the nummerator 
        numOfXi = sumOfXi(pts)
        
        #Get the value P(x)
        Px = (numOfXi/(n*V))
        
        #store px into output
        output.append(Px)
        
    #print Px
    print("\n")
    print("The output value is:")    
    print(output)
        

def sendOutput():
   outputString  = "" 
   outFile = open("output.txt", "w") 
   for col in output:
       #Convert data to string and display it vertically 
       outputString = str(col)+ '\n'
       outFile.write(outputString)

    
def main():
    #Step 1: Read data file
    readDataFile()
    #Step 2: Apply Naive Estimator 
    nEstimator()
    #Step 3: print results
    sendOutput()
    
    
    
main()
    
   
   

    


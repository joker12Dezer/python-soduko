
#the following is a project i was given at a BOOTCAMP (W E T H I N K C O D E _)

#Sorry unfortunately i can't comment to explain the code
#just try your best to understand this
import os
begin=True
first = []
second = []

puzzle = 'sample.txt'  

with open(puzzle,"r") as file:
    readed = file.read()
    end = readed.split("\n")
    for item in end:
        for ever in item:
            if ever.isalnum():
                second.append(int(ever))
            
        first.append(second)
        second=[]


#the function Below is responsible for rendering the Sudoku Grid
def Display(par):
    global begin
    os.system('clear')
    horizontal = 20
    for row in range(len(par)):
        if row%3 == 0:
            print(" ",end="")
            print("-"*horizontal)
        for item in range(9):
            if item%3 == 0:
                print("|",end="")
                
                   
            print(str(par[row][item])+" ",end='')
            if item == 8:
                print("|")
                print("",end="") 
            
    print(" "+"-"*horizontal)
    if begin:
    	print('Press q to exit')
    	begin=False
    

#does the final calculation and determines if the user score
def final_check(lt):
    zero = False
    bad = False
    for rows in lt:
        for item in rows[rows]:
            if item == 0:
                zero = True
    if not zero:
        for rows in range(len(lt)):
            
            sum=0
            for col in range(len(rows)):
                sum +=lt[rows][col]
            if sum != 45:
                bad = True

        for col in range(len(lt)):
            
            sum=0
            for rows in range(len(rows)):
                sum +=lt[rows][col]
            if sum != 45:
                bad = True
    if bad:
        again = input("Would You like To Play Again Y OR N ?")
        if again.lower() == 'y':
            return "continue" 
        else:
            return "stop"
            
#the valisert (validate + insert ) function checks if the given cordinates are empty and checks if a number is repeated in it's row ,col and nonet and insert if the condition meets assigns the users value to the grid


def valisert(y,x,val,lt):
    ygroup=0
    xgroup=0
    if lt[y][x] == 0:
         stop = False
         m = [[0,1,2],[3,4,5],[6,7,8]]
         for i in range(3):
         	if x in m[i]:
        	    xgroup=m[i]
         	if y in m[i]:
        	     ygroup=m[i]
         for xt in xgroup:
             for yt in ygroup:
        	     if lt[yt][xt] == val:
        		     stop=True
         for i in range(9):
             if val == lt[i][x]:
                 stop = True
             elif val == lt[y][i]:
                 stop = True
        
             if not stop:        
                lt[y][x] = val
                return 'changed Successfully'
         else:
         	return "Duplicate Found"             
    else:
        return "CAN'T CHANGE number PRESENT"





# Additional Functions above this comment
Display(first)
# Implement your Sudoku Solution Below:
def solve_sudoku():
    #Edit the code Below Here
    
    
    x=input('enter column:')
    if x.lower()=='q':
    	exit(0)
    else:
    	x =int(x)
    y=int(input('enter row:'))
    val=int(input('Enter a number 1-9:'))
    mes = valisert(y,x,val,first)
    Display(first)
    if mes:
    	print(mes)
    

while True:
    solve_sudoku()
   
    
    
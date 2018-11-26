import pygame as py
#def roll_test (dice_1,dice_2,dice_3):
def dice_check(dice_1,dice_2,dice_3):  
    '''
    goes through all the fumction checking for match
    When all three dices roll same numbers
    '''
    if dice_1 == 1 and dice_2 == 1 and dice_3 == 1:           
        #print('THREE OF A KIND','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)      
        return int(10)             
    if dice_1 == 2 and dice_2 == 2 and dice_3 == 2:           
        #print('THREE OF A KIND','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(20)   
    if dice_1 == 3 and dice_2 == 3 and dice_3 == 3:           
        #print('THREE OF A KIND','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(30)    
    if dice_1 == 4 and dice_2 == 4 and dice_3 == 4:           
        #print('THREE OF A KIND','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(40) 
    if dice_1 == 5 and dice_2 == 5 and dice_3 == 5:           
        #print('THREE OF A KIND','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(50)   
    if dice_1 == 6 and dice_2 == 6 and dice_3 == 6:           
        #print('THREE OF A KIND','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)       
        return int(60)       
    
    return two_of_kind(dice_1,dice_2,dice_3)

   
def two_of_kind(dice_1,dice_2,dice_3):
    '''
    COMBINATION OF TWO DICES EQUAL THE SAME
    '''          
    # two of a kind dice 3 score
    if dice_1 == dice_2:         
        #print('SCORE! dice3: ',dice_3,'\ndice1:',dice_1,'dice2:',dice_2)
        return int(dice_3) 
    # two of a kind dice 2 score   
    if dice_1 == dice_3:                                          
        #print('SCORE! dice2: ',dice_2,'\ndice1:',dice_1,'dice3:',dice_3)    
        return int(dice_2)  
    # two of a kind dice 1 score   
    if dice_3 == dice_2:                                           
        #print('SCORE! dice1: ',dice_1,'\ndice1:',dice_3,'dice2:',dice_2)       
        return int(dice_1)        
    return perfect_score(dice_1,dice_2,dice_3)

def perfect_score(dice_1,dice_2,dice_3):
    '''
    WHEN DICES ROLL HIGHEST ROLL COMBINATION OF 6,5,4
    '''  
     
    if dice_1 == 4 and dice_2 == 5 and dice_3 == 6:           
        #print('perfect score','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)       
        return int(100)  
    if dice_1 == 5 and dice_2 == 4 and dice_3 == 6:           
        #print('perfect score','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)      
        return int(100)   
    if dice_1 == 6 and dice_2 == 5 and dice_3 == 4:           
        #print('perfect score','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)      
        return int(100)
    if dice_1 == 4 and dice_2 == 6 and dice_3 == 5:           
        #print('perfect score','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)       
        return int(100) 
    if dice_1 == 5 and dice_2 == 6 and dice_3 == 4:           
        #print('perfect score','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(100)  
    if dice_1 == 6 and dice_2 == 4 and dice_3 == 5:           
        #print('perfect score','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)       
        return int(100)
    
    return lowest_score(dice_1,dice_2,dice_3)


def lowest_score(dice_1,dice_2,dice_3):
    '''
    WHEN DICES ROLL LOWEST ROLL POSIBLE OF 1,2,3
    '''
    if dice_1 == 1 and dice_2 == 2 and dice_3 == 3:           
        #print('LOWEST SCORE','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(-1)   
    if dice_1 == 1 and dice_2 == 3 and dice_3 == 2:           
        #print('LOWEST SCORE','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(-1)  
    if dice_1 == 2 and dice_2 == 1 and dice_3 == 3:           
        #print('LOWEST SCORE','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)       
        return int(-1)  
    if dice_1 == 2 and dice_2 == 3 and dice_3 == 1:           
        #print('LOWEST SCORE','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(-1)  
    if dice_1 == 3 and dice_2 == 2 and dice_3 == 1:           
        #print('LOWEST SCORE','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(-1)   
    if dice_1 == 3 and dice_2 == 1 and dice_3 == 2:           
        #print('LOWEST SCORE','\ndice 1:',dice_1,'\ndice 2:',dice_2,'\ndice 3:',dice_3)
        return int(-1)   
    
    return


    
    
        


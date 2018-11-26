import random
import pygame as py
import time
import dice_test as dt

py.init()


width = 400
height = 600
red = (205,0,0)
green = (128,128,0)
black = (0,0,0)
white = (255,255,255)
gray = (200,190,150)
gold = (197,179,88)
behind_gray = (102,102,102)
board_teal=(51,153,153)
board_gray =(51,102,102)
center = (width/2 - 122,height * .05)

gameDisplay = py.display.set_mode((width,height))
py.display.set_caption('Cee_lo')
clock = py.time.Clock()
med_logo = py.image.load('244x204_logo.png')
game_background = py.image.load('400x519.png')
small_text = py.font.Font('freesansbold.ttf',25)

dice1 = py.image.load('dice1.png')
dice2 = py.image.load('dice2.png')    # DICES IMAGES
dice3 = py.image.load('dice3.png')
dice4 = py.image.load('dice4.png')
dice5 = py.image.load('dice5.png')
dice6 = py.image.load('dice6.png')

dice_small_size = {
    1:py.transform.scale(dice1,(50,50)),
    2:py.transform.scale(dice2,(50,50)),    # RESIZE OF DICE IMAGES
    3:py.transform.scale(dice3,(50,50)),
    4:py.transform.scale(dice4,(50,50)),
    5:py.transform.scale(dice5,(50,50)),
    6:py.transform.scale(dice6,(50,50)),
}
    
#CLASSES
class Player:
    def __init__(self):
        self.player1_roll = None   # False lets you roll,True checks roll score and None stops all rolls!!!
        self.player1_bet = 0 #amount player will bet
        self.bet_player1 = False
        self.player1_bank = 500  # players starter bank
        self.player1_dice = []
        self.player1_score = 0
        
class Cpu:
    def __init__(self):
        self.cpu_roll = None
        self.cpu_score = 0
        self.cpu_dice = []

def text_objects(text,font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def button(name,x,y,rw,rh,color,action = None):
    mouse = py.mouse.get_pos()
    if x + rw > mouse[0] > x and y + rh > mouse[1] > y:
        py.draw.rect(gameDisplay,(0,200,0),(x,y,rw,rh))
        if event.type == 5:
            action()          
    else:
       py.draw.rect(gameDisplay,color,(x,y,rw,rh))
   
    textSurf, textRect = text_objects(name,small_text,white)       
    textRect.center = ((x+(rw/2)),(y+(rh/2)))
    gameDisplay.blit(textSurf,textRect)
    
def roll():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    return [a,b,c]

player = Player()    
cpu = Cpu()

def player_1():
    small_text_size = int((height+width)*.015)
    large_text_size = int((height+width)*.025)
    small_text = py.font.Font('freesansbold.ttf',small_text_size)
    large_text = py.font.Font('freesansbold.ttf',large_text_size)
    gameDisplay.blit(game_background,(0,0)) ### background of one player mode

    def cpu_roll():
        dice_width_cpu = (width*.12)
        dice_height_cpu  = (height*.65)
        
        while cpu.cpu_roll == False:
            cpu.cpu_dice = roll()                #computers turn to roll
            cpu.cpu_score = dt.dice_check(*cpu.cpu_dice)
            for x in cpu.cpu_dice:
                    dice_width_cpu = dice_width_cpu + 60
                    gameDisplay.blit(dice_small_size[x],(dice_width_cpu,dice_height_cpu))
            dice_width_cpu = (width*.12)  # MOVES DICES BACK INTO PLACE
            
            if type(cpu.cpu_score) == int:
                cpu_score_text = large_text.render('Cpu: '+ str(cpu.cpu_score),True,white)  # score displayed on screen
                gameDisplay.blit(cpu_score_text,(width*.33,height*.40))
                cpu.cpu_roll = True
                return
            else:
                pass
    
    def roll_button():
                                  # !!!!!!!Important roll Button!!!!!!!!!!!!!!!!!!!!!!!!
        dice_width = (width*.125)
        dice_height = (height*.53)
        mouse = py.mouse.get_pos()           
        if width*.78 + width*.20  > mouse[0] > width*.78 and height*.88 + height*.10 > mouse[1] > height*.88:
            py.draw.rect(gameDisplay,red,(width*.78,height*.88,width*.20,height*.10))      #actual button,will get change with png ROLL button
            textSurf, textRect = text_objects('ROLL',large_text,white)
            textRect.center = ((width*.78+(width*.20/2)),(height*.88+(height*.10/2)))
            gameDisplay.blit(textSurf,textRect)

            if event.type == 5 and player.player1_roll == False:  # MOUSE BUTTON DOWN VALUE
                player.player1_dice = roll()  
                player.player1_roll = True
                player.bet_player1 = None
                cpu.cpu_roll = None
                for x in player.player1_dice:
                    dice_width = dice_width + 60
                    gameDisplay.blit(dice_small_size[x],(dice_width,dice_height))
                dice_width = (width*.125)
                print(f'Player1 roll: {player.player1_dice}')
                                                          
        else:
            py.draw.rect(gameDisplay,gray,(width*.78,height*.88,width*.20,height*.10))
            textSurf, textRect = text_objects('ROLL',large_text,white)
            textRect.center = ((width*.79+(width*.20/2)),(height*.88+(height*.10/2)))
            gameDisplay.blit(textSurf,textRect)

    def bet_scrns ():
        mouse = py.mouse.get_pos()
        #### Players Bank !!!!!!!
        py.draw.rect(gameDisplay,board_teal,(width*.26,height*.80,width*.50,height*.05))
        textSurf, textRect = text_objects('Player: $'+str(player.player1_bank),large_text,white)  # color of text ,size
        textRect.center = ((width*.50),(height*.83))
        gameDisplay.blit(textSurf,textRect)

        ### BET SCREEN !!!!!
        py.draw.rect(gameDisplay,gold,(0,height*.87,width*.26,height*.15))  # rect box around text bet screen
        bet_text = large_text.render('BET ',True,black)                   # Bet shown on screen
        gameDisplay.blit(bet_text,(width*.05,height*.88))           # code to make it appear on screen
        textSurf, textRect = text_objects('$ '+str(player.player1_bet),large_text,white)   # color of text, size 
        textRect.center = ((width*.10),(height*.955))
        gameDisplay.blit(textSurf,textRect)
        
        ### minus BUTTON###!!!!!     
        if width* .77 + width*.10 > mouse[0] > width* .77 and height*.67 + height*.10 > mouse[1] > height*.60:  
            py.draw.rect(gameDisplay,red,(width*.77,height*.67,width*.10,height*.10)) # rect box around text bet screen #actual button,will gwt change with png BET button
            textSurf, textRect = text_objects('-',small_text,white)
            textRect.center = ((width* .75+(width*.10/2)),(height*.67+(height*.10/2)))
            gameDisplay.blit(textSurf,textRect)
            
            if event.type == 5 and player.player1_bet != 0:  # MOUSE BUTTON DOWN VALUE
                player.player1_bet = player.player1_bet - 50
                print(player.player1_bet)            
        else:
            py.draw.rect(gameDisplay,gray,(width*.77,height*.67,width*.10,height*.10))  #actual button,will gwt change with png BET button
            textSurf, textRect = text_objects('-',small_text,white)
            textRect.center = ((width* .77+(width*.10/2)),(height*.67+(height*.10/2)))
            gameDisplay.blit(textSurf,textRect)
            
       ####Bet BUTTON !!!!!!            
        if width* .89 + width*.20 > mouse[0] > width* .89 and height*.67 + height*.10 > mouse[1] > height*.60:  
            py.draw.rect(gameDisplay,red,(width*.89,height*.67,width*.10,height*.10))  #actual button,will gwt change with png BET button
            textSurf, textRect = text_objects('Bet',small_text,white)
            textRect.center = ((width* .89+(width*.10/2)),(height*.67+(height*.10/2)))
            gameDisplay.blit(textSurf,textRect)
            
            if event.type == 5 and player.player1_bet < player.player1_bank: # MOUSE BUTTON DOWN VALUE
                player.player1_bet = player.player1_bet + 50
                player.bet_player1 = True
                py.draw.rect(gameDisplay,board_gray,(width*.28,height*.35,170,30))  # player score BLANK BOX TO CLEAR AREA  ON BOARD
                py.draw.rect(gameDisplay,board_gray,(width*.28,height*.40,170,30))  # cpu score BLANK BOX TO CLEAR AREA  ON BOARD
                py.draw.rect(gameDisplay,gold,(width*.285,height*.92,180,30))  #WINNERS BLAnK   AT BOTTOM OF PAGE
                py.draw.rect(gameDisplay,board_teal,(width*.27,height*.53,175,50))  #player dice blanl clear
                py.draw.rect(gameDisplay,board_teal,(width*.26,height*.65,175,50)) # cpu dice blank clear
##            if player.player1_bet > 0:
##                py.draw.rect(gameDisplay,gray,(width*.77,height*.67,width*.10,height*.10))  #button will turn red when bet is more then  0
##                textSurf, textRect = text_objects('-',small_text,white)
##                textRect.center = ((width* .77+(width*.10/2)),(height*.67+(height*.10/2)))
##                gameDisplay.blit(textSurf,textRect)
              
                py.display.update()
                print(player.player1_bet)
        else:
            py.draw.rect(gameDisplay,gray,(width*.89,height*.67,width*.10,height*.10))  #actual button,will gwt change with png BET button
            textSurf, textRect = text_objects('Bet',small_text,white)
            textRect.center = ((width*.88 +(width*.10/2)),(height*.67+(height*.10/2)))
            gameDisplay.blit(textSurf,textRect)
            
    def who_wins (cpu, player):
        if player > cpu:
            return 'player'
        if cpu > player :          
            return 'cpu'
        if player == cpu:           
            return 're_roll'        
            
                  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!main game loop  start !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       
    while player.player1_bank != 0:
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

            bet_scrns()
            roll_button()
            clock.tick(60)
            py.display.update()

            if player.bet_player1 == True :  # you have to bet first in order to roll Bet Button !!!  bet_scrns() function
                player.player1_roll = False               

            if player.player1_roll == True:    # in order to check score you have to roll first roll funtion
                player.player1_score = dt.dice_check(*player.player1_dice)
                player.player1_roll = None
                
                if type(player.player1_score) == int and cpu.cpu_roll == None:
                    #py.draw.rect(gameDisplay,green,(width*.30,height*.35,170,30)) 
                    py.display.update()
                    player_score_text = large_text.render('Player: '+str(player.player1_score),True,white)                   # PLAYERS score displayed on screen
                    gameDisplay.blit( player_score_text,(width*.33,height*.35))
                    cpu.cpu_roll = False
                    cpu_roll()
                    who_wins_check = who_wins(int(cpu.cpu_score),int(player.player1_score))
                    if who_wins_check == 'player':
                        player.player1_bank = player.player1_bank + player.player1_bet   # PLAYERS WINS SO BET GETS ADDED TO HIS TOTAL
                        py.draw.rect(gameDisplay,gold,(width*.285,height*.92,180,30))
                        py.display.update()
                        cpu_score_text = large_text.render('PLAYER WINS',True,white)                   # PLAYER WINS IS SHOWN ON SCREEN
                        gameDisplay.blit(cpu_score_text,(width*.29,height*.92))     # where text will appear through width and height
                        print('\nplayer wins')
                    if who_wins_check == 'cpu':
                        player.player1_bank = player.player1_bank - player.player1_bet   #PLAYER LOSES BET GETS DEDUCTED
                        py.draw.rect(gameDisplay,gold,(width*.32,height*.92,180,30))
                        py.display.update()
                        cpu_score_text = large_text.render('CPU WINS',True,white)                   # CPU WINS IS SHOWN ON SCREEN
                        gameDisplay.blit(cpu_score_text,(width*.30,height*.92))     # where text will appear through width and heightLAYER LOSES SO BETS GETS MINUS TO HIS TOTAL
                        print('\ncpu wins')
                    if who_wins_check == 're_roll':
                        py.draw.rect(gameDisplay,gold,(width*.30,height*.92,180,30))
                        py.display.update()
                        cpu_score_text = large_text.render('TIE ROLL',True,white)                   # TIE RE ROLL IS SHOWN ON SCREEN
                        gameDisplay.blit(cpu_score_text,(width*.30,height*.92))     # where text will appear through width and height 
                        print('\nre roll')
                    player.player1_score = 0
                    cpu.cpu_score = 0
                    player.player1_bet = 0
                    
                    
                else:
                    player.player1_roll = False
                    
    if player.player1_bank == 0:
        player.player1_bank = 500
        player.player1_bet = 0
        game_intro()
               
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Main Game loop end!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
def player_2():   # two player mode
    pass        
def rules ():  #Rules page
    pass
      
def game_intro():    # main start display
    gameDisplay.fill(gold)  # main display color
    gameDisplay.blit(med_logo,(center))
    button('1 Player',width/2-width/6,height*.6,width/3,height*.10,gray,player_1)
    button('2 Player',width/2-width/6,height *.75,width/3,height*.10,gray,player_2)
    button('Rules',width/2-width/6,height *.89,width/3,height *.10,gray,rules)
    py.display.update()
    
if __name__ == '__main__':
    #intro game loop  
    while True:  
        for event in py.event.get():
            if event.type == py.QUIT:
               quit() 
        game_intro()
        

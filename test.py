##import test_cee_lo as tcl
##
##class Score:                    # scores of dices are kept for player
##    def __init__(self):
##        self.score = False
##        self.cpu = False
##        self.player = False
##        self.points_player_1 = 0
##        self.points_player_2 = 0
##        self.points_cpu = 0
##
##score = Score()
##
##score.points_player_1 = tcl.three_of_kind(1,1,1)
##print(score.points_player_1)
##

##a = 5
##b = 10
##
##print(f'Five plus ten is {a + b} and not {2*(a+b)} why.')
##print('Five plus ten is',a+b,'and not',(2*(a+b)),'why.')



##class Indenter:
##    def __init__(self):
##        self.level = 0
##    def __enter__(self):
##        self.level += 1
##        return self
##    def __exit__(self,exc_type,exc_val,exc_tb):
##        self.level -= 1
##    def print(self,text):
##        print(' '*self.level + text)
##
##
##with Indenter() as indent:
##    indent.print('hi')
##    with indent:
##        indent.print('hello')
##        with indent:
##            indent.print('bonjour')
##    indent.print('hey')



import requests    # impoort data from web


# was up check thi sput




    



    

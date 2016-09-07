
from graphics import *
from random import *

class AChaos(object):
    
    def __init__(self):
        
        # SIx tubes on the first side
        self.SideA = [ ['N',1,1],['W','W',2,2],['B','B','B',3,3], ['Y','Y','Y','Y',4,4],
                      ['G','G','G','G','G',5,5],['R','R','R','R','R','R',6,6]]
        
        #Six tubes on the second side 
        self.SideB = [[0,1,1], [0,0,2,2], [0,0,0,3,3], [0,0,0,0,4,4],
                      [0,0,0,0,0,5,5], [0,0,0,0,0,0,6,6]]
        
        self.win = GraphWin("Atomic Chaos",1000,500)
        
        #tells us which side is up
        self.orentation = True
    def Print(self):
        self.win.getMouse()
        self.win.close()
        self.win = GraphWin("Atomic Chaos",1000,500) 
        for tubeNum, tube in enumerate(self.SideA):
            p1 = Point(500,(6-tube[-2])*50+100)
            p2 = Point(tubeNum*50+550,(6-tube[-2])*50+150)
            Tube = Rectangle(p1, p2)
            Tube.draw(self.win)
            for i,ball in enumerate(tube):
                if False == isinstance( ball, int ):
                    Ball = Circle(Point(525+i*50,(6-tube[-2])*50+125),25)
                    if ball == 'R':
                        Ball.setFill(color_rgb(255, 0, 0))
                    elif ball == 'G':
                        Ball.setFill(color_rgb(0,255,0))                    
                    elif ball == 'Y':
                        Ball.setFill(color_rgb(255,255,0))
                    elif ball == 'B':
                        Ball.setFill(color_rgb(0, 0, 255))
                    elif ball == 'W':
                        Ball.setFill(color_rgb(0, 0, 0))
                    elif ball == 'N':
                        Ball.setFill(color_rgb(255, 255, 255))                    
                    Ball.draw(self.win)
                    
        for tubeNum, tube in enumerate(self.SideB):
            Tube = Rectangle(Point(450-tubeNum*50,(6-tube[-2])*50+100), Point(500,(6-tube[-2])*50+150))
            Tube.draw(self.win)
            for i,ball in enumerate(tube):
                if False == isinstance( ball, int ):
                    Ball = Circle(Point(475-i*50,(6-tube[-2])*50+125),25)
                    if ball == 'R':
                        Ball.setFill(color_rgb(255, 0, 0))
                    elif ball == 'G':
                        Ball.setFill(color_rgb(0,255,0))                    
                    elif ball == 'Y':
                        Ball.setFill(color_rgb(255,255,0))
                    elif ball == 'B':
                        Ball.setFill(color_rgb(0, 0, 255))
                    elif ball == 'W':
                        Ball.setFill(color_rgb(0, 0, 0))
                    elif ball == 'N':
                        Ball.setFill(color_rgb(255, 255, 255))                    
                        
                    Ball.draw(self.win)            
        if self.orentation == True:
            for item in self.SideA:
                print('[',end='')
                for ball in item:
                    if False == isinstance( ball, int ):
                        print ("(",ball,")",sep=' ',end='')
                    elif ball == 0:
                        print('---',end='')
                print('|',end='')
                for ball in self.SideB[item[-1]-1]:
                    if False == isinstance( ball, int ):
                        print ("(",ball,")",sep=' ',end='')
                    elif ball == 0:
                        print('---',end='')
                print(']')
                
        else:
            for item in self.SideB:
                print('[',end='')
                for ball in item:
                    if False == isinstance( ball, int ):
                        print ("(",ball,")",sep=' ',end='')
                    elif ball == 0:
                        print('---',end='')
                print('|',end='')
                for ball in self.SideA[item[-1]-1]:
                    if False == isinstance( ball, int ):
                        print ("(",ball,")",sep=' ',end='')
                    elif ball == 0:
                        print('---',end='')
                print(']')
            
            
    def flip(self):
        if self.orentation == False:
            self.orentation =True #change orentation
            self.DropIntoSideA()    #Drop the balls to sideA
            
        else:
            self.orentation = False #change orentation
            self.DropIntoSideB() #Drop the balls to sideB
            
    #---------------------Drops the ball into side A---------------------------------    
    def DropIntoSideA(self):
        Fallen = False
        for tube in self.SideA:
            for ball in range(len(tube)-2):
                if tube[-3] == 0 and tube[ball] !=0:
                    while tube[-3] ==0:
                        tube.pop(-3)
                        tube.insert(0,0)        
        for tubeNum, tube in enumerate(self.SideA): # for each tube on side A
                        for i in range(len(tube)-2,-1,-1): #find the last item of int the tube
                            if tube[i] == 0:
                                nextBall = next((j for j, x in enumerate(self.SideB[tube[-1]-1])
                                                 if True!=isinstance( x, int )), None) #http://stackoverflow.com/questions/19502378/python-find-first-instance-of-non-zero-number-in-list
                                if nextBall == None:
                                    break
                                Fallen = True
                                tube[i] = self.SideB[tube[-1]-1][nextBall]
                                self.SideB[tube[-1]-1][nextBall] = 0
        for tube in self.SideB:
            for ball in range(len(tube)-2):
                if tube[0] == 0 and tube[ball] !=0:
                    while tube[0] ==0:
                        tube.pop(0)
                        tube.insert(-2,0)
                    break
        return Fallen
                
                    
   #---------------------Drops the ball into side B---------------------------------
    def DropIntoSideB(self):
        Fallen = False
        for tube in self.SideB:
            for ball in range(len(tube)-2):
                if tube[-3] == 0 and tube[ball] !=0:
                    while tube[-3] ==0:
                        tube.pop(-3)
                        tube.insert(0,0)
                    break        
        for tubeNum, tube in enumerate(self.SideB): # for each tube on side B
                        for i in range(len(tube)-2,-1,-1): #find the last item of int the tube
                            if tube[i] == 0:
                                nextBall = next((j for j, x in enumerate(self.SideA[tube[-1]-1])
                                                 if True !=isinstance( x, int )), None) #http://stackoverflow.com/questions/19502378/python-find-first-instance-of-non-zero-number-in-list
                                if nextBall == None:
                                    break
                                Fallen = True
                                tube[i] = self.SideA[tube[-1]-1][nextBall]
                                self.SideA[tube[-1]-1][nextBall] = 0
        for tube in self.SideA:
            for ball in range(len(tube)-2):
                if tube[0] == 0 and tube[ball] !=0:
                    while tube[0] ==0:
                        tube.pop(0)
                        tube.insert(-2,0)
                    break
        return Fallen
                    
                                
    def rotateC(self):
        if self.orentation == False:
            for tubeNum, tube in enumerate(self.SideB):
                if tube[-1] == 6:
                    tube[-1] = 1
                else:
                    tube[-1]+=1
                                 
            for tubeNum, tube in enumerate(self.SideA):
                if tube[-1] == 1:
                    tube[-1] = 6
                else:
                    tube[-1]-=1
                if tube[-2] == 1:
                    tube[-2] = 6
                else:
                    tube[-2]-=1                    
            self.DropIntoSideB()
        else:
            for tubeNum, tube in enumerate(self.SideB):
                if tube[-1] == 1:
                    tube[-1] = 6
                else:
                    tube[-1]-=1
                if tube[-2] == 1:
                    tube[-2] = 6
                else:
                    tube[-2]-=1                 
            for tubeNum, tube in enumerate(self.SideA):
                if tube[-1] == 6:
                    tube[-1] = 1
                else:
                    tube[-1]+=1
            self.DropIntoSideA()            
        
    def rotateCC(self):
        if self.orentation == False:
            for tubeNum, tube in enumerate(self.SideA):
                if tube[-1] == 6:
                    tube[-1] = 1
                else:
                    tube[-1]+=1
                if tube[-2] == 6:
                    tube[-2] = 1
                else:
                    tube[-2]+=1                     
                                

            for tubeNum, tube in enumerate(self.SideB):
                if tube[-1] == 1:
                    tube[-1] = 6
                else:
                    tube[-1]-=1
                               
            self.DropIntoSideB()
        else:
            for tubeNum, tube in enumerate(self.SideA):
                if tube[-1] == 1:
                    tube[-1] = 6
                else:
                    tube[-1]-=1
                                
            for tubeNum, tube in enumerate(self.SideB):
                if tube[-1] == 6:
                    tube[-1] = 1
                else:
                    tube[-1]+=1
                if tube[-2] == 6:
                    tube[-2] = 1
                else:
                    tube[-2]+=1                 
            self.DropIntoSideA()
            
    def isFlat(self):
        if self.orentation == True:
            for tube in self.SideB:
                if tube[-3]==0 and tube[0] ==0:
                    flat =True
                else:
                    return False
            return True
        else:
            for tube in self.SideA:
                if tube[-3]==0 and tube[0] ==0:
                    flat =True
                else:
                    return False
            return True
    def Randomize(self):
        i = 0
        lastChoice = 4;
        k = 20
        while i < 10:
            choice = randint(0,2)
            while choice == 0 and lastChoice ==0:
                choice = randint(0,2)
            if choice == 0 and i+2 != k:
                self.flip()
                print("Flip")
                i+=1
            elif choice == 1:
                while self.rotateC() == False and self.isFlat() == False:
                    print("RotateC")
                    i+=1
                print("RotateC")
                i+=1  
            else:
                while self.rotateCC() == False and self.isFlat() == False:
                    print("RotateCC")
                    i+=1
                print("RotateCC")
                i+=1        
    def InversePuzzle(self,k):
        self.Randomize()
        self.Print()
        lastChoice = 4
        i = 0
        while i < k:
            #self.Print()
            choice = randint(0,2)
            while choice == 0 and lastChoice ==0:
                choice = randint(0,2)
            if choice == 0 and i+2 != k:
                self.flip()
                print("Flip")
                i+=1
                lastChoice = 0
            elif choice == 1:
                while self.rotateC() == False and self.isFlat() == False:
                    print("RotateC")
                    i+=1
                print("RotateC")
                i+=1
                lastChoice = 1;
            else:
                while self.rotateCC() == False and self.isFlat() == False:
                    print("RotateCC")
                    i+=1
                print("RotateCC")
                i+=1
                lastChoice = 2
        if i+1 != k:
            self.InversePuzzle(k)
            
        
        
        
def main():
    
    
    puzzle = AChaos()
    puzzle.Print()
    puzzle.InversePuzzle(5)
    puzzle.Print()
    print()    
    #print()
    #puzzle.rotateC()
    #puzzle.Print()
    #print()
    #puzzle.flip()
    #puzzle.Print()
    #print()    
    #puzzle.rotateCC()
    #puzzle.Print()
    #print()    
    #puzzle.flip()
    #puzzle.Print()
    #print()
    #puzzle.rotateC()
    #puzzle.Print()
    #print()
    #puzzle.rotateCC()
    #puzzle.Print()
    #print()    
    puzzle.win.getMouse()
    puzzle.win.close()    
            
            
            
    return 0  
main()
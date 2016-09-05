
from graphics import *

class AChaos(object):
    
    def __init__(self):
        
        # SIx tubes on the first side
        self.SideA = [ ['N',1],['W','W',2],['B','B','B',3], ['Y','Y','Y','Y',4],
                      ['G','G','G','G','G',5],['R','R','R','R','R','R',6]]
        
        #Six tubes on the second side 
        self.SideB = [[0,1], [0,0,2], [0,0,0,3], [0,0,0,0,4],
                      [0,0,0,0,0,5], [0,0,0,0,0,0,6]]
        
        #tells us which side is up
        self.orentation = True
    def Print(self,win):
        tubeA = Rectangle(Point(200,100), Point(500,150))
        tubeB = Rectangle(Point(250,150), Point(500,200))
        tubeC = Rectangle(Point(300,200), Point(500,250))
        tubeD = Rectangle(Point(350,250), Point(500,300))
        tubeE = Rectangle(Point(400,300), Point(500,350))
        tubeF = Rectangle(Point(450,350), Point(500,400))
        tubeF.draw(win)
        tubeE.draw(win)
        tubeD.draw(win)
        tubeC.draw(win)
        tubeB.draw(win)
        tubeA.draw(win)
        for item in self.SideA:
            print (item)
        print()
        for item in self.SideB:
            print(item)
            
    def flip(self):
        if self.orentation == False:
            self.orentation == True #change orentation
            self.DropIntoSideA()    #Drop the balls to sideA
            
        else:
            self.orentation == False #change orentation
            self.DropIntoSideB() #Drop the balls to sideB
            
    #---------------------Drops the ball into side A---------------------------------    
    def DropIntoSideA(self):
        for tubeNum, tube in enumerate(self.SideA): # for each tube on side A
                        for i in range(len(tube)-2,-1,-1): #find the last item of int the tube
                            if tube[i] == 0:
                                nextBall = next((j for j, x in enumerate(self.SideB[tube[-1]-1])
                                                 if True!=isinstance( x, int )), None) #http://stackoverflow.com/questions/19502378/python-find-first-instance-of-non-zero-number-in-list
                                if nextBall == None:
                                    break
                                tube[i] = self.SideB[tube[-1]-1][nextBall]
                                self.SideB[tube[-1]-1][nextBall] = 0
        for tube in self.SideB:
            if tube[0] == 0 and tube[-2] !=0:
                while tube[0] ==0:
                    tube.pop(0)
                    tube.insert(-1,0)
                    
   #---------------------Drops the ball into side B---------------------------------
    def DropIntoSideB(self):
        for tubeNum, tube in enumerate(self.SideB): # for each tube on side B
                        for i in range(len(tube)-2,-1,-1): #find the last item of int the tube
                            if tube[i] == 0:
                                nextBall = next((j for j, x in enumerate(self.SideA[tube[-1]-1])
                                                 if True !=isinstance( x, int )), None) #http://stackoverflow.com/questions/19502378/python-find-first-instance-of-non-zero-number-in-list
                                if nextBall == None:
                                    break
                                tube[i] = self.SideA[tube[-1]-1][nextBall]
                                self.SideA[tube[-1]-1][nextBall] = 0
        for tube in self.SideA:
            if tube[0] == 0 and tube[-2] !=0:
                while tube[0] ==0:
                    tube.pop(0)
                    tube.insert(-1,0)
                                
    def rotateC(self):
        if self.orentation == True:
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
            self.DropIntoSideB()
        else:
            for tubeNum, tube in enumerate(self.SideB):
                if tube[-1] == 1:
                    tube[-1] = 6
                else:
                    tube[-1]-=1
            for tubeNum, tube in enumerate(self.SideA):
                if tube[-1] == 6:
                    tube[-1] = 1
                else:
                    tube[-1]+=1
            self.DropIntoSideA()            
        
    def rotateCC(self):
        if self.orentation == True:
            for tubeNum, tube in enumerate(self.SideA):
                if tube[-1] == 6:
                    tube[-1] = 1
                else:
                    tube[-1]+=1
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
            self.DropIntoSideA()            
        
        
def main():
    win = GraphWin("Atomic Chaos",1000,500)
    
    
    puzzle = AChaos()
    puzzle.Print(win)
    print()
    puzzle.rotateC()
    puzzle.Print(win)
    print()
    puzzle.flip()
    puzzle.Print(win)
    print()      
    puzzle.rotateCC()
    puzzle.Print(win)
    print() 
    win.getMouse()
    win.close()    
    
            
            
            
    return 0  
main()
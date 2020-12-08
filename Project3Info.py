from random import *#import needed for random numbers which is used for natural deaths
#Now we will take inputs for the size of the grid and the required generation
class World():
    '''where all information about the EcoSystem is stored'''
    def __init__(self,rowers,colers):
        '''initialising'''
        self.rows=rowers
        self.col=colers
        self.arr= [[['e',0,0,0] for i in range (self.col+2)] for i in range(self.rows+2)]#Stores details of each cell
        self.stats=[[0 for i in range(5)]for j in range(4)]#living,old age,starvation,eaten,natural causes
        #adult lion, baby lion, adult ant, baby ant
        self.LMA=20#These are our constants
        self.AMA=10
        self.LBA=3
        self.ABA=2
        self.LND=32
        self.emp=1
        self.lio=1
        self.ant=1
        
    def randy(self):#randomises the grid
        '''Uses the inputed ratio to randomly fill grid'''
        for i in range(1,self.rows+1):
            for j in range(1,self.col+1):
                a = randint(1,(self.emp+self.lio+self.ant))#total possibilty of random numbers
                if a <=self.lio:#lions
                    self.arr[i][j][3]=randint(1,self.LMA)#Randomly generate age from 1 to maximum
                    if self.arr[i][j][3]>=self.LBA:#adult
                        self.arr[i][j][0]='L'
                        self.fill(i,j,1,11)#we add one to indicate a lion and 10 to indicate an adult
                        self.stats[0][0]+=1
                    else:
                        self.arr[i][j][0]='l'
                        self.fill(i,j,1,1)#all the surrounding blocks must store this lion
                        self.stats[1][0]+=1
                        
                elif a <=self.lio+self.ant:#antelopes
                    self.arr[i][j][3]=randint(1,self.AMA)
                    if self.arr[i][j][3]>=self.ABA:#Adult
                        self.arr[i][j][0]='A'
                        self.fill(i,j,2,11)#Records adult to adjacent blocks
                        self.stats[2][0]+=1
                    else:
                        self.arr[i][j][0]='a'              
                        self.fill(i,j,2,1)
                        self.stats[3][0]+=1
  
    def fill(self,i,j,k,l):
        '''This method is used to automatically fill surrounding when something happens'''
        for s in range(-1,2):
            for t in range(-1,2):
                if s==t and s==0:
                    continue
                self.arr[i+s][j+t][k]+=l
        

    def paste(self):
        '''a method that allows us to copy the content of our array to another'''
        tempry=[[]]
        for i in range(self.rows+2):
            tempry.append([])
            for j in range(self.col+2):
                tempry[i].append([])
                for k in range(4):
                    tempry[i][j].append(self.arr[i][j][k])
        return tempry        

    def check(self):
        '''runs one generation'''
        temp=self.paste()
        for i in range(1,self.rows+1):
            for j in range(1,self.col+1):
                #Birth
                if temp[i][j][0]=='e':#this means that it is an empty square
                    if temp[i][j][1]%10>=4 and temp[i][j][1]/10>=3 and temp[i][j][2]%10<=3:#lion birth
                        self.arr[i][j][0]='l'
                        self.arr[i][j][3]=1
                        self.fill(i,j,1,1)
                        self.stats[1][0]+=1
                        
                        
                    elif temp[i][j][2]%10>=4 and temp[i][j][2]/10>=3 and temp[i][j][1]%10<=3:#antelope birth
                        self.arr[i][j][0]='a'
                        self.arr[i][j][3]=1
                        self.fill(i,j,2,1)
                        self.stats[3][0]+=1
                                  
       
                else:#there is an animal living there
                    if temp[i][j][0]=='l' or temp[i][j][0]=='L':#lions
                        if temp[i][j][3]>=self.LMA:#die of old age, must be an adult
                            self.arr[i][j][0]='e'
                            self.stats[0][1]+=1
                            self.stats[0][0]-=1#one less living
                            
                            self.fill(i,j,1,-11)
                        else:
                            if (temp[i][j][1]%10>=6 and temp[i][j][2]==0):#Lion starvation
                                self.arr[i][j][0]='e'
                                if temp[i][j][0]=='L':#if adult lion was starved
                                    self.fill(i,j,1,-11)
                                    self.stats[0][2]+=1
                                    self.stats[0][0]-=1
                                    
                                else:#baby lion was starved
                                    self.fill(i,j,1,-1)
                                    self.stats[1][2]+=1
                                    self.stats[1][0]-=1
                                    
                            else:
                                if self.LND==0:#The Case where we remove natural death
                                    y=2
                                else:
                                    y = randint(1,self.LND)#chance of natural death
                                if y==1:
                                    self.arr[i][j][0]='e'
                                    if temp[i][j][0]=='L':#if adult lion dies naturally
                                        self.fill(i,j,1,-11)
                                        self.stats[0][4]+=1
                                        self.stats[0][0]-=1
                                        
                                    else:#baby lion died naturally
                                        self.fill(i,j,1,-1)
                                        self.stats[1][4]+=1
                                        self.stats[1][0]-=1
                                        
                        
                    else:#antelopes                     
                        if temp[i][j][3]>=self.AMA:#old age
                            self.fill(i,j,2,-11)#it had to be an adult that died of old age
                            self.stats[2][1]+=1
                            self.stats[2][0]-=1
                            self.arr[i][j][0]='e'
                            
                        elif temp[i][j][1]%10>=5: #eat the antelope
                            if temp[i][j][0]=='A':#if it was an adult antelope
                                self.fill(i,j,2,-11)
                                self.stats[2][3]+=1
                                self.stats[2][0]-=1
                                
                            else:#baby eaten
                                self.fill(i,j,2,-1)
                                self.stats[3][3]+=1
                                self.stats[3][0]-=1
                                
                            self.arr[i][j][0]='e'
                        elif temp[i][j][2]%10==8:#starvation
                            if temp[i][j][0]=='A':#if it was an adult antelope
                                self.fill(i,j,2,-11)
                                self.stats[2][2]+=1
                                self.stats[2][0]-=1
                                
                            else:#baby lion starved
                                self.fill(i,j,2,-1)
                                self.stats[3][2]+=1
                                self.stats[3][0]-=1
                                
                            self.arr[i][j][0]='e'
                    #Growth         
                    self.arr[i][j][3]+=1
                    if self.arr[i][j][0]=='l' and self.arr[i][j][3]>=self.LBA:#baby turns to adult
                        self.arr[i][j][0]='L'
                        self.fill(i,j,1,10)
                        self.stats[1][0]-=1
                        self.stats[0][0]+=1
                        
                    if self.arr[i][j][0]=='a' and self.arr[i][j][3]>=self.ABA:#baby turns to adult
                        self.arr[i][j][0]='A'
                        self.fill(i,j,2,10)
                        self.stats[2][0]+=1
                        self.stats[3][0]-=1

#! /usr/bin/python
from tkinter import *
import Project3Info
import tkinter.messagebox
import math#used for the floor function
import copy

class ClearApp(Tk):
    '''where all our GUI is done'''
    def __init__(self,parent=0):
        '''initialising'''
        Tk.__init__(self)
        self.mainWindow=Frame(parent)
        self.mainWindow.pack()
        self.choice()
        self.counter=0
        self.REC='black'#These values are for the playing from file colours
        self.RLC='blue'
        self.RAC='red'
    

    def choice(self):
        '''play recording or continue'''
        self.counter=0
        self.mainWindow.master.title("Choice")
        self.tmp=Frame(self.mainWindow)
        tit=Label(self.tmp,text="What would you like to do?",
                       fg='maroon',font=('courier',15))#This is how we edit our font
        self.cont = Button(self.tmp, text="CONTINUE",
		      width=10,height=2,fg='purple',bg='pink',command=self.GRID)
        self.playback = Button(self.tmp, text="Playback",
		      width=10,height=2,fg='purple',bg='pink',command=self.playb)
        ES = Label(self.tmp,text='What file would you like to playback?',fg='darkgreen',font=('courier',10))
        Buta=Button(self.tmp,text="HELP",
                 width=8,height=2,fg='red',bg='lightgray',command=self.helpchoice)
        self.frames = Entry(self.tmp)
        self.cont.pack()

        ES.pack()
        self.frames.pack()
        self.playback.pack()
        self.tmp.pack()
        Buta.pack(side='right')
        
    def helpchoice(self):
       '''general help for the choice screen'''     
       tkinter.messagebox.showinfo("INFO",'''You can choose to play a previously recorded file or continuing to other options
Note that you must not enter the file extenstion 'txt', it will load automatically''')
    
    def GRID(self):
        '''inputs of grid sizes'''
        self.tmp.forget()
        self.mainWindow.master.title("GRID SIZES")
        self.temp0=Frame(self.mainWindow)
        tit=Label(self.temp0,text="Choose Grid Sizes",
                       fg='maroon',font=('courier',15))#This is how we edit our font
        rower = Label(self.temp0,text='Row Size',fg='darkgreen',font=('courier',12))#Code for a label
        self.rw = Scale(self.temp0, from_=1, to=250,orient=HORIZONTAL)#Code for a slider
        coler = Label(self.temp0,text='Column Size',fg='darkgreen',font=('courier',12))
        self.cl = Scale(self.temp0, from_=1, to=250,orient=HORIZONTAL)
        but=Button(self.temp0,text='NEXT', width=8,height=2,bg='green',pady=1,command=self.click0)
        Buta=Button(self.temp0,text="HELP",
                 width=8,height=2,fg='red',bg='lightgray',command=self.helpGRID)
        #have to pack everything
        tit.pack()
        rower.pack()
        self.rw.pack()
        self.rw.set(10)  # Set the initial value to 10
        coler.pack()
        self.cl.pack()
        self.cl.set(10)  # Set the initial value to 10
        but.pack()
        Buta.pack(side='right')
        self.temp0.pack()
        
    def helpGRID(self):#help message
        '''Gives some general information'''
        tkinter.messagebox.showinfo("INFO",'''These are the inputs that specify the grid that our animals will lie on
To Select size, just slide the sliders to the desired level\n
To move 1 unit at a time, click in the space on the desired side of the slider''')
        
    def click0(self):#We have valid rows and columns
        '''Gets the rows and columns for the grid'''
        self.rows=int(self.rw.get())
        self.col=int(self.cl.get())
        self.Eco=Project3Info.World(self.rows,self.col)#create an instance of the ProjectAltered class
        self.sizer= float(500)/max(self.rows,self.col)
        self.temp0.forget()
        self.part1()
        
    def part1(self):
        '''Changes the probability of each thing in random population'''
        self.mainWindow.master.title("PROBABILITY RATIOS")
        self.temp=Frame(self.mainWindow)
        tit=Label(self.temp,text="Here you can choose the ratio of probability\nthat a block is randomly filled with",
                       fg='maroon',font=('courier',15))
        e = Label(self.temp,text='Empty ratio',fg='darkgreen',font=('courier',12))
        self.em = Entry(self.temp)
        l = Label(self.temp,text='Lion ratio',fg='darkgreen',font=('courier',12))
        self.lm = Entry(self.temp)
        a = Label(self.temp,text='Antelope ratio',fg='darkgreen',font=('courier',12))
        self.am = Entry(self.temp)
        but=Button(self.temp,text='NEXT', width=8,height=2,fg='red',bg='darkgray',command=self.click)
        Buta=Button(self.temp,text="HELP",
                 width=8,height=2,fg='red',bg='lightgray',command=self.helppart1)
        self.em.insert(0,'1')#Store default value
        self.lm.insert(0,'1')
        self.am.insert(0,'1')
        tit.pack()
        e.pack()
        self.em.pack()
        l.pack()
        self.lm.pack()
        a.pack()
        self.am.pack()
        but.pack()
        Buta.pack(side='right')
        self.temp.pack()
        
    def helppart1(self):
        '''More General Information'''
        tkinter.messagebox.showinfo("INFO",'''Each block on the grid is randomised. You can choose
the probability that it will be an empty square, a lion or an antelope''')        
        
    def click(self):
        '''Gets info for the random generation'''
        try:
            self.Eco.emp=int(self.em.get())
            self.Eco.lio=int(self.lm.get())
            self.Eco.ant=int(self.am.get())
            if ((self.Eco.emp<0 or self.Eco.emp>100000) or (self.Eco.lio<0 or self.Eco.lio>100000) or (self.Eco.ant<0 or self.Eco.ant>100000)):
                tkinter.messagebox.showinfo("ERROR!!!","Values must be between 0 and 100000")
            elif (self.Eco.emp==self.Eco.lio==self.Eco.ant==0):
                tkinter.messagebox.showinfo("ERROR!!!","At least one value must be greater than 0")
            else:
                self.temp.forget()#get rid of frame
                self.part2(self.mainWindow)
                self.helper()#this is to complete the frame the first time
        except ValueError:
            tkinter.messagebox.showinfo("ERROR!!!","Invalid Input")
        self.em.delete(0,END)
        self.lm.delete(0,END)
        self.am.delete(0,END)
        self.em.insert(0,'1')#Reset defaults
        self.lm.insert(0,'1')
        self.am.insert(0,'1')

    def helper(self):#Ensures that the following doesnt appear when we use the code the second time
        '''completes the part2 method'''
        but7=Button(self.temp2,text='NEXT',width=10,height=2,fg='red',bg='darkgray',command=self.click7)
        but7.pack()
        self.mainWindow.master.title("CHANGE CONSTANTS")
        Buta=Button(self.temp2,text="HELP",
        width=8,height=2,fg='red',bg='lightgray',command=self.helphelper)
        Buta.pack(side='right')

    def helphelper(self):
        '''More General Information'''
        tkinter.messagebox.showinfo("INFO",'''You can change the constants to numbers that make sense to the programme''')   
        
    def part2(self,frm):
        '''Allows us to change the constants'''
        self.temp2=Frame(frm)
        top=Label(self.temp2,text='() indicates current settings',fg='maroon',font=('courier',14))
        top.pack()
    
        self.e2 = Label(self.temp2,text=('Lion Maximum Age ('+str(self.Eco.LMA)+')'),fg='darkgreen',font=('courier',10))
        self.em2 = Entry(self.temp2)
        but2=Button(self.temp2,text='CHANGE', width=8,height=1,bg='green',command=self.click2)
        self.e2.pack()
        self.em2.pack()
        but2.pack()

        self.e3 = Label(self.temp2,text=('Antelope Maximum Age ('+str(self.Eco.AMA)+')'),fg='darkgreen',font=('courier',10))
        self.em3 = Entry(self.temp2)
        but3=Button(self.temp2,text='CHANGE',width=8,height=1,bg='green',command=self.click3)
        self.e3.pack()
        self.em3.pack()
        but3.pack()

        self.e4 = Label(self.temp2,text=('Lion Breeding Age ('+str(self.Eco.LBA)+')'),fg='darkgreen',font=('courier',10))
        self.em4 = Entry(self.temp2)
        but4=Button(self.temp2,text='CHANGE', width=8,height=1,bg='green',command=self.click4)
        self.e4.pack()
        self.em4.pack()
        but4.pack()

        self.e5 = Label(self.temp2,text=('Antelope Breeding Age ('+str(self.Eco.ABA)+')'),fg='darkgreen',font=('courier',10))
        self.em5 = Entry(self.temp2)
        but5=Button(self.temp2,text='CHANGE', width=8,height=1,bg='green',command=self.click5)
        self.e5.pack()
        self.em5.pack()
        but5.pack()

        self.e6 = Label(self.temp2,text=('Lion Natural Death [1 in x] ('+str(self.Eco.LND)+')\n[0 to turn off Natural Death]'),fg='darkgreen',font=('courier',10))
        self.em6 = Entry(self.temp2)
        but6=Button(self.temp2,text='CHANGE', width=8,height=1,bg='green',command=self.click6)
        self.e6.pack()
        self.em6.pack()
        but6.pack()
        self.temp2.pack(side='right')

    def click2(self):#Lion Maximum Age
        '''Tries to change the Maximum age of lions'''
        try:
            tem=int(self.em2.get())
            if tem<self.Eco.LBA or tem>=100000:
                msg=''.join(['Must be greater than or equal to Lion breeding age, ',str(self.Eco.LBA),', and less than 100000'])
                tkinter.messagebox.showinfo("ERROR!!!",msg)    
            else:
                self.Eco.LMA=tem
                msg=''.join(['Maximum Lion Age changed to ',str(self.Eco.LMA)])
                tkinter.messagebox.showinfo("CHANGED!!!",msg)
                self.e2.configure(text=('Lion Maximum Age ('+str(self.Eco.LMA)+')'),fg='darkgreen',font=('courier',10))#change stored text
        except ValueError:#if the user enters a non-int
            tkinter.messagebox.showinfo("ERROR!!!","Invalid Input")
        self.em2.delete(0,END)
        
    def click3(self):#Antelope maximum age
        '''Tries to change the Maximum age of Antelopes'''        
        try:
            tem=int(self.em3.get())
            if tem<self.Eco.ABA or tem>=100000:#must lie in boundaries
                msg=''.join(['Must be greater than or equal to Antelope breeding age, ',str(self.Eco.ABA),', and less than 100000'])
                tkinter.messagebox.showinfo("ERROR!!!",msg)#A message box    
            else:
                self.Eco.AMA=tem
                msg=''.join(['Maximum Antelope Age changed to ',str(self.Eco.AMA)])
                tkinter.messagebox.showinfo("CHANGED!!!",msg)
                self.e3.configure(text=('Antelope Maximum Age ('+str(self.Eco.AMA)+')'),fg='darkgreen',font=('courier',10))
        except ValueError:
            tkinter.messagebox.showinfo("ERROR!!!","Invalid Input")
        self.em3.delete(0,END)

    def click4(self):#Lion Breeding age
        '''Changes the breeding age of Lions if it fulfills conditions'''
        try:
            tem=int(self.em4.get())
            if tem<2 or tem>self.Eco.LMA:
                msg=''.join([ 'Must be between 2 and Lion Maximum Age,',str(self.Eco.LMA)])
                tkinter.messagebox.showinfo("ERROR!!!",msg)    
            else:
                self.Eco.LBA=tem
                msg=''.join(['Lion Breeding Age changed to ',str(self.Eco.LBA)])
                tkinter.messagebox.showinfo("CHANGED!!!",msg)
                self.e4.configure(text=('Lion Breeding Age ('+str(self.Eco.LBA)+')'),fg='darkgreen',font=('courier',10))
        except ValueError:
            tkinter.messagebox.showinfo("ERROR!!!","Invalid Input")
        self.em4.delete(0,END)

    def click5(self):#Antelope Breeding Age
        '''Changes the breeding age of Antelopes if it fulfills conditions'''
        try:
            tem=int(self.em5.get())
            if tem<2 or tem>self.Eco.AMA:
                msg=''.join([ 'Must be between 2 and Antelope Maximum Age,',str(self.Eco.AMA)])
                tkinter.messagebox.showinfo("ERROR!!!",msg)    
            else:
                self.Eco.ABA=tem
                msg=''.join(['Antelope Breeding Age changed to ',str(self.Eco.ABA)])
                tkinter.messagebox.showinfo("CHANGED!!!",msg)
                self.e5.configure(text=('Antelope Breeding Age ('+str(self.Eco.ABA)+')'),fg='darkgreen',font=('courier',10))
        except ValueError:
            tkinter.messagebox.showinfo("ERROR!!!","Invalid Input")
        self.em5.delete(0,END)

    def click6(self):
        '''Changes the probability of a natural death for a lion'''
        try:
            tem=int(self.em6.get())
            if tem<0 or tem>10000000:
                tkinter.messagebox.showinfo("ERROR!!!",'Must be between 0 and 10000000')    
            else:
                self.Eco.LND=tem
                if tem==0:#Case where we turn Natural Death Off
                    msg='Lion Natural Death turned off'
                    self.e6.configure(text=('Lion Natural Death [1 in x]\n(Currently Off)'),fg='darkgreen',font=('courier',10))
                else:
                    msg=''.join(['Lion Natural Death changed to 1 in ',str(self.Eco.LND)])
                    self.e6.configure(text=('Lion Natural Death [1 in x] ('+str(self.Eco.LND)+')\n[0 to turn off Natural Death]'),fg='darkgreen',font=('courier',10))
                tkinter.messagebox.showinfo("CHANGED!!!",msg)
                
        except ValueError:
            tkinter.messagebox.showinfo("ERROR!!!","Invalid Input")
        self.em6.delete(0,END)
    
    def click7(self):
        '''clears screen and moves to the next one'''
        self.Eco.randy()
        self.Eco2=copy.deepcopy(self.Eco)
        self.temp2.forget()
        self.partN()

    def partN(self):
        '''Presents options, main one being the recording to files'''
        self.mainWindow.master.title("DECISION SCREEN")
        self.fB = Frame(self.mainWindow, border=2, relief="groove")
        self.bNex = Button(self.fB, text="MAIN SIMULATION",
		      width=16,height=2,fg='purple',bg='pink',command=self.inter)
        self.bNex2 = Button(self.fB, text="RECORD",
		      width=10,height=2,fg='purple',bg='pink',command=self.rec)
        GEN = Label(self.fB,text='How many generations to record for?',fg='darkgreen',font=('courier',10)) 
        self.frames = Entry(self.fB)
        GEN2 = Label(self.fB,text='What is the name of the file you want to save to?',fg='darkgreen',font=('courier',10))
        self.frames2 = Entry(self.fB)
        self.bNex.pack()
        main = Button(self.fB, text="MAIN",
		      width=10,height=2,fg='red',bg='darkgray',command=self.main3)

        GEN.pack()
        self.frames.pack()
        GEN2.pack()
        self.fB.pack()
        self.frames2.pack()
        self.bNex2.pack()
        main.pack()
        Buta=Button(self.fB,text="HELP",
                 width=8,height=2,fg='red',bg='lightgray',command=self.helpdec)
        Buta.pack(side='right')
        
    def helpdec(self):
       tkinter.messagebox.showinfo("INFO",'''You can choose to record a file, go to main simulation or going back to the beginning
Enter a positive integer for the number of generations to simulate and specfiy the file you wish to save this to
Note that the '.txt' file extension is automatically added so you should not specify it''')
 
    def inter(self):
        '''intermediate screen'''
        self.Eco=copy.deepcopy(self.Eco2)#Copies original state
        self.mainScr()
        
    def rec(self):
        '''does the recording to files'''
        self.tcount=-1
        try:
            num=int(self.frames.get())#Gets number of frames to simulate
            if num<1:
                raise ValueError
            self.fName=self.frames2.get()+'.txt'#So user does not have to type the extension
            self.fout = open(self.fName,'w')
            #If user tries to write to this file, say its reserved
            self.fout.write(str(self.rows)+' '+str(self.col)+' '+str(num)+'\n')
            for k in range(num):#Store this number of generations
                self.let=self.Eco.arr[1][1][0].upper()#store first block
                self.fout.write(self.let)
                self.tcount=0
                for i in range(1,self.rows+1):
                    for j in range(1,self.col+1):
                        if i==self.rows and j==self.col:#we are at last block and must store its info
                            if self.Eco.arr[i][j][0].upper()==self.let:
                                self.fout.write(str(self.tcount+1))
                            else:
                                self.fout.write(str(self.tcount)+' '+self.Eco.arr[i][j][0].upper()+'1')
                        else:
                            self.compressor(self.Eco.arr[i][j][0])
                self.Eco.check()#simulate one gen
                self.fout.write('\n')
            self.fout.close()            
            tkinter.messagebox.showinfo("SUCCESS!!!",'File Writing Complete')   

        except ValueError:
            tkinter.messagebox.showinfo("ERROR!!!",'Must record for a positive integer of times')
            self.frames.delete(0,END)

    def compressor(self,nex):
        '''helps to store info in the text file'''
        if nex.upper()==self.let:
            self.tcount+=1
        else:
            self.let=nex.upper()
            self.fout.write(str(self.tcount)+' '+self.let)
            self.tcount=1

        
    def main3(self):
        '''used to go back to start screen'''
        self.fB.forget()
        self.choice()
        
                
    def mainScr(self):
        '''used to go to the main simulation screen'''
        self.fB.forget()
        self.part3()
        
    
    def part3(self):
        '''The main simulation screen'''
        self.mainWindow.master.title("SIMULATION")
        self.t2=Frame(self.mainWindow)
        self.t2.pack()
        self.fButtons = Frame(self.mainWindow, border=2, relief="groove")
        self.bNext = Button(self.fButtons, text="NEXT",
		      width=10,height=2,fg='purple',bg='yellow',command=self.gener)
        self.bNext2 = Button(self.fButtons, text="PLAY",
		      width=10,height=2,fg='purple',bg='yellow',command=self.play)
        self.bNext3 = Button(self.fButtons, text="PAUSE",
		      width=10,height=2,fg='purple',bg='yellow',command=self.pause)
        self.bNext4 = Button(self.fButtons, text="RESTART",
		      width=10,height=2,fg='purple',bg='yellow',command=self.restart)
        self.bNext5 = Button(self.fButtons, text="MAIN",
		      width=10,height=2,fg='purple',bg='yellow',command=self.main2)

        self.gen = Label(self.mainWindow,text='GENERATION: 0',fg='purple',font=('courier',15))
        self.gen.pack()
        self.bNext.pack(side='left',padx=1)#This just packs it up so that the 4 buttons lie in a line
        self.bNext2.pack(side='left',padx=1)
        self.bNext3.pack(side='left',padx=1)
        self.bNext4.pack(side='left',padx=1)
        self.bNext5.pack(side='left',padx=1)

        self.fButtons.pack()
        self.t=Frame(self.mainWindow)
        
        self.myCanvas=Canvas(self.t, width = 20+self.sizer*self.col, height=20+self.sizer*self.rows,bg='brown')#where our grid is drawn
        self.myCanvas.bind('<Button-1>', self.clickGrid)#performs the function when grid is clicked
        self.OutCan=Canvas(self.t2, width = 700, height=110,bg='lightgreen',border=3,relief='groove')#Where our stats are ouputed to
        self.part2(self.t)
        Buta=Button(self.temp2,text="HELP",
		      width=8,height=2,fg='red',bg='gray',command=self.help0)
        Buta.pack(side='right')
        self.ESC= 'black'#default values
        self.ALC='blue'
        self.BLC= 'lightblue'
        self.AAC='red'
        self.BAC='pink'
        self.output()
        self.part3A()
        self.colours()
        self.t.pack()
        


    def main2(self):
        '''used to go to the start screen'''
        self.pause()
        self.myCanvas.forget()
        self.fButtons.forget()
        self.t.forget()
        self.t2.forget()
        self.gen.forget()
        self.choice()
        
    def clickGrid(self, event):
        '''Allows to click the grid and get information about a block'''
        if event.x>=12 and event.y>=12 and event.x<8+self.sizer*self.col and event.y<8+self.sizer*self.rows:#checks if cell is actually part of the grid and not the border            
            x=int(math.floor((event.y-12)/self.sizer))+1
            y=int(math.floor((event.x-12)/self.sizer))+1
            if self.Eco.arr[x][y][0]=='e':#Seperate this case so it doesnt say 'of age'
                msg='Empty Square'
                color=self.ESC
            else:#Print Type and age
                if self.Eco.arr[x][y][0]=='a':
                    msg= 'Baby Antelope '
                    color=self.BAC
                elif self.Eco.arr[x][y][0]=='A':
                    msg= 'Adult Antelope '
                    color=self.AAC
                elif self.Eco.arr[x][y][0]=='L':
                    msg= 'Adult Lion '
                    color=self.ALC
                else:
                    msg='Baby Lion '
                    color=self.BLC
                msg+='of age '+str(self.Eco.arr[x][y][3])
            msg+=' surrounded by:\n'
            msg+=str(self.Eco.arr[x][y][1]/10)+' Adult Lion(s)\n'#Surrounding information
            msg+=str(self.Eco.arr[x][y][1]%10-self.Eco.arr[x][y][1]/10)+' Baby Lion(s)\n'
            msg+=str(self.Eco.arr[x][y][2]/10)+' Adult Antelope(s)\n'
            msg+=str(self.Eco.arr[x][y][2]%10-self.Eco.arr[x][y][2]/10)+' Baby Antelope(s)'
            self.myCanvas.create_rectangle(12+(y-1)*self.sizer,
                                           12+(x-1)*self.sizer,
                                           12+self.sizer*(y),
                                           12+self.sizer*(x),fill='white')#to see selected cell
            tkinter.messagebox.showinfo("DETAILS",msg)
            self.myCanvas.create_rectangle(12+(y-1)*self.sizer,
                                           12+(x-1)*self.sizer,
                                           12+self.sizer*(y),
                                           12+self.sizer*(x),fill=color)#return cell to normal

    def help0(self):
        '''More general information'''
        tkinter.messagebox.showinfo("INFO",'''Changing the constants only takes effect when a generation is simulated\n
Breeding age and Adulthood are defined as the same thing, so if breeding age is changed, those adults that are below the new breeding
age will still be adults capable of breeding (Adult can not change to a child).\n
Those that are older than the new maximum age can only die once a generation is simulated\n
Similarly children older than new breeding age only grow up after a generation is simulated\n
Click on the grid to see details of a particular block, the selected block turns white''')

    def partB(self):
       '''The frame that allows us to change colours'''
       self.temp3A=Frame(self.t)
       tit=Label(self.temp3A,text="     Choose Colours      ",
                       fg='maroon',font=('courier',15))
       tit.pack()
       ES = Label(self.temp3A,text='EMPTY SPACE',fg='darkgreen',font=('courier',12))
       self.vary = StringVar(self.temp3A)
       ES.pack()
       self.vary.set("black") # initial value
       #stin='\'black\',
       option = OptionMenu(self.temp3A, self.vary, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       #code of drop-down menu
       option.pack()
       
       AL = Label(self.temp3A,text='LION',fg='darkgreen',font=('courier',12))
       self.var2 = StringVar(self.temp3A)
       AL.pack()
       self.var2.set("blue") # initial value
       option2 = OptionMenu(self.temp3A, self.var2, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       option2.pack()

       BL = Label(self.temp3A,text='ANTELOPE',fg='darkgreen',font=('courier',12))
       self.var3 = StringVar(self.temp3A)
       BL.pack()
       self.var3.set("red") # initial value
       option3 = OptionMenu(self.temp3A, self.var3, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       option3.pack()

       button = Button(self.temp3A, text="OK", width=10,height=2,fg='pink',bg='purple',command=self.ok2)
       button.pack()

    def ok2(self):
        '''change colours of grid'''
        self.REC= self.vary.get()#get all the colours selected in the dropdown menu
        self.RLC=self.var2.get()
        self.RAC= self.var3.get()
        self.shade()
        
    def part3A(self):
       '''The frame that allows us to change colours'''
       self.temp3A=Frame(self.t)
       tit=Label(self.temp3A,text="     Choose Colours      ",
                       fg='maroon',font=('courier',15))
       tit.pack()
       ES = Label(self.temp3A,text='EMPTY SPACE',fg='darkgreen',font=('courier',12))
       self.vary = StringVar(self.temp3A)
       ES.pack()
       self.vary.set("black") # initial value
       option = OptionMenu(self.temp3A, self.vary, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       #code of drop-down menu
       option.pack()
       
       AL = Label(self.temp3A,text='ADULT LION',fg='darkgreen',font=('courier',12))
       self.var2 = StringVar(self.temp3A)
       AL.pack()
       self.var2.set("blue") # initial value
       option2 = OptionMenu(self.temp3A, self.var2, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       option2.pack()

       BL = Label(self.temp3A,text='BABY LION',fg='darkgreen',font=('courier',12))
       self.var3 = StringVar(self.temp3A)
       BL.pack()
       self.var3.set("lightblue") # initial value
       option3 = OptionMenu(self.temp3A, self.var3, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       option3.pack()

       AA = Label(self.temp3A,text='ADULT ANTELOPE',fg='darkgreen',font=('courier',12))
       self.var4 = StringVar(self.temp3A)
       AA.pack()
       self.var4.set("red") # initial value
       option4 = OptionMenu(self.temp3A, self.var4, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       option4.pack()

       BA = Label(self.temp3A,text='BABY ANTELOPE',fg='darkgreen',font=('courier',12))
       self.var5 = StringVar(self.temp3A)
       BA.pack()
       self.var5.set("pink") # initial value
       option5 = OptionMenu(self.temp3A, self.var5, 'black','blue','lightblue','green','lightgreen','red','pink','purple','yellow','gray','orange')
       option5.pack()
       
       button = Button(self.temp3A, text="OK", width=10,height=2,fg='pink',bg='purple',command=self.ok)
       button.pack()
       Buta=Button(self.temp3A,text="HELP",
		      width=8,height=2,fg='red',bg='lightgray',command=self.help5)
       Buta.pack(side='right')#default values
       self.temp3A.pack(side='left')
       
    def help5(self):
        '''More General Information'''
        tkinter.messagebox.showinfo("INFO",'''Select Colours on Dropdown Menu's
and Click OK to change grid colours''')
        
    def ok(self):
        '''change colours of grid'''
        self.ESC= self.vary.get()#get all the colours selected in the dropdown menu
        self.ALC=self.var2.get()
        self.BLC= self.var3.get()
        self.AAC=self.var4.get()
        self.BAC= self.var5.get()
        self.counter-=1
        self.colours()

    def playb(self):
        '''Plays from the text file'''
        try:
            self.fName=self.frames.get()+".txt"
            self.fin = open(self.fName,'r')
            self.tmp.forget()
            self.gen = Label(self.mainWindow,text='GENERATION: 0',fg='purple',font=('courier',15))
            self.gen.pack()
            self.fButtons = Frame(self.mainWindow, border=2, relief="groove")
            self.bNext = Button(self.fButtons, text="NEXT",
		      width=10,height=2,fg='purple',bg='yellow',command=self.next2)
            self.bNext21 = Button(self.fButtons, text="PLAY",
		      width=10,height=2,fg='purple',bg='yellow',command=self.play2)
            self.bNext31 = Button(self.fButtons, text="PAUSE",
		      width=10,height=2,fg='purple',bg='yellow',command=self.pause2)
            self.bNext4 = Button(self.fButtons, text="RESTART",
		      width=10,height=2,fg='purple',bg='yellow',command=self.restart2)
            self.bNext5 = Button(self.fButtons, text="MAIN",
		      width=10,height=2,fg='purple',bg='yellow',command=self.main)
            self.f=Frame(self.fButtons,border=2,relief='groove')
            self.rows2,self.col2,self.run=map(int,self.fin.readline().split())
            self.rw = Scale(self.f, from_=1, to=self.run,orient=HORIZONTAL)#Code for a slider
            self.bNext6 = Button(self.f, text="SKIP TO",
		      width=10,height=2,fg='purple',bg='yellow',command=self.skip)
            self.bNext.pack(side='left',padx=1)#This just packs it up so that the 4 buttons lie in a line
            self.bNext21.pack(side='left',padx=1)
            self.bNext31.pack(side='left',padx=1)
            self.bNext4.pack(side='left',padx=1)
            self.bNext5.pack(side='left',padx=1)

            self.rw.pack()
            self.bNext6.pack()
            self.f.pack(side='left',padx=1)

            self.fButtons.pack()
            self.t=Frame(self.mainWindow,border=2,relief='groove')
            self.t.pack(side='left')
            self.partB()
            self.temp3A.pack(side='right')
            self.colours2()
            Buta=Button(self.fButtons,text="HELP",
		      width=8,height=2,fg='red',bg='lightgray',command=self.helpplay)
            Buta.pack(side='left')#default values
            
        except IOError:
            tkinter.messagebox.showinfo("ERROR!!!","File Not Found")

    def helpplay(self):
        '''More General Information'''
        tkinter.messagebox.showinfo("INFO",'''Displays from selected file
Slider can be used to jump to any of the recorded frames
Colours can be changed from the dropdown menu's''')            
    def skip(self):
        '''alternate use of skiper method'''
        self.skiper(int(self.rw.get()))
               
    def skiper(self,fram):
        '''goes to a place in the file when we use slider menu'''
        self.fin.close()
        self.fin = open(self.fName,'r') 
        for i in range(fram):
            temp=self.fin.readline()
        self.counter=fram-1
        self.next2()
         
    def main(self):
        '''used to go to start screen'''
        self.pause2()
        self.t.forget()
        self.temp3A.forget()
        self.gen.forget()
        self.t2.forget()
        self.fButtons.forget()
        self.choice()
        
    def colours2(self):#after this we are a position we want to be in file
        '''sets up the canvas'''
        self.sizer= float(500)/max(self.rows2,self.col2)
        self.t2=Frame(self.mainWindow)
        self.t2.pack()
        self.myCanvas=Canvas(self.t2, width = 20+self.sizer*self.col2, height=20+self.sizer*self.rows2,bg='brown')#where our grid is drawn
        self.gen.configure(text='GENERATION: '+str(self.counter))#updates what generation it is
        self.next2()

    def pause2(self):
        '''Causes the simulation to pause'''
        self.var0=False#Play will stop
        self.bNext31.configure(bg='green')#shows it is selected
        self.bNext21.configure(bg='yellow')

    def play2(self):
        '''Runs the simulation continously'''
        try:
            self.bNext31.configure(bg='yellow')
            self.bNext21.configure(bg='green')        
            self.var0=True#Only false if pause is selected
            self.generate2()
        except TclError:
            pass
        
    def generate2(self):
        '''The play function runs off this'''
        while self.var0==True:
            self.trial2()

    def trial2(self):
        '''helps the generate function'''
        self.update()
        self.next2()
        
    def restart2(self):
        '''restart method for playing from a file'''
        self.skiper(1)
        self.t2.forget()
        self.counter=0
        self.colours2()
        
    def colours(self):
        '''paints the grid'''
        self.myCanvas.delete(ALL)
        for r in range(1,self.rows+1):
            for c in range(1,self.col+1):
                if self.Eco.arr[r][c][0]=='e':
                    colour = self.ESC
                elif self.Eco.arr[r][c][0]=='L':
                    colour = self.ALC
                elif self.Eco.arr[r][c][0]=='l':
                    colour = self.BLC
                elif self.Eco.arr[r][c][0]=='A':
                    colour = self.AAC
                elif self.Eco.arr[r][c][0]=='a':
                    colour = self.BAC
                self.myCanvas.create_rectangle(12+(c-1)*self.sizer,
                                               12+(r-1)*self.sizer,
                                               12+self.sizer*(c),
                                               12+self.sizer*(r),fill=colour)#make rectangle of corresponding colour
        self.myCanvas.pack(side='left')
        self.counter+=1
        self.gen.configure(text='GENERATION: '+str(self.counter))#updates what generation it is

    def next2(self):
        '''goes to next frame stored in file'''
        if self.counter==self.run:
            self.var0=False#This is to ensure we stop playing when we reach this point
            self.bNext21.configure(bg='yellow')
            tkinter.messagebox.showinfo("ERROR!!!","That is the furthest that was recorded")
        else:
            self.tempy=self.fin.readline().split()
            self.shade()
            self.counter+=1
            if self.counter==self.run:
                self.gen.configure(text='GENERATION: '+str(self.counter)+' (Furthest Recorded)')#updates what generation it is
            else:
                self.gen.configure(text='GENERATION: '+str(self.counter))#updates what generation it is

    def shade(self):
        '''when we use dropdown menus to change colours'''
        s=0
        for i in range(0,len(self.tempy)):
            let=self.tempy[i][:1]
            times=int(str(self.tempy[i][1:]))
            if let=='E':
                colour = self.REC
            elif let=='L':
                colour = self.RLC
            else:
                colour = self.RAC
            for m in range(times):
                self.myCanvas.create_rectangle(12+(s%self.col2)*self.sizer,
                                               12+int(s/self.col2)*self.sizer,
                                               12+self.sizer*((s%self.col2)+1),
                                               12+self.sizer*(int(s/self.col2)+1),fill=colour)#make rectangle of corresponding colour
                s+=1
        self.myCanvas.pack()
        
    def output(self):
        '''Gives detailed stats by filling out the outCan Canvas'''
        self.OutCan.delete(ALL)
        Heads=['Living','Old Age Death','Starvation','Eaten','Natural Death']
        Tails=['Adult Lion','Baby Lion','Adult Antelope','Baby Antelope']
        for c in range(5):
            for r in range(4):
                if c==0:
                    self.OutCan.create_text(45,34+r*20,fill='red',text=Tails[r])
                self.OutCan.create_text(170+c*120,34+r*20,fill='blue',text=self.Eco.stats[r][c])
            self.OutCan.create_text(170+c*120,16,fill='red',text=Heads[c])
        self.OutCan.pack()

    def pause(self):
        '''Causes the simulation to pause'''
        self.var=False#Play will stop
        self.bNext3.configure(bg='green')#shows it is selected
        self.bNext2.configure(bg='yellow')

    def play(self):
        '''Runs the simulation continously'''
        try:
            self.bNext3.configure(bg='yellow')
            self.bNext2.configure(bg='green')        
            self.var=True#Only false if pause is selected
            self.generate()
        except TclError:
            pass
                
    def generate(self):
        '''The play function runs off this'''
        while self.var==True:
            self.trial()

    def trial(self):
        '''helps the generate function'''
        self.update()
        self.gener()
    
    def gener(self):
        '''runs one generation'''
        self.Eco.check()#simulates one generation
        self.colours()
        self.output()

    def restart(self):
        '''restarts the aplication by taking the same state as the start'''
        self.Eco=copy.deepcopy(self.Eco2)#Copies original state
        self.counter=0#resets generation counter
        self.colours()
        self.output()
        self.temp2.forget()
        self.part2(self.t)
        Buta=Button(self.temp2,text="HELP",
		      width=8,height=2,fg='red',bg='gray',command=self.help0)
        Buta.pack(side='right')
app=ClearApp()
app.mainWindow.mainloop()                          

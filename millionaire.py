from tkinter import *
import pygame


pygame.init()
root=Tk()
root.title("Who Wants To Be A Millionaire")
root.geometry('1352x652+0+0')
root.configure(background='black')

#====================================Frames================================#

ABC=Frame(root,bg='black')
ABC.grid()

ABC1=Frame(root,bg='black',bd=20,width=900,height=600)
ABC1.grid(row=0,column=0)

ABC2=Frame(root,bg='black',bd=20,width=452,height=600)
ABC2.grid(row=0,column=1)

ABC1a=Frame(ABC1,bg='black',bd=20,width=900,padx=130,height=200)
ABC1a.grid(row=0,column=0)
ABC1b=Frame(ABC1,bg='black',bd=20,width=900,height=200)
ABC1b.grid(row=1,column=0)
ABC1c=Frame(ABC1,bg='black',bd=20,width=900,height=200)
ABC1c.grid(row=2,column=0)

#====================================Functions================================#

def Change50_50():
    canvas = Canvas(ABC1a,bg="black",width=180,height=80)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='Capture3.PNG')
    canvas.create_image(90,40,image=image1)
    canvas.image=image1
    

def ChangePeople():
    canvas = Canvas(ABC1a,bg="black",width=180,height=80)
    canvas.grid(row=0,column=1)
    canvas.delete("all")
    image1=PhotoImage(file='Capture5.PNG')
    canvas.create_image(90,40,image=image1)
    canvas.image=image1

    
def ChangePhone():
    canvas = Canvas(ABC1a,bg="black",width=180,height=80)
    canvas.grid(row=0,column=2)
    canvas.delete("all")
    image1=PhotoImage(file='Capture7.PNG')
    canvas.create_image(90,40,image=image1)
    canvas.image=image1

    
def MillionPic1():
    canvas = Canvas(ABC2,bg="black",width=430,height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='Picture012.png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1

def MillionPic2():
    canvas = Canvas(ABC2,bg="black",width=430,height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='Picture22.png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1

def MillionPic3():
    canvas = Canvas(ABC2,bg="black",width=430,height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='Picture32.png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1

def MillionPic4():
    canvas = Canvas(ABC2,bg="black",width=430,height=600)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    image1=PhotoImage(file='Picture42.png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1
    
#====================================Images================================#

CentreImage=PhotoImage(file='Capture.PNG')
LogoCentre=Button(ABC1b,image=CentreImage,bg='black',width=300,height=200)
LogoCentre.grid()


Image50=PhotoImage(file='Capture2.PNG')
Live50=Button(ABC1a,image=Image50,bg='black',width=180,height=80,command = Change50_50)
Live50.grid(row=0,column=0)

ImagePeople=PhotoImage(file='Capture4.PNG')
LivePeople=Button(ABC1a,image=ImagePeople,bg='black',width=180,height=80,command = ChangePeople)
LivePeople.grid(row=0,column=1)

ImagePhone=PhotoImage(file='Capture6.PNG')
LivePhone=Button(ABC1a,image=ImagePhone,bg='black',width=180,height=80,command=ChangePhone)
LivePhone.grid(row=0,column=2)

MillionImage=PhotoImage(file='Picture00.png')
MillionImg=Button(ABC2,image=MillionImage,bg='black',width=400,height=600)
MillionImg.grid(row=0,column=0)


#=================================Questions================================#

Question1=StringVar()
Question2=StringVar()
Question3=StringVar()
Question4=StringVar()


Answer1=StringVar()
Answer2=StringVar()
Answer3=StringVar()
Answer4=StringVar()


Question1.set("Q1: What is 1 + 1?")
Answer1.set("22")
Answer2.set("4")
Answer3.set("2")
Answer4.set("9")

def Question2():
    Question1.set("Q1: What is 5 + 5?")
    Answer1.set("10")
    Answer2.set("19")
    Answer3.set("55")
    Answer4.set("0")
    MillionPic1()

def Question3():
    Question1.set("Q1: What is 10 + 10?")
    Answer1.set("3")
    Answer2.set("5")
    Answer3.set("10")
    Answer4.set("20")
    MillionPic2()
    
def Question4():
    Question1.set("Q1: Who is our current president?")
    Answer1.set("Zuma")
    Answer2.set("Motse")
    Answer3.set("Motsepe")
    Answer4.set("Ramaphosa")
    MillionPic3()


def Question5():
    Question1.set("Q1: What colour is the sky?")
    Answer1.set("Blue")
    Answer2.set("Red")
    Answer3.set("Pink")
    Answer4.set("Black")
    MillionPic4()
#=================================Labels,Buttons,Text================================#

txtQuestion=Entry(ABC1c,font=('arial',18,'bold'),bg='blue',fg='white',bd=5,width=44,justify=CENTER, textvariable = Question1)
txtQuestion.grid(row=0,column=0,columnspan=4,pady=4)

lblQuestionA=Label(ABC1c,font=('arial',14,'bold'),text="A: ",bg='black',fg='white',bd=5,justify=CENTER)
lblQuestionA.grid(row=1,column=0,pady=4,sticky=W)
txtQuestion1=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer1,command=Question2)
txtQuestion1.grid(row=1,column=1,pady=4)


lblQuestionB=Label(ABC1c,font=('arial',14,'bold'),text="B: ",bg='black',fg='white',bd=5,justify=LEFT)
lblQuestionB.grid(row=1,column=2,sticky=W)
txtQuestion2=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer2,command=Question4)
txtQuestion2.grid(row=1,column=3,pady=4)

lblQuestionC=Label(ABC1c,font=('arial',14,'bold'),text="C: ",bg='black',fg='white',bd=5,justify=LEFT)
lblQuestionC.grid(row=2,column=0,sticky=W)
txtQuestion3=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer3,command=Question5)
txtQuestion3.grid(row=2,column=1,pady=4)

lblQuestionD=Label(ABC1c,font=('arial',14,'bold'),text="D: ",bg='black',fg='white',bd=5,justify=LEFT)
lblQuestionD.grid(row=2,column=2,sticky=W)
txtQuestion4=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer4,command=Question3)
txtQuestion4.grid(row=2,column=3,pady=4)


root.mainloop()

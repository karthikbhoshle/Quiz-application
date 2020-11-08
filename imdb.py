import tkinter
from tkinter import *
import random
import sys
from PIL import ImageTk, Image
def ex():
    sys.exit()
questions=['Which of this not a keyword in python?',
           'Total number of key-word in python?',
           'Who is the creator of Python?',
           'what is output of below code?\nprint(print(\'hello\',end=' '))',
           'what is output of below code?\nst=\'python\'\nprint(st[2:])',
           'Which is the input function in python ?',
           'what is output of below code?\nl1=l2=[2,3,4]\nprint(id(l1)==id(l2))',
           'Does Python support OOP?',
           'Which keyword is used to create a function?',
           'Which year Python was released ?'
           ]
choice=[['switch','for','else','try'],
        ['34','33','32','43'],
        ['Dennis Ritchie','James Gosling','Guido van Rossum','Brendan Eich'],
        ['hello None','None','Error','hello'],
        ['thon','python','pthon','Error'],
        ['str()','input()','id()','print()'],
        ['false','False','True','true'],
        ['Not-at-all','Maybe','No','Yes'],
        ['continue','return','pass','def'],
        ['1991','1995','2001','1985']]
useranswer=[]
correct_answer=[0,1,2,0,0,1,2,3,3,0]
index=[]
global t
t=21
def showresult(n):
    l4.destroy(); r11.destroy(); r12.destroy(); r13.destroy(); r14.destroy(),l5.destroy()
    l6=Label(root,text='Your Total Score = '+str(n),foreground='#FACA2F',background='#000000',font=('Consolas',27),width=500,justify='center',wraplength=400)
    l6.pack()
    b=Button(root,text='Enter to Exit',foreground='#FACA2F',background='#000000',font=('Consolas',10),justify='center',command=ex)
    b.pack()

def gen():
    global index
    while len(index)<10:
          x=random.randint(0,9)
          if x in index:
              continue
          else:
              index.append(x)
def cal():
    global useranswer,correct_answer
    n=0

    for i in range(len(index)):
        n=n+1 if correct_answer[index[i]]==useranswer[i] else n
        #p+=1
    showresult(n)
def selected():
    global r1,useranswer,l4,r11,r12,r13,r14,t
    x = r1.get()
    useranswer.append(x)
    r1.set(-1)
    #x=r1.get()
    #useranswer.append(x)
    if len(useranswer)<10:

        l4.config(text=questions[index[len(useranswer)]])
        r11.config(text=choice[index[len(useranswer)]][0])
        r12.config(text=choice[index[len(useranswer)]][1])
        r13.config(text=choice[index[len(useranswer)]][2])
        r14.config(text=choice[index[len(useranswer)]][3])
        t=21

    else:
        cal()

def time():
    global l5,t
    if t>0:
        t-=1
        l5.config(text='Time-Left\n' + str(t))

    if t==0:
        selected()
    l5.after(1000, time)



def Quizz():
    global l4,r11,r12,r13,r14,l5
    l4=Label(root,text=questions[index[0]],fg='red',background='white',font=('Consolas',16),width=500,justify='center',wraplength=400)
    l4.pack()
    global r1
    r1=IntVar()
    r1.set(-1)
    r11=Radiobutton(root,text=choice[index[0]][0],fg='green',background='white',font=('Consolas',16),value=0,wraplength=400,variable=r1,command=selected)
    r11.pack(pady=5)
    r12 = Radiobutton(root, text=choice[index[0]][1],fg='green',background='white', font=('Consolas', 16),wraplength=400,value=1, variable=r1,command=selected)
    r12.pack(pady=5)
    r13 = Radiobutton(root, text=choice[index[0]][2],fg='green',background='white', font=('Consolas', 16),wraplength=400, value=2, variable=r1,command=selected)
    r13.pack(pady=5)
    r14 = Radiobutton(root, text=choice[index[0]][3],fg='green',background='white', font=('Consolas', 16),wraplength=400, value=3, variable=r1,command=selected)
    r14.pack(pady=5)
    l5 = Label(root, text='Time-Left\n' + str(t),fg='blue', background='white', font=('Consolas', 16), width=500,
               justify='center')
    l5.pack()
    time()
def Start():
    l1.destroy()
    b1.destroy()
    l2.destroy()
    l3.destroy()
    gen()
    Quizz()
root=tkinter.Tk()
root.title("QUIZ Application")
root.geometry('700x600')
root.configure(background='white')
root.resizable(False,False)

'''img = PhotoImage(file='C:\\Users\\DELL\\Pictures\\python.gif')
panel = Canvas(root)
panel.create_image(0,0,image=img)

panel.pack()'''
l1=Label(root,text='Simple Quiz on Python',background='white',font=('Comic sans Ms',24,'bold'))
l1.pack()
b1=Button(root,text='Start',width=10,font=('Comic sans Ms',15,'bold'),command=Start)
b1.pack()
l2=Label(root,text='Read The Rules And\nClick Start Once You Are Ready.',background='white',font=('Comic sans Ms',10,'bold'),justify='center')
l2.pack()
l3=Label(root,text='This quiz contains 10 questions\nYou will get 20 seconds to solve a Question\nOnes you select a radio button that will be a final choice\nhence think before you select.',width=100,foreground='#FACA2F',background='#000000',font=('times ',14))
l3.pack()
root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:59:30 2019

@author: HASEE
"""

from tkinter import *
import tkinter.messagebox as mbox
import random
class game_gui(Frame):
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.wrong_answer=0
        self.var=Variable()
        self.var_list=Variable()
        self.var_result=Variable()

        self.result=[]
        self.answer_list=[]
        self.current_answer_list=[]
        self.right_answer_count=0
        self.question_num=0
        #self.Label=Label(frame)#,text=self.puzzle)
       
        self.Label=Label(frame,textvariable=self.var)
        self.Label.grid(row=0,column=1,sticky=W)

        self.Label_2=Label(frame,text="wrong answer count: %d"%self.wrong_answer)
        self.Label_2.grid(row=7,column=0,sticky=W)

        self.entry=Entry(frame,text=self.var_result)
        self.entry.grid(row=0,column=2,sticky=W)
        
        self.Label_1=Label(frame)#,text=self.answer_list)
        self.Label_1.grid(row=8,column=0,sticky=W)
        self.get_problem()
        self.button1=Button(frame,text="check answer",command=self.check_answer,fg="orange")
        self.button1.grid(row=1,column=2,sticky=W)
        
        self.button2=Button(frame,text="exit",command=self.exit,fg="blue")
        self.button2.grid(row=5,column=6,sticky=W)


        self.button3=Button(frame,text="New Math Problem",command=self.get_problem,fg="green")
        self.button3.grid(row=2,column=2,sticky=W)
        
        self.exit=frame
    def check_answer(self):
        if self.result==eval(self.entry.get()):
            mbox.showinfo("right","you have got right answer!")
            self.entry["state"]="readonly"
            self.right_answer_count+=1
        else:
            mbox.showinfo("wrong","your's answer is wrong ,please cal again")
            self.answer_list.append(self.entry.get())
            self.current_answer_list.append(self.entry.get())
            self.Label_1["text"]=self.current_answer_list
            self.wrong_answer+=1
            self.Label_2["text"]="wrong answer count: %d"%self.wrong_answer
            self.entry.delete(0,'end')
    def exit(self):
        #
        print("the history of numbers : %s, the number solved : %d"%(self.question_num,self.right_answer_count))
        print(self.answer_list)
        print("the average number of incorrect answer attempts per problem: %f"%((len(self.answer_list)-self.question_num)/self.question_num))
        self.exit.destroy()
        

    def get_problem(self):
        self.question_num+=1
        op=["+","-","*","/"]
        operation=random.choice(op)
        if operation=="*":
            a=random.randint(1,99)
            b=random.randint(1,99)
            result=a*b
        elif operation=="+":
            a=random.randint(0,1000)
            b=random.randint(0,1000)
            result=a+b
        elif operation=="-":
            a=random.randint(0,1000)
            b=random.randint(0,1000)
            result=a-b#a<b
            if result<0:
                temp=b
                b=a
                a=temp
            result=a-b
        elif operation=="/":
            a=random.randint(0,1000)
            b=random.randint(1,1000)
            while(a%b!=0):
                a=random.randint(0,1000)
                b=random.randint(1,1000)
            result=int(a/b)
        puzzle="%d%s%d="%(a,operation,b)
        if puzzle in self.answer_list:
            mbox.showinfo("please press one more time on the New Math Button!cause the puzzle already appeared before!")
            return 0
        self.current_answer_list=[]
        self.wrong_answer=0
        self.result=result
        self.answer_list.append(puzzle)
        self.var.set(puzzle)
        self.Label_1["text"]=""
        self.entry["state"]="normal"
        self.Label_2["text"]="wrong answer count: %d"%0
        self.entry.delete(0,'end')
        self.var_list.set(self.answer_list)
        #self.Label.config(text=puzzle)
        #return result
        
root=Tk()
root.title("Math Game")
root.geometry("600x250")
app=game_gui(root)
root.mainloop()

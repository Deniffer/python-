import random
import turtle

file_name="wordlist.txt"
state=[0]
letter_case=["a","o","i","u","e"]

def open_file(file):
    with open(file,mode='r') as f:
        lst=f.readlines()
        return lst[random.randint(0,len(lst))]
    
def go_to(x, y, p):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(p)
    turtle.pendown()
    
def hang():
    turtle.speed(0)
    if state[0]==0:
        go_to(-300,0,0)
        turtle.forward(600)
        go_to(-100,0, 90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(25)
    elif state[0]==1:
        go_to(0, 150, 0)
        turtle.circle(12.5)
    elif state[0]==2:
        go_to(0,150, -90)
        turtle.forward(50)
    elif state[0]==3:
        go_to(0,140, -45)
        turtle.forward(25)
        go_to(0,140, -135)
        turtle.forward(25)
    elif state[0]==4:
        go_to(0,100, -45)
        turtle.forward(25)
        go_to(0,100, -135)
        turtle.forward(25)
    state[0]+=1
    return 0

def spaces(word):
    l=len(word)
    if l %2 !=0:
        go_to(-5-(l//2*20) - (l//2*10), -150, 0)
        for i in range(l):
            turtle.forward(20)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
    else:
        go_to(-(l//2*20) - (l//2*10), -150, 0)
        for i in range(l):
            turtle.forward(20)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()

def error(word, char):
    go_to(-5-(len(word)//2*20) - (len(word)//2*10), -200, 0)
    turtle.penup()
    for j in range(state[0]):
        turtle.forward(20)
    turtle.pendown()
    turtle.write(char, align='center', font=("Arial",16, "bold"))
    hang()
def point(word, char, i):
    go_to(-5-(len(word)//2*20) - (len(word)//2*10), -150, 0)
    turtle.penup()
    for j in range(i):
        turtle.forward(20)
        turtle.forward(10)
    turtle.forward(10)
    turtle.pendown()
    turtle.write(char, align='center', font=("Arial", 30, "normal"))
    
def play(word, out):
    ch=input(r"please input one guess character!:")
    key=''
    keylist = [chr(i) for i in range(97, 123)]
    while len(ch)!=1 or ch not in keylist :
        print("invalid input guess letter ,please input again!! ")
        print("Note:input one specific  lo wer case letter per time!")
        ch=input(r"please input one guess character!:")
    if ch in word:
        for i in range(len(word)):
            if ch==word[i]:
                key+=ch
                point(word, ch, i)
            else:
                key+=out[i]
        return key
    else:
        error(word, ch)
        return out

def game_ask():
    ask=True
    while(ask):
        ask=input("would you like to paly one more time? (y/n):")
        if ask=="Y" or ask=="y":
            ask=True
            #turtle.exitonclick()
            break
        elif ask =="N" or ask =="n":
            ask=False
            #turtle.exitonclick()
            break
        else:
            print("invalid input ,please input again!")
    return ask
def main():
    playing=True
    global state
    while(playing):
        import turtle
        word=open_file(file_name).strip('\n').lower()       
        #print(word)
        spaces(word)
        out=''
        for i in range(len(word)):
            if word[i] not in letter_case:
                out+='_'
            else:
                out+=word[i]
                point(word,word[i],i)
        while out != word and state[0]<=4:
            print(out)
            out=play(word, out)
        if state[0] > 4:
            print('You have run out your turn!')
            turtle.bgcolor('black')
            turtle.bye()
            playing=game_ask()
            state=[0]
            #game_ask()
        else:
            print('Congratulation!!! you have cracked the word!!and the word was ' + word + '!')
            playing=game_ask()
            state=[0]
            turtle.bye()
            #game_ask()
        
    print("game over!")
if __name__ == '__main__':
    main()
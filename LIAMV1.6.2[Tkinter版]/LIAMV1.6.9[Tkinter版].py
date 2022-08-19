from tkinter import *
import datetime
import time
import aiml
import threading
from flask import Flask, render_template, request              
import sqlite3
import datetime
import requests  
import json
root= Tk()
root.title('LIAM&小泮')
root.geometry('800x600')

global n,m,mm,xuexi,ask
n=False
ask=True
xuexi=False
m=True
def run1():
    global n,m,mm,xuexi,ask
    global n
    global m
    global a
    a = inp1.get()
    txt.see("end")
    inp1.delete(0, END)
    txt.see("end")
    
    

    if n and m:
         #a = inp1.get()
         #b = float(inp2.get())
         #s = liam(a)
         #dun()
         if ask:#如果是选菜单
             zhuanhua(a)
             time.sleep(0.2)
             m=False
             ask=False
             
         #else:
        
             
    elif m==False:#如果是输入liam内容
        if xuexi==False:
            liam1(a)
        else :
            xuexi1(mm,a)
        
       
    else :
         kaiji()
         xunwen()

         n=True

def xuexi1(ask,ii):
                                                             global xuexi
    
                                                             f = open("xuexi.aiml",encoding = "utf-8")#删除</aiml>
                                                             lines = f.readlines()
                                                             f.close()
                                                             f = open("xuexi.aiml", "w",encoding = "utf-8")
                                                             f.writelines([item for item in lines[:-1]])
                                                             f.close()
                                                             f = open("xuexi.aiml", "a",encoding = "utf-8")
                                                             f.write('\r\n')
                                                             f.write('\r\n')
                                                             f.write('\r\n')
                                                             f.write('<category>\r\n')
                                                             f.write('<pattern>%s</pattern>\r\n'%ask)
                                                             f.write('<template>\r\n')
                                                             f.write('<srai>%s</srai>\r\n'%ii)
                                                             f.write('</template>\r\n')
                                                             f.write('</category>\r\n')

                                                             f.write('\r\n')
                                                             f.write('\r\n')
                                                             f.write('<category>\r\n')
                                                             f.write('<pattern>%s</pattern>\r\n'%ii)
                                                             f.write('<template>%s</template>\r\n'%ii)
                                                             f.write('</category>\r\n')
                                                             f.write('\r\n')
                                                             f.write('</aiml>')
                                                             
                                                             f.close()
                                                             txt.insert(INSERT,"\n")
                                                             txt.insert(END,'学习成功！')
                                                             txt.see("end")
                                                             xuexi=False
                                                             
    
def zhuanhua(q):
    if '1'<=q<='9':

            if q=='1':
                global w
                w=0
                for i in range(10):
                    time11(i)
            elif q=='9':
                jiazai()
                global xuexi
                xuexi=False
            elif q=='3':
                dun()
                
                
            else:
                txt.insert(INSERT,"\n")
                txt.insert(END,'输入有误，请重试！')
    else:
        txt.insert(INSERT,"\n")
        txt.insert(END,'输入有误，请重试！')
                
        
            
    inp1.delete(0, END)
    
def jiazai():
    '''k = aiml.Kernel()
    k.learn("cn-startup1.xml")
    k.respond("load aiml cn")
    k.respond("start")
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'
    txtx=""'''
    
    txt.insert(END,'下面开始基本询问交互，可在回答完‘你最喜欢什么颜色后开始发挥’：')
    txt.insert(INSERT,"\n")
    txt.insert(END,'你好！我是LIAM，想问我什么呢？')

    txt.see("end")
def time11(w):
    
    s='计算中，请稍后'+'----'*w
    txt.insert(INSERT,'\n')
    txt.insert(END,s)
    txt.insert(INSERT,'\n')
    txt.see("end")#自动滚动txt成功
    #txt.update_idletasks()
    #txt.after(1000,refreshText)
    
def refreshText():#企图自动滚动txt
    global i
    i += 1
    text1.delete(0.0,tk.END)
    text1.insert(tk.INSERT,i)
    text1.update()
    windows.after(1000,refreshText)
def liam(txtx):
     
     #t2= threading.Thread(target=jiazai1)
     #jiazai1()
     
     #time.sleep(3)
     t1= threading.Thread(target=liam1,args=(txtx,))#此处全是问题
     
     #t2.daemon = False
     #t2.start()
     t1.start()
     #liam1()
     #t2.join()
     #t1.join()
     #jiazai1()
     #liam1(txtx)

def liam1(txtx):
    global n,m,mm,xuexi,ask
   
    
    time_str=datetime.datetime.now()
    t= datetime.datetime.strftime(time_str,'%Y-%m-%d %H:%M:%S')
    txt.insert(INSERT,"\n")
    txt.insert(INSERT,"\n")
    txt.insert(INSERT,"\n")#INSERT索引表示插入光标当前的位置
    txt.insert(END,t)
    txt.insert(INSERT,"\n")
    txt.insert(END,"我: ")
        
         
    txt.insert(END,txtx)
    
    
    '''k = aiml.Kernel()
    #k = aiml.Kernel()
    k.learn("cn-startup1.xml")
    k.respond("load aiml cn")
    #k.respond("start")
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hard to guess string"'''
    robot_text = k.respond(txtx)
    mm=txtx
    if robot_text !='':

        time_str=datetime.datetime.now()
        t= datetime.datetime.strftime(time_str,'%Y-%m-%d %H:%M:%S')
        

        

        r=robot_text
        conn=sqlite3.connect('LDT.db')
        cur=conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS "LDT"(DATE BLOB,MYSG BLOB,RSG BLOB)')
        cur.execute("INSERT INTO LDT(DATE,MYSG,RSG) VALUES(?,?,?)",(t,mm,r))
        conn.commit()
        cur.close()

        txt.insert(INSERT,"\n") #INSERT索引表示插入光标当前的位置
        txt.insert(END,t)
        txt.insert(INSERT,"\n")
        txt.insert(END,'LIAM:  ')


    
        txt.insert(END,r)
        inp1.delete(0, END)# 清空输入
        txt.see("end")

    else:
         txt.insert(INSERT,'\n')
         txt.insert(END,'我该怎么回答呢？')
         txt.see("end")
         inp1.delete(0, END)
        
         xuexi=True
         
         
         
        
       
def kaiji():
   
    txt.insert(INSERT,"\n")
    txt.insert(END,'恭喜你发现了宝藏!!')
    
    txt.insert(INSERT,"\n")
    txt.insert(END,'恭喜宝藏发现了你!!')
    

    txt.insert(INSERT,"\n")
    txt.insert(END,'加载模块中,请稍后')
    inp1.delete(0, END)
    txt.see("end")
    
    #t2= threading.Thread(target=jiazai1)
    #jiazai1()
     
    #time.sleep(3)
     #t1= threading.Thread(target=liam1,args=(txtx,))#此处全是问题
     
    #t2.daemon = False
    #t2.start()
     #t1.start()
    
    
def dun():
        import turtle
        print(' 请切换页面观看,并在完成后关闭')

        #turtle.title('冰墩墩2022')

        turtle.speed(1000)  # 速度

        # 左手
        turtle.penup()
        turtle.goto(177, 112)
        turtle.pencolor("lightgray")
        turtle.pensize(3)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(80)
        turtle.circle(-45, 200)
        turtle.circle(-300, 23)
        turtle.end_fill()

        # 左手内
        turtle.penup()
        turtle.goto(182, 95)
        turtle.pencolor("black")
        turtle.pensize(1)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.setheading(95)
        turtle.pendown()
        turtle.circle(-37, 160)
        turtle.circle(-20, 50)
        turtle.circle(-200, 30)
        turtle.end_fill()
        # 轮廓
        # 头顶
        turtle.penup()
        turtle.goto(-73, 230)
        turtle.pencolor("lightgray")
        turtle.pensize(3)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(20)
        turtle.circle(-250, 35)
        # 左耳
        turtle.setheading(50)
        turtle.circle(-42, 180)
        # 左侧
        turtle.setheading(-50)
        turtle.circle(-190, 30)
        turtle.circle(-320, 45)
        # 左腿
        turtle.circle(120, 30)
        turtle.circle(200, 12)
        turtle.circle(-18, 85)
        turtle.circle(-180, 23)
        turtle.circle(-20, 110)
        turtle.circle(15, 115)
        turtle.circle(100, 12)
        # 右腿
        turtle.circle(15, 120)
        turtle.circle(-15, 110)
        turtle.circle(-150, 30)
        turtle.circle(-15, 70)
        turtle.circle(-150, 10)
        turtle.circle(200, 35)
        turtle.circle(-150, 20)
        # 右手
        turtle.setheading(-120)
        turtle.circle(50, 30)
        turtle.circle(-35, 200)
        turtle.circle(-300, 23)
        # 右侧
        turtle.setheading(86)
        turtle.circle(-300, 26)
        # 右耳
        turtle.setheading(122)
        turtle.circle(-53, 160)
        turtle.end_fill()

        # 右耳内
        turtle.penup()
        turtle.goto(-130, 180)
        turtle.pencolor("black")
        turtle.pensize(1)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(120)
        turtle.circle(-28, 160)
        turtle.setheading(210)
        turtle.circle(150, 20)
        turtle.end_fill()

        # 左耳内
        turtle.penup()
        turtle.goto(90, 230)
        turtle.setheading(40)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(-30, 170)
        turtle.setheading(125)
        turtle.circle(150, 23)
        turtle.end_fill()

        # 右手内
        turtle.penup()
        turtle.goto(-180, -55)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.setheading(-120)
        turtle.pendown()
        turtle.circle(50, 30)
        turtle.circle(-27, 200)
        turtle.circle(-300, 20)
        turtle.setheading(-90)
        turtle.circle(300, 14)
        turtle.end_fill()

        # 左腿内
        turtle.penup()
        turtle.goto(108, -168)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(-115)
        turtle.circle(110, 15)
        turtle.circle(200, 10)
        turtle.circle(-18, 80)
        turtle.circle(-180, 13)
        turtle.circle(-20, 90)
        turtle.circle(15, 60)
        turtle.setheading(42)
        turtle.circle(-200, 29)
        turtle.end_fill()
        # 右腿内
        turtle.penup()
        turtle.goto(-38, -210)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(-155)
        turtle.circle(15, 100)
        turtle.circle(-10, 110)
        turtle.circle(-100, 30)
        turtle.circle(-15, 65)
        turtle.circle(-100, 10)
        turtle.circle(200, 15)
        turtle.setheading(-14)
        turtle.circle(-200, 27)
        turtle.end_fill()

        # 右眼
        # 眼圈
        turtle.penup()
        turtle.goto(-64, 120)
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(40)
        turtle.circle(-35, 152)
        turtle.circle(-100, 50)
        turtle.circle(-35, 130)
        turtle.circle(-100, 50)
        turtle.end_fill()
        # 眼珠
        turtle.penup()
        turtle.goto(-47, 55)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(25, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-45, 62)
        turtle.pencolor("darkslategray")
        turtle.fillcolor("darkslategray")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(19, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-45, 68)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(10, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-47, 86)
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(5, 360)
        turtle.end_fill()

        # 左眼
        # 眼圈
        turtle.penup()
        turtle.goto(51, 82)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(120)
        turtle.circle(-32, 152)
        turtle.circle(-100, 55)
        turtle.circle(-25, 120)
        turtle.circle(-120, 45)
        turtle.end_fill()
        # 眼珠
        turtle.penup()
        turtle.goto(79, 60)
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(24, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(79, 64)
        turtle.pencolor("darkslategray")
        turtle.fillcolor("darkslategray")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(19, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(79, 70)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(10, 360)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(79, 88)
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(5, 360)
        turtle.end_fill()

        # 鼻子
        turtle.penup()
        turtle.goto(37, 80)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(-8, 130)
        turtle.circle(-22, 100)
        turtle.circle(-8, 130)
        turtle.end_fill()

        # 嘴
        turtle.penup()
        turtle.goto(-15, 48)
        turtle.setheading(-36)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(60, 70)
        turtle.setheading(-132)
        turtle.circle(-45, 100)
        turtle.end_fill()

        # 彩虹圈
        turtle.penup()
        turtle.goto(-135, 120)
        turtle.pensize(5)
        turtle.pencolor("cyan")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-165, 150)
        turtle.circle(-130, 78)
        turtle.circle(-250, 30)
        turtle.circle(-138, 105)
        turtle.penup()
        turtle.goto(-131, 116)
        turtle.pencolor("slateblue")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-160, 144)
        turtle.circle(-120, 78)
        turtle.circle(-242, 30)
        turtle.circle(-135, 105)
        turtle.penup()
        turtle.goto(-127, 112)
        turtle.pencolor("orangered")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-155, 136)
        turtle.circle(-116, 86)
        turtle.circle(-220, 30)
        turtle.circle(-134, 103)
        turtle.penup()
        turtle.goto(-123, 108)
        turtle.pencolor("gold")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-150, 136)
        turtle.circle(-104, 86)
        turtle.circle(-220, 30)
        turtle.circle(-126, 102)
        turtle.penup()
        turtle.goto(-120, 104)
        turtle.pencolor("greenyellow")
        turtle.pendown()
        turtle.setheading(60)
        turtle.circle(-145, 136)
        turtle.circle(-90, 83)
        turtle.circle(-220, 30)
        turtle.circle(-120, 100)
        turtle.penup()

        # 爱心
        turtle.penup()
        turtle.goto(220, 115)
        turtle.pencolor("brown")
        turtle.pensize(1)
        turtle.fillcolor("brown")
        turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(36)
        turtle.circle(-8, 180)
        turtle.circle(-60, 24)
        turtle.setheading(110)
        turtle.circle(-60, 24)
        turtle.circle(-8, 180)
        turtle.end_fill()

        # 五环
        turtle.penup()
        turtle.goto(-5, -170)
        turtle.pendown()
        turtle.pencolor("blue")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(10, -170)
        turtle.pendown()
        turtle.pencolor("black")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(25, -170)
        turtle.pendown()
        turtle.pencolor("brown")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(2, -175)
        turtle.pendown()
        turtle.pencolor("lightgoldenrod")
        turtle.circle(6)
        turtle.penup()
        turtle.goto(16, -175)
        turtle.pendown()
        turtle.pencolor("green")
        turtle.circle(6)
        turtle.penup()

        turtle.pencolor("black")
        turtle.goto(-16, -160)
        turtle.write("BEIJING 2022", font=('Arial', 16, 'bold italic'))
        turtle.hideturtle()

        turtle.mainloop()
        print('huizhichenggoing')

def xunwen():
    txt.insert(INSERT,'\n')
    txt.insert(END,"1，计算时间。2，查询计算机硬件价格。3.一墩难求。")
    txt.insert(INSERT,'\n')
    #txt.insert(END,' 4.原神辅助工具。5，括号判断计算。6,求最大公约数。7,最炫民族风。8.约瑟夫环（选猴子王）')
    txt.insert(INSERT,'\n')    
    txt.insert(END,'9.LIAM聊天机器人/小泮机器人,10.留言板')
    txt.see("end")
lb1 = Label(root, text='欢迎来到LIAM&小泮')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0, rely=0.8, relwidth=0.8, relheight=0.1)


# 直接调用 run1()
btn1 = Button(root, text='发送', command=run1)
btn1.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.1)

txt = Text(root)
'''scrollBar = Scrollbar(txt)
scrollBarx =Scrollbar(txt, orient=HORIZONTAL)
#yscrollcommand=scrollBar.set,xscrollcommand=scrollBarx.set
#靠右，充满Y轴
scrollBar.pack(side=RIGHT, fill=Y)
#靠下，充满X轴
scrollBarx.pack(side=BOTTOM,fill=X)
scrollBar.config(command=treeview.yview)
scrollBarx.config(command=txt.xview)'''
txt.place(rely=0.1, relheight=0.6,relwidth=1)
#txt1=Canvas(txt)
#scrollBar = Scrollbar(txt)
#scrollBarx =Scrollbar(txt, orient=HORIZONTAL)
scrollBar = Scrollbar(root, command=txt.yview)
scrollBar.pack(side=RIGHT, fill=Y)

txt.configure(yscrollcommand = scrollBar.set)
#txt.bind('<Configure>', on_configure)

#txt.configure(yscrollcommand = scrollbar.set)
root.resizable(False, False)
time_str=datetime.datetime.now()
t= datetime.datetime.strftime(time_str,'%Y-%m-%d %H:%M:%S')
 #INSERT索引表示插入光标当前的位置
txt.insert(END,t)
txt.insert(INSERT,"\n")
txt.insert(END,"LIAM&小泮（Tkinter版）V1.4.2 版权归liam所有,单击‘发送’以开机")
root.attributes("-topmost",1)#窗口置顶
k = aiml.Kernel()
#k = aiml.Kernel()
k.learn("cn-startup1.xml")
k.respond("load aiml cn")
#k.respond("start")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
root.mainloop()



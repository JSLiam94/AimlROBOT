# LIAM泮泣 
### 开发日志 :point_up: 

LIAM带有简易学习功能，目前学习只能一句话对应一个回答，语料库在本地</br>
小泮(小Q)为青云客开源机器人，需联网

测试前检查xuexi.aiml文件是否完整
开头是否有

    <?xml version="1.0" encoding="UTF-8"?>

    <aiml version="1.0">

    <!-- Free software (c) 2012 andelf -->
    <!-- This program is open source code released under -->
    <!-- the terms of the GNU General Public License -->
    <!-- as published by the Free Software Foundation. -->

    <meta name="author" content="Andelf"/>
    <meta name="language" content="zh"/>

如果无，需添加（支持aiml库原作者）


每次在询问并回答完“你叫什么名字？”后可开始根据语料库交流</br>
每次在询问并回答完“你喜欢什么颜色？”后可开始自由交互及学习</br>
LIAM中输入exit退出（目前终端版本实现，Tkinter版本开发中）

LDT.db文件为聊天记录，会自动创建



###   ——2022.5.21 LIAM 
## 内容自检 :point_down: ：

文件夹：</br>
build</br>
chinese #LIAM所有中文语料库</br>
chinese-some #LIAM部分中文语料库</br>
dist #应用程序备份</br>
english #LIAM所有英文语料库</br>

主文件：</br>
ai.aiml #LIAM英文语料库其一</br>
cn-startup.xml #LIAM完整语料库学习文件</br>
cn-startup1.xml #LIAM部分语料库学习文件</br>
liam[启动程序].exe</br>
xuexi.aiml #LIAM学习中语料库</br>


liamV1.4.2完整版本为娱乐版本，对其中部分功能（如时间，价格计算）请勿较真</br>
	精简版[实用版本]开发中，敬请期待……</br></br>
## 墨染测试 :v: ：</br>
	发现human_text在首次input为空时报错</br>，
#解决方法1：</br>
	提前使之不为空，（暴力）‘+’</br>
#解决方法二：</br>
	检测语句，为空时提示重新输入</br>
## LIAM测试 :ok_hand: ：
	#pyinstaller在win10x64环境下打包的.exe文件在win732位中无法运行
## ————2022.8.7




### LIAM[Tkinter版]初步功能开发成功，期间困难与解决方案 :raised_hands: ：
##### 1.tk界面创建，GUI布置困难： </br>
        txt.place(rely=0.1, relheight=0.6,relwidth=1)
        
            #绝对位置，但是只需要界面百分比，更方便
        root.mainloop()

##### 2.txt模块自动滚动显示最新文本实现</br>
        txt.see("end")</br>
##### 3.实现滚动条与txt区块同步</br>
        scrollBar = Scrollbar(root, command=txt.yview)
        scrollBar.pack(side=RIGHT, fill=Y)#实现滚动条GUI
        txt.configure(yscrollcommand = scrollBar.set)

##### 4.清空entry框内容：
        inp1.delete(0, END)
#### 5.LIAM无法运行，经检查，原因如下 :+1: ：</br>
        k = aiml.Kernel()</br>
        k.learn("cn-startup1.xml")</br>
        k.respond("load aiml cn")</br>
        k.respond("start")</br>
        app = Flask(__name__)</br>
        app.config['SECRET_KEY'] = 'hard to guess string'
* 运行后learn内容保存在了aiml模块自定义函数中，一旦停止运行则无法继续访问而需要重新加载，每次进入会访问基本交互‘你叫什么名字’‘你喜欢的颜色？’等

* 尝试Threading，但初步无法实现每个threads之间的数据沟通，in vain</br>
### 最后解决 :clap: ：
* 删除cn-hallo.aiml中的基本交互内容，忍痛割爱，放弃逻辑交互，实现基本问答功能，所幸无损ask-answer模式
#存在新问题：
即使一句hallo也要重新加载数据库，花费时间长，效率低   
### -2022.8.19/17：20

## ！最最最最后解决[暴怒] :facepunch: ：
##### 把*加*载*放*到*的*主*程*序（_main_）*里*，但*是*为*什*么之前*出*现*了**问*题*？*？*？***&%￥#
        算了，我和程序有一个能跑就行	
### ##wxpython的GUI版本后继开发
# #先感谢墨染wx GUI界面支持
## -2022.8.19/19.40





		



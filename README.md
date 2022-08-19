# LIAM泮泣

LIAM带有简易学习功能，目前学习只能一句话对应一个回答，语料库在本地
小泮为青云开源机器人，需联网

测试前检查xuexi.aiml文件是否完整
开头是否有
'''
<?xml version="1.0" encoding="UTF-8"?>

<aiml version="1.0">

<!-- Free software (c) 2012 andelf -->
<!-- This program is open source code released under -->
<!-- the terms of the GNU General Public License -->
<!-- as published by the Free Software Foundation. -->

<meta name="author" content="Andelf"/>
<meta name="language" content="zh"/>
'''
如果无，需添加


每次在询问并回答完“你叫什么名字？”后可开始根据语料库交流
每次在询问并回答完“你喜欢什么颜色？”后可开始自由交互及学习
LIAM中输入exit退出

LDT.db文件为聊天记录，会自动创建



——2022.5.21 LIAM 
内容自检：

文件夹：
build
chinese #LIAM所有中文语料库
chinese-some #LIAM部分中文语料库
dist #应用程序备份
english #LIAM所有英文语料库

主文件：
ai.aiml #LIAM英文语料库其一
cn-startup.xml #LIAM完整语料库学习文件
cn-startup1.xml #LIAM部分语料库学习文件
liam[启动程序].exe
xuexi.aiml #LIAM学习中语料库


liamV1.4.2完整版本为娱乐版本，对其中部分功能（如时间，价格计算）请勿较真
	精简版[实用版本]开发中，敬请期待……
#墨染测试：
	发现human_text在首次input为空时报错，
#解决方法1：
	提前使之不为空，（暴力）‘+’
#解决方法二：
	检测语句，为空时提示重新输入

	#pyinstaller在win10x64环境下打包的.exe文件在win732位中无法运行
-2022.8.7




#LIAM机器人Tkinter版初步功能开发成功，期间困难与解决方案：
	1.tk界面创建，GUI布置困难： txt.pack()#绝对位置，但是只需要界面百分比，更方便
	2.txt模块自动滚动显示最新文本实现 txt.see("end")
	3.scrollBar = Scrollbar(root, command=txt.yview)
	  scrollBar.pack(side=RIGHT, fill=Y)
	  txt.configure(yscrollcommand = scrollBar.set)
	  #实现滚动条与txt区块同步
	4.清空entry框内容：inp1.delete(0, END)
	5.LIAM无法运行，经检查，原因如下：
			k = aiml.Kernel()
    			
    			k.learn("cn-startup1.xml")
    			k.respond("load aiml cn")
   			k.respond("start")
   			app = Flask(__name__)
   			app.config['SECRET_KEY'] = 'hard to guess string'
			运行后learn内容保存在了aiml模块自定义函数中，一旦停止运行则无法继续访问而需要重新加载，
					    每次进入会访问基本交互‘你叫什么名字’‘你喜欢的颜色？’等

			尝试Threading，但初步无法实现每个threads之间的数据沟通，in vain
	###最后解决：删除cn-hallo.aiml中的基本交互内容，忍痛割爱，放弃逻辑交互，实现基本问答功能，
								所幸无损ask-answer模式
				#存在新问题：
					即使一句hallo也要重新加载数据库，花费时间长，
								效率低2022.8.19 17：20

	######最最最最后解决[暴怒]：把*的*加*载*的*放*到*的*主*程*序（_main_）*里*，
				但*是*为*什*么*昨*晚*出*现*了**问**题？？？**&%￥#	
	wx版本后继开发
   	#先感谢墨染wx gui界面支持
                                                                -2022.8.19.19.40





		



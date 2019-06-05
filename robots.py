#机器人脚本代码V1.0
"""
三个功能：一、机器人自动向群中发送伤寒金匮条文。二、提供检索功能。以某一个特定的主题将相关的条文全部返回。三、将二功能中的信息全部保存到另外一张表中。
"""
#机器人脚本代码V2.0
"""
新增的功能：一、自动发送医案及答案。二、@经方机器人返回的不在是一条一条的条文，而是一个txt的文件。三、条文的自动发送功能还是有
"""
import time
import random
import pymysql
from wxpy import *
from multiprocessing import Process
class JFrobots_data():
    def return_text(self):
        self.db = pymysql.connect("localhost","xwj","sGFmqgocQ7OnGIHI","JingFang")
        self.ids = random.randint(1,100)
        self.sql = "select onetext from provision where id=%d"%self.ids
        self.cursor1 = self.db.cursor()
        print(self.sql)
        try:
            self.response = self.cursor1.execute(self.sql)
            print("开始查询")
            self.text = self.cursor1.fetchall()[0][0]
            #print("____")
            print(self.text)
            self.db.close()
            print("进程一的数据库关闭")
            return self.text
        except Exception:
            print("查询出错！")
            pass
def auto_tiaoweng(bot,my_group,robot1):
    while True:
        print("进程一ZZ")
        response = robot1.return_text()
        my_group.send_msg(response)
        time.sleep(30*60)
def connect_mysql(sql):
    db1 = pymysql.connect("localhost","xwj","sGFmqgocQ7OnGIHI","JingFang")
    print("连接成功")
    cursor1 = db1.cursor()
    print("创建执行对象")
    t = cursor1.execute(sql)
    print("执行查询语句")
    search_response = cursor1.fetchall()
    print(search_response)
    response_text = ""
    for i in range(len(search_response)):
        print(i)
        response_text = response_text + search_response[i][0]
        response_text = response_text + "\n"
    print("获取查询结果")
    print(response_text)
    print("函数连接")
    return response_text

if __name__ == "__main__":
    robot1 = JFrobots_data()
    bot = Bot()
    my_groups = bot.groups().search("经方机器人助手群")[0]
    t1 = Process(target=auto_tiaoweng,args=(bot,my_groups,robot1))
    t1.start()
    while True:
        #装饰器这里有问题，似乎函数没有到里面去执行
        print("_____")
        print("主进程")
        time.sleep(2)

        @bot.register(my_groups)
        def search_data(msg):
            print("函数内部")
            print(msg.is_at)
            if msg.is_at:
                print("******")
                text = msg.text
                print(type(text))
                text = text.split()
                #del text[0]
                print(text[1])
                text = "%" + text[1] + "%"
                print(text)
                sql = "select onetext from provision where onetext like '%s'"%text
                print(sql)
                print("连接数据库中")
                response = connect_mysql(sql)
                #print(search_response)
                list1_response = response.split("\n")
                for i in list1_response:
                    i = text + "\n" + i
                    print(i)
                    my_groups.send_msg(i)
                    time.sleep(random.randint(1,3))
                    
                db.close()
            else:
                pass

        




#将伤寒金匮原文写入数据库的脚本
#coding:utf-8
#import time
import re
import pymysql
def dealtext():
    print("-------")
    with open("新伤寒论.txt","r") as f:
        print("-------")
        text = f.read()
        print("____111")
        list1 = re.split(r"\d{1,3}",text)
        del list1[0]
        j = 1
        a = []
        for i in list1:
            i = str(j) + i
            a.append(i)
            print(i)
            j = j + 1
        return a
if __name__ == "__main__":
    text = dealtext()
    db = pymysql.connect("localhost","xwj","sGFmqgocQ7OnGIHI","JingFang")
    cursor = db.cursor()
    for i in text:
        sql = 'insert into provision(onetext) values("%s")'%i
        print(sql)
        print("\n")
        cursor.execute(sql)
    db.commit()
    #hhh,这是添加的
    db.close()

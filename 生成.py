kie = '''
软件作者：crazy  作者TG：@crazy7753 并不经常上线
软件支持四位补齐，三位补齐，二位补齐
模式——：四位补齐  模式二：三位补齐   模式三：二位补齐 模式四：六位补齐 模式五：男女分配
软件内置：身份证批量校验/身份证男女分配/结果输出
'''
print(kie)
# 身份证批量生成
print("补齐举例【四位：3305221994****2515/六位：******199412172515/二位：33052219941217**15/三位：***522199412172515】")
cet = input("选择模式【1/2/3/4/5/6】：")
base = input("请输入要生成的身份证")
# print(base[-1])
def found_1():
    for i in range(10000):
        dek = str(f'{i:04}')
        dek_1 = base.replace('****', dek)
        print(dek_1)
        with open('补齐.txt', 'a') as file0:
            print(dek_1, file=file0)
def found():
    for i in range(10000):
        dek = str(f'{i:04}')
        dek_1 = base.replace('****', dek)
        print(dek_1)
        with open('补齐.txt', 'a') as file0:
            print(dek_1, file=file0)
    for it in range(1000):
        dkk = str(f'{it:03}') + str('X')
        dkk_1 = base.replace('****', dkk)
        print(dkk_1)
        with open('补齐.txt', 'a') as file0:
            print(dkk_1, file=file0)

def find():
    for et in range(1000):
        dsk = str(f'{et:03}')
        but_1 = base.replace('***', dsk)
        print(but_1)
        with open('补齐.txt', 'a') as file0:
            print(but_1, file=file0)
    for cs in range(100):
        dik = str(f'{cs:02}') + str('X')
        dik_1 = base.replace('***', dik)
        print(dik_1)
        with open('补齐.txt', 'a') as file0:
            print(dik_1, file=file0)
def e():
    for i in range(1000000):
        dek = str(f'{i:06}')
        dek_1 = base.replace('******', dek)
        print(dek_1)
        with open('补齐.txt', 'a') as file0:
            print(dek_1, file=file0)
    for it in range(100000):
        dkk = str(f'{it:05}') + str("X")
        dkk_1 = base.replace('******', dkk)
        print(dkk_1)
        with open('补齐.txt', 'a') as file0:
            print(dkk_1, file=file0)
def e_1():
    for i in range(1000000):
        dek = str(f'{i:06}')
        dek_1 = base.replace('******', dek)
        print(dek_1)
        with open('补齐.txt', 'a') as file0:
            print(dek_1, file=file0)
def find_1():
    for et in range(1000):
        dsk = str(f'{et:03}')
        but_1 = base.replace('***', dsk)
        print(but_1)
        with open('补齐.txt', 'a') as file0:
            print(but_1, file=file0)
def lost():
    for ct in range(100):
        dbk = str(f'{ct:02}')
        ket_1 = base.replace('*', dbk)
        print(ket_1)
        with open('补齐.txt', 'a') as file0:
            print(ket_1, file=file0)
    for cs in range(10):
        dpk = str(f'{cs:01}') + str("X")
        dpk_1 = base.replace('**', dpk)
        print(base + dpk_1)
        with open("补齐.txt", "a") as file0:
            print(base + dpk_1, file=file0)
def lost_1():
    for ct in range(100):
        dbk = str(f'{ct:02}')
        ket_1 = base.replace('**', dbk)
        print(ket_1)
        with open('补齐.txt', 'a') as file0:
            print(ket_1, file=file0)
if cet == "1":
    if base[-1] == '*':
        print(found())
    else:
        print(found_1())
if cet == '2':
    if base[-1] == '*':
        print(find())
    else:
        print(find_1())
elif cet == "3":
    if base[-1] == '*':
        print(lost())
    else:
        print(lost_1())
elif cet == "4":
    print(e())
elif cet == "5":
    def s():
        txt = input("选择文件：")
        f = open(f"{txt}", "r")
        for line in f.readlines():  # 依次读取每行
            line = line.strip()
            hit = line
            n = int(hit[16])  # 取数据的倒数第二位并且转换 int类型
            if n % 2 == 0:  # 如果可以整除，是偶数，则为女性
                print('女' + hit)
                with open('女.txt', 'a') as file0:
                    print(hit, file=file0)
            else:  # 否则是男性
                print('男' + hit)
                with open('男.txt', 'a') as file0:
                    print(hit, file=file0)
input("回车开始校验身份证")
IDE = input('请输入姓名: ')
f = open("补齐.txt", "r", encoding='utf-8')
for line in f.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    ID = line[0:18]
    ID_add = ID[0:6]
    ID_birth = ID[6:14]
    ID_sex = ID[14:17]
    ID_check = ID[17]

    # ID_add是身份证中的区域代码，如果有一个行政区划代码字典，就可以用获取大致地址#
    year = ID_birth[0:4]
    moon = ID_birth[4:6]
    day = ID_birth[6:8]
    # 此部分应为错误判断，如果错误就不应有上面的输出，如何实现？#
    W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ID_num = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    ID_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    ID_aXw = 0

    for i in range(len(W)):
        ID_aXw = ID_aXw + int(ID[i]) * W[i]
    ID_Check = ID_aXw % 11
    if ID_check == ID_CHECK[ID_Check]:
        print('正确的身份证号码' + ID + IDE)
        with open('结果.txt', 'a') as file0:
            print(ID + IDE, file=file0)
    else:
        print('错误的身份证号码' + ID)
dlt = input("回车筛选结果")
lines = [l for l in open("结果.txt", "r") if l.find("错误的", 0, 8) != 0]
fd = open("结果.txt", "w")
fd.writelines(lines)
fd.close()
input("筛选完成")
kop = input("回车分配男女：")
f = open("结果.txt", "r")
for line in f.readlines():
    line = line.strip()
    hit = line
    n = int(hit[16])
    if n % 2 == 0:  # 正确女性
        print('女' + hit)
        with open('女.txt', 'a') as file0:
            print(hit, file=file0)
    else:  # 否则是男性
        print('男' + hit)
        with open('男.txt', 'a') as file0:
            print(hit, file=file0)
input("筛选完成")


[Program finished]
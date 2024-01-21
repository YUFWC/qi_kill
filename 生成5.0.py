
kie = '''
软件作者：@BFGzm11
软件内置：身份证批量校验/身份证男女分配/结果输出
'''
print(kie)
# 身份证批量生成
buqi=[]
boy = []
girl = []
print('补齐举例【四位：3305221994****2515/六位：******199412172515/二位：33052219941217**15/三位：***522199412172515】')
abcd = []
base = input('请输入要生成的身份证：')
base_1 = base.count('*')
a = '0'
b = '1'+a*base_1
e = '1'+a*(base_1-1)
c = int(b)
f = int(e)
g = base_1-1
d = '0'+str(base_1)
print(base_1)
if base[-1] != '*':
	for i in range(c):
	       dek = str(f'{i:0{base_1}}')
	       dek_1 = base.replace('*'*base_1, dek)
	       print(dek_1)
	       with open('补齐.txt', 'a') as file0:
           	print(dek_1, file=file0)
else:
	for ib in range(c):
        	dsk = str(f'{ib:0{base_1}}')
        	dsk_1 = base.replace('*'*base_1, dsk)
        	print(dsk_1)
        	with open('补齐.txt', 'a') as file0:
           	 print(dsk_1, file=file0)
        	   
	for it in range(f):
        	dkk = str(f'{it:0{g}}') + str('X')
        	dkk_1 = base.replace('*'*base_1, dkk)
        	print(dkk_1) 
        	with open('补齐.txt', 'a') as file0:
           	 print(dkk_1, file=file0)                        
input('回车开始校验身份证')
# IDE = input('请输入姓名: ')
f = open("补齐.txt", "r", encoding="utf-8")
for line in f.readlines(): 
    line = line.strip()  
    ID = line[0:18]
    ID_add = ID[0:6]
    ID_birth = ID[6:14]
    ID_sex = ID[14:17]
    ID_check = ID[17]

    year = ID_birth[0:4]
    moon = ID_birth[4:6]
    day = ID_birth[6:8]

    W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ID_num = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    ID_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    ID_aXw = 0

    for i in range(len(W)):
        ID_aXw = ID_aXw + int(ID[i]) * W[i]
    ID_Check = ID_aXw % 11
    if ID_check == ID_CHECK[ID_Check]:
        print('正确的身份证号码' + ID)
        with open('结果.txt', 'a') as file0:
           	print(ID, file=file0)   
    else:
        print('错误的身份证号码' + ID)
input('回车筛选结果')
lines = [l for l in open('结果.txt', 'r') if l.find('错误的', 0, 8) != 0]
fd = open('结果.txt', 'w')
fd.writelines(lines)
fd.close()
input('筛选完成回车分配男女')
f = open("结果.txt", "r", encoding="utf-8")
for line in f.readlines():
    line = line.strip()
    hit = line
    n = int(hit[16])
    if n % 2 == 0:  
        print('女' + hit)
        with open('girl.txt', 'a') as file0:
           	print(hit,  file=file0)   
    else:  
        print('男' + hit)
        with open('boy.txt', 'a') as file0:
           	print(hit, file=file0)   
input('筛选完成')	
txt = input("请选择文件: ")
print("正在读取文件...")
sourceFileData = open(txt,'r',encoding='utf-8')
ListOfLine = sourceFileData.read().splitlines()
n = len(ListOfLine)
print("文件共有" + str(n) + "行")
print("请输入需要将文件分割的个数:")
m = int(input(""))
p = n//m + 1
print("需要将文件分成 " + str(m) + " 个子文件")
print("每个文件最多有 " + str(p) + " 行")
print("开始进行分割···")
for i in range(m):
    print("正在生成第 " + str(i+1) + " 个子文件")
    destFileName = str(i) + ".txt"
    destFileData = open(destFileName,"w",encoding='utf-8')
    if(i == m-1):
        for line in ListOfLine[i*p:]:
        	destFileData.write(line + '\n')
    else:
        for line in ListOfLine[i*p:(i+1)*p]:
              	destFileData.write(line + '\n')
              	
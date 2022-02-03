import random
import requests
import time
import os
orr="\033[0;91m"
gr = "\033[0;92m"

line = "-------------------#Sliver~«@_559x»--------------------"
logo = f"""

[$]Free Bot From «@_559x» in Instagram

 .d8888b.  888      8888888 888     888 8888888888 8888888b.  
d88P  Y88b 888        888   888     888 888        888   Y88b 
Y88b.      888        888   888     888 888        888    888 
 "Y888b.   888        888   Y88b   d88P 8888888    888   d88P 
    "Y88b. 888        888    Y88b d88P  888        8888888P"  
      "888 888        888     Y88o88P   888        888 T88b   
Y88b  d88P 888        888      Y888P    888        888  T88b  
 "Y8888P"  88888888 8888888     Y8P     8888888888 888   T88b 
       
Ultra Report Bot By @_559x
"""

r = requests.Session()
print(logo)

print(line)
print ("""[1]Get Session Id
[2]Start Report""")
print(line)
print("     ")
repo = input("\n[+]Choose The mode : ")

def sid():
	try:
		user = input("[+]YOUR U$ERNAME  :>> ")
		password = input("[+]YOUR PA$$WORD :>> ")
		
		b = 'https://www.instagram.com/accounts/login/ajax/'
		
		w = {
		"accept":"*/*",
		"accept-encoding":"gzip, deflate,br",
		"accept-language": "ar,en-US;q=0.9,en;q=0.8",
		"content-length": "279",
		"content-type": "application/x-www-form-urlencoded",
		"origin": "https://www.instagram.com",
		"referer": "https://www.instagram.com/",
		"sec-fetch-dest":"empty",
		"sec-fetch-site":"same-origin",
		"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
		"x-ig-app-id": "936619743392459",
		"x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
		"x-instagram-ajax":"901e37113a69",
		"x-requested-with":"XMLHttpRequest"
		}
		
		k = {'username':user,
            'enc_password':
'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
        
		l = r.post(b,headers=w,data=k)
		sid = l.cookies['sessionid']
		with open('sid.txt','a') as si:
                    si.write(f'\n{sid}')
		print(sid)
	except:
		print("[+]Check Your Info ;)")

def spam():
	e = 0
	a = 0
	print(line)
	print("[1]Spam")
	print("[2]Self injury")
	print("[3]Sale of illegal or regulated goods")
	print("[4]Nudity or sexual activity")
	print("[5]Violence or dangerous organizations")
	print("[6]Hate speech or symbols")
	print("[7]Bullying or harassment")
	print("[8]preteding someone i know")
	print("[11]under the age of 13")
	print("[12]Sale Guns")
	print("[13]pretending me")
	print(line)
	mo = int(input("[+]Choose The Report : "))
	target = input("[+]THE TARGET : ")
	z = int(input("[+]The Sleep : "))
	much = int(input("[+]How Much The Bot Report? : "))
	
	idhe = {
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
	v = (f"https://instagram.com/{target}/?__a=1")
	vv = requests.get(v, headers=idhe)
	h = str(vv.json()["graphql"]["user"]["id"])
	
	headrepp = {
	"Host": "www.instagram.com",
	"content-length": "2995",
	"x-ig-www-claim": "hmac.AR0HB7TD0QsHzsME30oLkwz7qoNhBiL1ugPY_b2NyrrOQquz",
	"x-instagram-ajax": "843034f2a3dc",
	"content-type": "application/x-www-form-urlencoded",
	"accept": "*/*",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
	"x-requested-with": "XMLHttpRequest",
	"x-csrftoken": "a65nzn6vCPgegaJDjv6lIoekFiQUfKBN",
	"x-ig-app-id": "1217981644879628",
	"origin": "https://www.instagram.com",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": f"https://www.instagram.com/{h}/",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7"
	}
	
	for i in range(much):
		sidra = open('sid.txt','r').read().splitlines()
		sid = random.choice(sidra)
		cookies = {'sessionid': sid}
		urreport = "https://www.instagram.com/users/{}/report/".format(h)
		dat = {f'source_name':'','reason_id':{mo},'frx_context':''}
		repp = r.post(urreport,data=dat, headers= headrepp, cookies=cookies)
		if repp.status_code == 200:
			os.system("clear")
			a += 1
			print(f"{logo}\nThe Target : {target}\nThe Reports count : {much}\nThe Sleep : {z}\nDone Report [{a}] || Error Report [{e}]")
			time.sleep(z)

		else:
			os.system("clear")
			e += 1
			print(repp.text)

if repo == "1":
	sid()

elif repo == "2":
	spam()
	
else:
		print("Wrong Number !")
		exit(0)
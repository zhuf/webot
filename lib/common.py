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



# 根据appid和appsecret 创建API
# a = API('wx56cd36af256adcd0', 'c19b70c35825e1ebfad11c3ee428e')
# a = API('wx56cd36af256adcd0', 'c19b70c35825e1ebfad11c3ee428e5bb')
# class API:

#     def __init__(self, globalid, appid, appsecret, token='', expireTime=0):
#         self.groupid = globalid
#         self.appid = appid
#         self.appsecret = appsecret
#         self.prefix = 'https://api.weixin.qq.com/cgi-bin/'
#         self.mpPrefix = 'https://mp.weixin.qq.com/cgi-bin/'
#         self.fileServerPrefix = 'http://file.api.weixin.qq.com/cgi-bin/'

#         self.token = token
#         self.expireTime = expireTime

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
    #expireTime = int(time.time()) + data.get('expires_in', '') - 10

    r.set('access_token_' + globalid, token)
    return access_token
    #r.rpush(globalid, expireTime)


#def isAccessTokenValid(globalid):
#    token, expireTime = r.lrange(globalid, 0, -1)
#    return token and int(time.time()) < int(expireTime)

#'''
#    需要access_token的接口调用如果采用preRequest进行封装后，就可以直接调用
#    无需依赖getAccessToken为前置调用
#'''
#def preRequest(globalid, appid, appsecret):
#    if not isAccessTokenValid(globalid):
#        getAccessToken(globalid, appid, appsecret)

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






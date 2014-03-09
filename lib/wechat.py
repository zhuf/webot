# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import hashlib
import time
from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree as ET

# 检查签名
def checkSignature(query, token):
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr', '')

    arr = [token, timestamp, nonce].sort()
    s = ''.join(arr)

    return hashlib.sha1(s).hexdigest() == signature and echostr or False


# 将内容回复给微信的封装方法
# http://mp.weixin.qq.com/wiki/index.php?title=发送被动响应信息
def reply(msgType, content, fromUsername, toUsername):
    '''
        reply('text', '朱峰', 'zhu', 'feng')
        #reply('image', {'mediaId':'media_id'}, 'zhu', 'feng')
        #reply('voice', {'mediaId':'media_id'}, 'zhu', 'feng')
        #reply('video', {'mediaId':'media_id', 'title':'abc', 'description':'abc'}, 'zhu', 'feng')
        reply('music', {'title':'abc', 'description':'abc', 'musicUrl':'music_url','hqMusicUrl':'hq_music_url'},'zhu', 'feng')
        reply('news', [{'title':'abc1', 'description':'abc1','picUrl':'pic_url1','url':'url1'}, {'title':'abc2', 'description':'abc2','picUrl':'pic_url2','url':'url2'}], 'zhu', 'feng')
    '''

    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('tpl.txt')


    return template.render(toUser=toUsername, fromUser=fromUsername,
        createTime=str(int(time.time())), msgType=msgType, content=content).encode('utf-8')


# 从微信的提交中提取XML文件
# 返回为dict
def getMessage(stream):
    xml_recv = ET.fromstring(stream)
    message = {}
    for child in xml_recv:
        message[child.tag] = child.text

    return message


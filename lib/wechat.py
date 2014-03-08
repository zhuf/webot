# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import hashlib
import time
from jinja2 import Environment, FileSystemLoader

# 检查签名
def checksignature(query, token):
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr', '')

    arr = [token, timestamp, nonce].sort()
    s = ''.join(arr)

    return hashlib.sha1(s).hexdigest() == signature and echostr or False


# 将内容回复给微信的封装方法
# http://mp.weixin.qq.com/wiki/index.php?title=发送被动响应信息
def reply(msgtype, content, fromusername, tousername):
    '''
        reply('text', '朱峰', 'zhu', 'feng')
        #reply('image', {'mediaid':'media_id'}, 'zhu', 'feng')
        #reply('voice', {'mediaid':'media_id'}, 'zhu', 'feng')
        #reply('video', {'mediaid':'media_id', 'title':'abc', 'description':'abc'}, 'zhu', 'feng')
        reply('music', {'title':'abc', 'description':'abc', 'musicurl':'music_url','hqmusicurl':'hq_music_url'},'zhu', 'feng')
        reply('news', [{'title':'abc1', 'description':'abc1','picurl':'pic_url1','url':'url1'}, {'title':'abc2', 'description':'abc2','picurl':'pic_url2','url':'url2'}], 'zhu', 'feng')
    '''

    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('tpl.txt')


    return template.render(touser=tousername, fromuser=fromusername,
        createtime=str(int(time.time())), msgtype=msgtype, content=content).encode('utf-8')



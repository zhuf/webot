# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json

class Menu:
    '''
    {
        "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"V1001_TODAY_MUSIC"
        },
        {
            "name":"菜单",
            "sub_button":[
            {
                "type":"view",
                "name":"搜索",
                "url":"http://www.soso.com/"
            },
            {
                "type":"view",
                "name":"视频",
                "url":"http://v.qq.com/"
            }]
        }]
    }

    m.addButton({"type":"click","name":"今日歌曲","key":"V1001_TODAY_MUSIC"})
    m.addButton({"name":"菜单"},
            [{"type":"view","name":"搜索","url":"http://www.soso.com/"},
            {"type":"view","name":"视频","url":"http://v.qq.com/"}])

    '''
    buttons = []

    def addButton(self, button, subbuttons=[]):
        if subbuttons != []:
            button['sub_button'] = subbuttons
        self.buttons.append(button)

        return self.buttons

    def toString(self):
        return json.dumps({'button': self.buttons})




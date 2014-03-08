# -*- coding: utf-8 -*-

import json

# 对返回结果的一层封装, 如果遇见微信返回的错误, 将返回一个错误
# http://mp.weixin.qq.com/wiki/index.php?title=返回码说明
def wrapper(err, data, res):
    pass


# 对提交参数一层封装, 当POST JSON, 并且结果也为JSON时使用
def postJSON(data):
    return json.dumps({
        'dataType': 'json',
        'type': 'POST',
        'data': data,
        'headers': {'Content-Type': 'application/json'}
        })
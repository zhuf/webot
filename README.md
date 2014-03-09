webot
=====

the python version of [node-webot](https://github.com/node-webot/wechat)



### TODO
- *util.py*
	* json encode, postjson 暂时未用
- *common.py*
	* api中token的缓存问题(redis?)
- *session*
- *mediaid*
	* 是否需要将media存储([七牛](http://developer.qiniu.com/docs/v6/sdk/python-sdk.html))

### changelog
- 2013-03-09:
	* 完成checkSignature, reply, getMessage, 基本api
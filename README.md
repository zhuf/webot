webot
=====

the python version of [node-webot](https://github.com/node-webot/wechat)



### TODO

- *common.py*
	* api中token的缓存问题(redis?)
	* 用redis缓存, 定期同步, 发起post请求时, 从redis中读取相应的token, 然后发起请求, 如果发现过时, 则重新获取token, 并且更新到redis中.
- *session*
- *mediaid*
	* 是否需要将media存储([七牛](http://developer.qiniu.com/docs/v6/sdk/python-sdk.html))
- *util.py*
	* json encode, postjson 暂时未用

### changelog
- 2013-03-09:
	* 完成checkSignature, reply, getMessage, 基本api
# -*- coding: utf-8 -*-



import sys
sys.path.append('../lib')

from common import *


# access_token = getAccessToken('gh_56f50354626a', 'wx56cd36af256adcd0', 'c19b70c35825e1ebfad11c3ee428e5bb')
# print access_token

access_token = 'yknAIYfPASWlXT4kPOqRuK6sN5KUGorz7TUqx9YRZX_KSS9HjGnhKSyH3FELBV9Yaq7MRwqzd13NFzLb0qzFaclWXG3HTGAMym9Cv-TG03LKt5HBynVpfvTMDuDd5WG8cuvEAfTCqzFq41kKJOleqA'


# print removeMenu(access_token)

# print getMenu(access_token)


# menu = {"button":[{"type":"view","name":"2048","url":"http://gabrielecirulli.github.io/2048/"},{"type":"click","name":"歌手简介","key":"V1001_TODAY_SINGER"},{"name":"菜单","sub_button":[{"type":"view","name":"搜索","url":"http://www.soso.com/"},{"type":"view","name":"视频","url":"http://v.qq.com/"},{"type":"click","name":"赞一下我们","key":"V1001_GOOD"}]}]}

# print createMenu(access_token, menu)

# print getGroups(access_token)

# group = {"group": {"id": 100, "name": "朱峰1"}}
# print updateGroup(access_token, group)
# print getGroups(access_token)

# print moveUserToGroup(access_token, 'oYhyAuDWv-1cDCJtXyWfyiaq9ZaE', 101)
# print getGroups(access_token)

# print getUserGroup(access_token, 'oYhyAuDWv-1cDCJtXyWfyiaq9ZaE')
# print getUserInfo(access_token, 'oYhyAuDWv-1cDCJtXyWfyiaq9ZaE')
# print getFollowers(access_token)

# musicurl = 'http://zhufwechat.qiniudn.com/%E8%8C%83%E7%8E%AE%E7%90%AA-%E6%82%84%E6%82%84%E5%91%8A%E8%AF%89%E4%BD%A0.mp3'
# thumb_media_id = 'DvXVfEHboOVIz0MjRJeuyDdJInH9KDlx2JRG-25VKWxeMY3EsQIWru2-Ak0WRceH'

# print sendText(access_token, 'oYhyAuDWv-1cDCJtXyWfyiaq9ZaE', '朱峰')
# print sendImage(access_token, 'oYhyAuDWv-1cDCJtXyWfyiaq9ZaE', 'PWNOq_CwRnABC72SiHrTUGVAdKeU3jLUk78x_k1lxUmxyo3OMp6szA0bzgrpF6IG')

# print sendMusic(access_token, 'oYhyAuNJgfK8k-TREF3IhIGZXBCQ', musicurl, thumb_media_id, title='悄悄告诉你', description='范玮琪')
# print getMedia(access_token, thumb_media_id)

# print createTmpQRCode(access_token, 111)
# print createLimitQRCode(access_token, 1)
# print showQRCodeURL('gQGB8DoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL3lFT0hkNGZtalFmMDNCMldzR19tAAIEfIggUwMEAAAAAA==')
print getQRCode(access_token)



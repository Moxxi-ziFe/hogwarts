import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww65f497c6496830ff'
        corpsecret = 'DxeJyj6EoNa22SWUJEipe_FYUu2z01gTPraxCot5Q6c'
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        # print(json.dumps(r.json(), indent=2))
        return r

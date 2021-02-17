import requests


class Tag:

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww65f497c6496830ff'
        corpsecret = 'DxeJyj6EoNa22SWUJEipe_FYUu2z01gTPraxCot5Q6c'

        r = requests.get(
            'https://qyapi.weixin.qq.com'
            '/cgi-bin'
            '/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com'
            '/cgi-bin'
            '/externalcontact'
            '/get_corp_tag_list',
            params={'access_token': self.token},
            json={
                'tag_id': [],
            }
        )
        return r

    def update(self, tag_id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com'
            '/cgi-bin/externalcontact'
            '/edit_corp_tag',
            params={'access_token': self.token},
            json={
                'id': tag_id,
                'name': tag_name
            }
        )
        return r

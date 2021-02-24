import json

import requests

from api.WecomAPI.tag_PO.base_api import BaseApi


class Tag(BaseApi):

    # def get_token(self):
    #     corpid = 'ww65f497c6496830ff'
    #     corpsecret = 'DxeJyj6EoNa22SWUJEipe_FYUu2z01gTPraxCot5Q6c'
    #
    #     r = requests.get(
    #         'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
    #         params={'corpid': corpid, 'corpsecret': corpsecret}
    #     )
    #     assert r.status_code == 200
    #     assert r.json()['errcode'] == 0
    #     token = r.json()['access_token']
    #     return token

    def list(self):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'params': {'access_token': self.token},
            'json': {'tag_id': []}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        #     params={'access_token': self.token},
        #     json={'tag_id': []}
        # )
        # print(json.dumps(r.json(), indent=2))
        return r

    def add(self, group_name, tag):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'params': {'access_token': self.token},
            'json': {"group_name": group_name, "tag": tag}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #     params={'access_token': self.token},
        #     json={"group_name": group_name, "tag": tag}
        # )
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, tag_id, tag_name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'params': {'access_token': self.token},
            'json': {'id': tag_id, 'name': tag_name}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        #     params={'access_token': self.token},
        #     json={'id': tag_id, 'name': tag_name}
        # )
        return r

    def delete_group(self, group_id):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token},
            'json': {"group_id": [group_id]}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #     params={'access_token': self.token},
        #     json={"group_id": group_id}
        # )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_tag(self, tag_id):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {'access_token': self.token},
            'json': {"tag_id": [tag_id]}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
        #     params={'access_token': self.token},
        #     json={"tag_id": tag_id}
        # )
        print(json.dumps(r.json(), indent=2))
        return r

    def find_group(self, group_name):
        r = self.list()
        res = [group for group in r.json()['tag_group'] if group['group_name'] == group_name]
        return res

    def find_tag(self, tag_name, group_name=None):
        res = []
        if group_name:
            group = self.find_group(group_name)
            if group:
                return [tag for tag in group[0]['tag'] if tag['name'] == tag_name]
        else:
            groups = [group for group in self.list().json()['tag_group']]
            for group in groups:
                for tag in group['tag']:
                    if tag['name'] == tag_name:
                        res.append(tag)
        return res

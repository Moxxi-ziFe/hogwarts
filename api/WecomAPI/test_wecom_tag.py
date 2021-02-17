import datetime
import json

import requests


def test_tag_list():
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

    # r = requests.post(
    #     'https://qyapi.weixin.qq.com'
    #     '/cgi-bin'
    #     '/externalcontact'
    #     '/get_corp_tag_list',
    #     params={'access_token': token},
    #     json={
    #         'tag_id': [],
    #     }
    # )
    # print(json.dumps(r.json(), indent=2))
    # assert r.status_code == 200
    # assert r.json()['errcode'] == 0

    tag_name = 'tag_' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
    r = requests.post(
        'https://qyapi.weixin.qq.com'
        '/cgi-bin/externalcontact'
        '/edit_corp_tag',
        params={'access_token': token},
        json={
            'id': 'etO62TCwAAD48h8wbeaJcczjA9ZVqWpg',
            'name': tag_name
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com'
        '/cgi-bin'
        '/externalcontact'
        '/get_corp_tag_list',
        params={'access_token': token},
        json={
            'tag_id': [],
        }
    )
    # print(r.json())
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'python15'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    assert tags != []
    print(tags)

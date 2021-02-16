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
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

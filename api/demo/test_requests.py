import requests
from requests.auth import HTTPBasicAuth
from jsonpath import jsonpath


class TestDemo:
    def test_demo(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())

    def test_query(self):
        payload = {
            'level': 1,
            'name': 'Moxxi'
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'level': 1,
            'name': 'Moxxi'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.status_code)
        print(r.request.body)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={'hello': 'world'})
        print(r.request.headers)
        print(r.text)
        print(r.json())
        assert r.json()['headers']['Hello'] == 'world'

    def test_post_json(self):
        payload = {
            'level': 1,
            'name': 'Moxxi'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.status_code)
        print(r.request.body)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'

    def test_cookies(self):
        # 方法一: 使用header
        header = {
            'User-Agent': 'student'
        }
        # r = requests.get('https://httpbin.testing-studio.com/cookies', headers=header)
        # print(r.request.headers)

        # 方法二: 使用关键字
        cookie = {
            'User': 'Moxxi',
            'Age': '24'
        }
        r = requests.get('https://httpbin.testing-studio.com/cookies', headers=header, cookies=cookie)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get(
            url='https://httpbin.testing-studio.com/basic-auth/Moxxi/123',
            auth=HTTPBasicAuth('Moxxi', '123')
        )
        print(r.json())

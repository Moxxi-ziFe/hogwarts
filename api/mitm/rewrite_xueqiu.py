import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:  # 加上过滤条件
        data = json.loads(flow.response.content)  # 把响应数据转化成python对象，保存到data中
        data['data']['items'][0]['quote']['name'] = 'ziFe'  # 修改第一只股票的名称
        data['data']['items'][1]['quote']['name'] = 'Moxxi'  # 修改第二只股票的名称
        data['data']['items'][1]['quote']['current'] = 100  # 修改第二只股票的价格
        data['data']['items'][1]['quote']['percent'] = 100  # 修改第二只股票的涨幅
        flow.response.text = json.dumps(data)  # 把修改后的内容赋值给response, 原始数据格式

# -*- coding: utf-8 -*-
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开本地保存的数据文件
        with open(r"/tmp/stock.json", encoding='utf-8') as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content, 读取文件中的数据作为返回内容
                {"Content-Type": "application/json"}  # (optional) headers, 指定返回数据的类型
            )

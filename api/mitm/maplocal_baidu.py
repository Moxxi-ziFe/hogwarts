from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 发起请求，判断url是不是预期的url
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个response
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"content-Type": "text/html"}  # (optional) headers
        )

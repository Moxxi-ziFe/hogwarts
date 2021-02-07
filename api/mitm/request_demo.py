from mitmproxy import http


# request 方法名不能修改
def request(flow: http.HTTPFlow):
    # 增加请求的头部信息中的字段
    flow.request.headers["myHeader"] = "Moxxi"
    print(flow.request.headers)

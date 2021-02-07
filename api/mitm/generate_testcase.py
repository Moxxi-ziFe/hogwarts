import json

from mitmproxy import http

# 修改规则模型
rule = [-5, -3, -1, 0, 1, 3, 5, 100]

# 统计url
url_index = dict()


# def response(flow: http.HTTPFlow):
#     if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:  # 加上过滤条件
#         data = json.loads(flow.response.content)  # 把响应数据转化成python对象，保存到data中
#         data_new = data_process(data, num=10)  # 对数据进行批量修改
#         flow.response.text = json.dumps(data_new)  # 把修改后的内容赋值给response, 原始数据格式

def response(flow: http.HTTPFlow):
    # url = flow.request.url.split('.json')[0]
    # if url not in url_index.keys():
    #     url_index[url] = 0
    # else:
    #     url_index[url] += 1
    # seed = url_index[url] % len(rule)
    # 拿到请求 url
    url = flow.request.url.split('.json')[0]

    # 如果 url 不在 url_index 字典的key中
    if url not in url_index.keys():
        # 把对应的key值赋值为0
        url_index[url] = 0
    else:
        url_index[url] += 1

    seed = url_index[url] % len(rule)
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:  # 加上过滤条件
        data = json.loads(flow.response.content)  # 把响应数据转化成python对象，保存到data中
        data_new = data_process(data, num=0)  # 对数据进行批量修改
        flow.response.text = json.dumps(data_new, ensure_ascii=False)  # 把修改后的内容赋值给response, 原始数据格式


def data_process(data, array=1, string=1, num=1):
    """
    完成json数据的加倍操作
    :param data: 数据
    :param array: 列表修改倍数，默认不加倍
    :param string: 字符串修改倍数，默认不加倍
    :param num: 数字修改倍数，默认不加倍
    :return:
    """
    if isinstance(data, dict):
        data_new = {}
        for key, value in data.items():
            data_new[key] = data_process(value, array, string, num)
        return data_new
    if isinstance(data, list):
        data_new = []
        for item in data:
            item_new = data_process(item, array, string, num)
            for i in range(array):
                data_new.append(item_new)
        return data_new
    if isinstance(data, str):
        return data * string
    if isinstance(data, (int, float)):
        return data * num
    return data

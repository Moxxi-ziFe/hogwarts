import json

from api.mitm.generate_testcase import data_process

data = {
    "teacher": {
        "name": "Moxxi",
        "age": 18
    },
    "student": {
        "name": ['a', 'b'],
        "age": 3
    }
}


def test_data():
    print(json.dumps(data_process(data, num=5), ensure_ascii=False, indent=2))

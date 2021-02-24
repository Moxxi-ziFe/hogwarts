import datetime
import json

import pytest

from api.WecomAPI.tag_PO.Wecom_tag_PO import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    @pytest.mark.parametrize(
        "tag_id, group_name, tag_name",
        [
            ['etO62TCwAAD48h8wbeaJcczjA9ZVqWpg', 'python15', 'tag_'],
            ['etO62TCwAAD48h8wbeaJcczjA9ZVqWpg', 'python15', 'tag_中文']
        ]
    )
    def test_update_tag(self, tag_id, group_name, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        self.tag.update(tag_id=tag_id, tag_name=tag_name)
        tags = self.tag.find_tag(tag_name=tag_name)
        assert tags != []

    def test_list(self):
        self.tag.list()

    # 40071, UserTag Name Already Exist
    # 1. 删除对应tag(推荐)
    # 2. 已有的tag基础上追加时间戳或计数器
    @pytest.mark.parametrize(
        'group_name, tag',
        [
            ["TMP_1", [{"name": "TAG_1"}, {"name": "TAG_2"}, {"name": "TAG_3"}]]
        ]
    )
    def test_add_tag(self, group_name, tag):
        self.tag.add(group_name=group_name, tag=tag)

    # 40068, invalid tagId
    # 1. 删除接口有问题
    # 2. 再进行重试 (重试次数: n): 手动实现, 或借助pytest 钩子(rerun插件)
    #  a. 添加一个tag
    #  b. 对新添加的tag再删除
    #  c. 查询删除是否成功
    def test_delete_group(self):
        group_id = "etO62TCwAAS_ujrxfnTb-_FL4L4I_dKQ"
        self.tag.delete_group(group_id=group_id)

    def test_delete_tag(self):
        tag_id = 'etO62TCwAAckTSrcATz7ToTkF1-469_Q'
        self.tag.delete_tag(tag_id=tag_id)

    @pytest.mark.parametrize(
        'group_name',
        [
            'TMP_1'
        ]
    )
    def test_delete_group_by_name(self, group_name):
        groups = self.tag.find_group(group_name=group_name)
        for group in groups:
            group_id = group['group_id']
            self.tag.delete_group(group_id=group_id)
        assert self.tag.find_group(group_name) == []

    def test_delete_tag_by_name(self):
        tags = self.tag.find_tag(tag_name='TAG_1')
        for tag in tags:
            tag_id = tag['id']
            self.tag.delete_tag(tag_id=tag_id)
        assert self.tag.find_tag(tag_name='TAG_1') == []

    def test_find_group(self):
        group = self.tag.find_group('TMP_1')
        print(json.dumps(group, indent=2))

    def test_find_tag(self):
        tag = self.tag.find_tag(tag_name='TAG_1')
        print(json.dumps(tag, indent=2))

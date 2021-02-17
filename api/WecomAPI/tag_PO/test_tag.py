import datetime

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
    def test_tag_list(self, tag_id, group_name, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        tag = self.tag
        tag.list()
        tag.update(
            tag_id=tag_id,
            tag_name=tag_name
        )
        r = tag.list()
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == group_name
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        assert tags != []

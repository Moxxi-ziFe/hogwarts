import pytest
import yaml


def get_data(file_name):
    with open(file_name) as f:
        test_data = yaml.safe_load(f)
        return test_data


class TestRotate:
    # def setup(self):
    #     self.solution = Solution()

    @pytest.mark.parametrize("nums, expect", get_data("../Datas/rotate_list.yml"))
    def test_solution(self, get_function, nums, expect):
        print(f'rotate_list_search{nums} = {expect}')
        assert get_function.rotate_list_search_minimum(nums) == expect

    def test_solution2(self, get_function):
        nums = [3, 4, 5, 6, 7, 8, 9, 1, 2]
        for i in range(1, 10):
            print(f'{nums, i}, {get_function.rotate_list_search_target(nums, i)}, {nums.index(i)}')
            assert get_function.rotate_list_search_target(nums, i) == nums.index(i)
        assert get_function.rotate_list_search_target(nums, 0) == -1

from typing import List


def answer_five(nums: List[object]):
    # iterate through list and fill None elements with previous elements in incremental way
    for ix in range(1, len(nums)):
        if nums[ix] is None:
            nums[ix] = nums[ix - 1]

    return nums


print(answer_five([3, None, 2, None, None, 1, False, None, 10]))

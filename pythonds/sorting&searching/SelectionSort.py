"""
Simple Selection Sort implementation
"""


def selection_sort(nums: list) -> list:
    # In-place algorithim
    l = len(nums)
    for i in range(l - 1):
        min_index = i
        for j in range(i + 1, l, 1):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


if __name__ == "__main__":
    print(selection_sort([10, 2, 4, 2, 5, 3]))

"""
Simple Bubble Sort Implementation
"""


def bubble_sort(nums: list) -> list:
    # return the sorted list and In-place algorithim
    l = len(nums)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == "__main__":
    print(bubble_sort([20, 30, 40, 90, 50, 60, 70, 80, 100, 110]))

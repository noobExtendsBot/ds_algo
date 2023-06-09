import pdb

def removeDuplicates(nums):
    if len(nums) == 0: return
    prev = 0
    nxt = prev + 1
    # pdb.set_trace()
    while prev < nxt and nxt < (len(nums)):
        if nums[nxt] == nums[prev]:
            nums[prev] = None
        prev += 1
        nxt += 1
    return nums

if __name__=="__main__":
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
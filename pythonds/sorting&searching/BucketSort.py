"""
Bucket Sort: The idea is to divide the elements into k buckets (k=10)
Then for each elements BucketIndex = int(k*j), where j in the j-th element in nums  
Now we have elements in the Buckets, now sort the each Bucket using insertion sort
And concat them

A more generalized version of this would be:
range = (max - min) / k
BucketIndex = ( arr[i] - min) / range
Time Complexity: O(n+k) n = number of elements and k = number of buckets
"""


def insertion_sort(arr):
    
    for i,_ in enumerate(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]

def bucket_sort(nums):
    slot_num = 10
    res = []
    # divide the arr into buckets
    bucket = [[] for x in range(slot_num)]

    # divide the numbers into buckets
    for j in nums:
        slot = int(slot_num*j)
        bucket[slot].append(j)
    
    print(bucket)
    # now sort each bucket
    for i in bucket:
        insertion_sort(i)
    
    # now concat the bucket into single array
    # keep a result array and keep adding elements in the order 
    # they appear in the Bucket
    for i in bucket:
        for j in i:
            res.append(j)
    
    return res


    

if __name__=="__main__":
    nums = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
    print(bucket_sort(nums))
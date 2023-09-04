class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        arr= sorted(nums1+nums2)
        if len(arr)%2==0:
            x= len(arr)/2
            k = float(arr[x-1]+arr[x])/2.0            
            return k
        else:
            y =len(arr)//2
            y = int(y)
            return arr[y]

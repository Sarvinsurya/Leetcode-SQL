class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        while (i<len(nums1)):
            nums3.append(nums1[i])
            i+=1
        while (j<len(nums2)):
            nums3.append(nums2[j])
            j+=1
        n=len(nums3)
  
        if n % 2 == 0: 
            return (float)(nums3[n // 2] + nums3[(n // 2) - 1]) / 2  
        else:  
            return nums3[n // 2]  

        
        # n1=len(nums1)
        # n2=len(nums2)
        # if (n1>n2):
        #     return findMedianSortedArrays(n2,n1)
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1=len(nums1)
        n2=len(nums2)
        if (n1>n2):
            return self.findMedianSortedArrays(nums2,nums1)
        low=0
        high=n1
        left=(n1+n2+1)/2
        n=n1+n2
        while(low<=high):
            mid1=(low+high)/2
            mid2= left - mid1
            l1,l2=float('-inf'),float('-inf')
            r1,r2=float('inf'),float('inf')
            if(mid1<n1):
                r1=nums1[mid1]
            if(mid2<n2):
                r2=nums2[mid2]
            if(mid1-1>=0) :
                l1=nums1[mid1-1]
            if(mid2-1>=0):
                l2=nums2[mid2-1]
            if(l1<=r2 and l2<=r1):
                if(n%2==1):
                    return max(l1,l2)
                return ((max(l1,l2)+min(r1,r2))/2.0)
            elif (l1>r2):
                high=mid1-1
            else:
                low=mid1+1


        # nums3=[] #in this approach i merged 2 arrays in sorting order then i found the median of sorted arrays 
        # i=0
        # j=0
        # n=len(nums1)+len(nums2)
        # limit=(n//2)+1
        # while(i<len(nums1) and j<len(nums2) and len(nums3)<limit):
        #     if nums1[i]<nums2[j]:
        #         nums3.append(nums1[i])
        #         i+=1
        #     else:
        #         nums3.append(nums2[j])
        #         j+=1
        # while (i<len(nums1) and len(nums3)<limit):
        #     nums3.append(nums1[i])
        #     i+=1
        # while (j<len(nums2) and len(nums3)<limit):
        #     nums3.append(nums2[j])
        #     j+=1
        # n=len(nums2)+len(nums1)

        # if n % 2 == 0: 
        #     return (nums3[-1] + nums3[-2]) / 2.0
        # else:  
        #     return float(nums3[-1])  
        # nums3=[]
        # i=0
        # j=0
        # while(i<len(nums1) and j<len(nums2)):
        #     if nums1[i]<nums2[j]:
        #         nums3.append(nums1[i])
        #         i+=1
        #     else:
        #         nums3.append(nums2[j])
        #         j+=1
        # while (i<len(nums1)):
        #     nums3.append(nums1[i])
        #     i+=1
        # while (j<len(nums2)):
        #     nums3.append(nums2[j])
        #     j+=1
        # n=len(nums3)
  
        # if n % 2 == 0: 
        #     return (float)(nums3[n // 2] + nums3[(n // 2) - 1]) / 2  
        # else:  
        #     return nums3[n // 2]  

        
        # n1=len(nums1)
        # n2=len(nums2)
        # if (n1>n2):
        #     return findMedianSortedArrays(n2,n1)
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
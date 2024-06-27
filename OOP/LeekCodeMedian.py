class Solution(object):
    def findMedianSortedArrays(nums1, nums2): #define a function that finds the media of the two sorted arrays
        if len(nums1) > len(nums2): #if length of array 1 > length of array 2
            nums1, nums2 = nums2, nums1 #ensure that nums1 is the smaller aray
    
        m, n = len(nums1), len(nums2) #m is the length of nums1, n is the length of nums2
        imin, imax, half_len = 0, m, (m + n + 1) // 2 #initialize imin to 0, imax to m, 
        #and ensures we can split the combined arrays into two halves.
    
        while imin <= imax: #while imin is less than or equal to imax
                            #i is the average of imin and imax
            
            i = (imin + imax) // 2 ##incices used to partition tthe two input arrays
            j = half_len - i  
        
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
            
                if (m + n) % 2 == 1:
                    return max_of_left
            
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
            
                return (max_of_left + min_of_right) / 2.0


nums1 = [1, 3, 90, 20, 40, 50, 60, 70, 80, 100]
nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(Solution.findMedianSortedArrays(nums1, nums2))
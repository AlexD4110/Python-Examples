class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Lengths of the two arrays
        m, n = len(nums1), len(nums2)
        
        # Initialize binary search bounds for the smaller array
        imin, imax, half_length = 0, m, (m + n + 1) // 2
        
        # Perform binary search
        while imin <= imax:
            # Partition nums1 at index i
            i = (imin + imax) // 2
            
            # Partition nums2 at index j so that the left and right partitions have equal length
            j = half_length - i
            
            # Adjust imin if nums1's current element is smaller than nums2's previous element
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            # Adjust imax if nums1's previous element is greater than nums2's current element
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # We have found the correct partition
                # Determine max of the left partition
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                
                # If the total number of elements is odd, the median is max_of_left
                if (m + n) % 2 == 1:
                    return max_of_left #return 8
                
                                                #in CASS of nums1 = [1, 3, 8] and nums2 = [7, 9, 10, 11]
                
                # Determine min of the right partition
                if i == m:                      #i = 3, m = 3
                    min_of_right = nums2[j]     #j = 1 => nums2[1] = 9
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                
                # If the total number of elements is even, the median is the average of max_of_left and min_of_right
                return (max_of_left + min_of_right) / 2.0 #

# Example arrays
nums1 = [1, 3, 8]
nums2 = [7, 9, 10, 11]



# Create an instance of Solution
solution_instance = Solution()

# Print the median of the two sorted arrays
print(solution_instance.findMedianSortedArrays(nums1, nums2))

if ( 7 % 2 == 1):
    print("7 is odd")
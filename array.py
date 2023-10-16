def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        max_of_left = float('-inf') if i == 0 else nums1[i - 1]
        min_of_right = float('inf') if i == m else nums1[i]

        max_of_left2 = float('-inf') if j == 0 else nums2[j - 1]
        min_of_right2 = float('inf') if j == n else nums2[j]

        if max_of_left <= min_of_right2 and max_of_left2 <= min_of_right:
            if (m + n) % 2 == 0:
                return (max(max_of_left, max_of_left2) + min(min_of_right, min_of_right2)) / 2.
            else:
                return max(max_of_left, max_of_left2)
        elif max_of_left > min_of_right2:
            right = i - 1
        else:
            left = i + 1

    # If no solution is found, return None or raise an exception as desired.
    return None

# Example usage:
nums1 = [1, 3]
nums2 = [2]
median = findMedianSortedArrays(nums1, nums2)
print(median)  # Output: 2.0

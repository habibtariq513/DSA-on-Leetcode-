class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        i = j = 0
        res = []

        while len(nums1) > i and len(nums2) > j:
            id1, v1 = nums1[i]
            id2, v2 = nums2[j]

            if id1 == id2:
                res.append([id1, v1 + v2])
                i += 1
                j += 1
            
            elif id1 < id2:
                res.append([id1, v1])
                i += 1

            else:
                res.append([id2, v2])
                j += 1
        
        res.extend(nums1[i:])
        res.extend(nums2[j:]) 
        return res

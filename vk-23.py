from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    return [i for i, (x, y) in enumerate(zip(nums1, nums2)) if x < y]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
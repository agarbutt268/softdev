def big_diff(nums):
  small = nums[0]
  big = nums[0]
  for i in range(len(nums)):
    small = min(nums[i], small)
    big = max(nums[i], big)
  
  return big - small

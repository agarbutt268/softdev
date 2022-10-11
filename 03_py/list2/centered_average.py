def centered_average(nums):
  small = nums[0]
  big = nums[0]
  for i in range(len(nums)):
    small = min(nums[i], small)
    big = max(nums[i], big)
  
  nums.remove(small)
  nums.remove(big)
  
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
    
  return sum // len(nums)

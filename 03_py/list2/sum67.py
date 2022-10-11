def sum67(nums):
  sum = 0
  seen6 = False
  for i in range(len(nums)):
    if (nums[i] == 6):
      seen6 = True
    if (not seen6):
      sum += nums[i]
    if (seen6 and nums[i] == 7):
      seen6 = False
  
  return sum

def array123(nums):
  next = 1
  for i in range(len(nums)):
    if (nums[i] != next):
      next = 1

    if (nums[i] == next):
      next += 1
      if (next == 4):
        return True

  return False

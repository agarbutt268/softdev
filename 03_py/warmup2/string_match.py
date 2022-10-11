def string_match(a, b):
  length =  min(len(a), len(b))
  match = 0
  for i in range(length-1):
    if (a[i:i+2] == b[i:i+2]):
      match += 1
  
  return match

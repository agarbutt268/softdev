def last2(str):
  l=0
  for i in range(len(str)-1):
    if(str[i:i+2] == str[-2:]):
      l+=1

  if (l > 0):
    return l-1
  return l

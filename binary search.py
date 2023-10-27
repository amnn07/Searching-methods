def bin(lst,item):
   left=0
   right=len(lst)-1
   while left<=right:
      mid=(left+right)//2
      if lst[mid]==item:
         return mid
      if item<lst[mid]:
         right=mid-1
      else:
         left=mid+1
   else:
      return False
print(bin([-8,-7,-5,-3,-3,-1,1],-5))

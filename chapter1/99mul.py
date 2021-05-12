# for i in range(1,10):
#   for j in range(1,i+1):
#     print(j,"*",i,"=",j*i,"\t",end=" ")
#   print("")


list=[0,1]
for i in range(0,10):
  c=list[i]+list[i+1]
  list.append(c)
print(list)
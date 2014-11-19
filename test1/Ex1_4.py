import sys
def dict(x):
   dict1={}
   for i in x:
       if i in dict1.keys():
           dict1[i]+=1




       else:
            dict1[i]=1
   test =sorted(dict1.items())
   b=test[0]
   n=len(test)
   m=test[n-1]
   return(b,m)
if __name__ == '__main__':
  x="A for loop on a dictionary iterates over its keys by default"
  print dict(x)





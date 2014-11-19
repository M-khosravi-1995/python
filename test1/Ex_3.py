import sys
import math

def avg(input_list):
    sum=0
    for i in input_list:
        sum+=i
    n=len(input_list)
    avg1=sum/n
#######################
    if n%2==1:
        md= input_list[n/2]
    else:
       mid=n/2
       k= (input_list[mid]+input_list[mid-1])
       md= float(k)/2.0
#######################
    sum=0
    for i in input_list:
        sum+=(i-avg1)^2
    a=sum/n
    decimal=math.sqrt(a^2)
    return avg1,md,decimal







def main():
  x = input("Enter numbers to be sorted:" )
  print avg(x)

if __name__ == '__main__':
  main()








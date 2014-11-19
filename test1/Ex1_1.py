import sys
def mabna(n):
    dict={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    s=n/16
    n=n%16
    k=s/16
    while (s>16):
        s=s%16
        if s>9:
            list= dict[s]
        else:
           list= s
    w=str(k)+str(s)+str(n)
    return w




def main():
    x = input("Enter your numbers:" )
    print mabna(x)



if __name__ == '__main__':
  main()
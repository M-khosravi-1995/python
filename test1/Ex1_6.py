import sys

def y_d(x):
    list=["Jan","Feb","Mar","Apr","may","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    c=31
    v=x/c
    w=x%c
    if w>30:
        b=w/30
        w=w%30
        a=v+b
    else:
        a=v
    if a>12:
        a = a-12

    return (str(w)+list[a-1])



def main():
    x = input("Enter your numbers:" )
    print y_d(x)


if __name__ == '__main__':
  main()

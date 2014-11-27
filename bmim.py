__author__ = 'esy'
def bmim(x,y):
    if y==0:
     return x
    else:
     n=x%y
     return  bmim(y,n)


if __name__ == '__main__':
    x=[15,9]
    print bmim(15,9)
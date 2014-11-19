import sys


def robat(list1):
    x=0
    y=0
    list3=[]

    for i in range(len(list1)):
        if list1[i]=="R":
            x+=1
        elif list1[i]=="L":
            x-=1
        elif list1[i]=="U":
            y+=1
        elif list1[i]=="D":
            y-=1
        list2=(x,y)
        list3.append(list2)
    return list3






def main():
    list=['R','U','U','L','L','L','D','D','D','R','R']
    print robat(list)


if __name__ == '__main__':
  main()
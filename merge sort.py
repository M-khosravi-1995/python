def merge_sort(q):
    if len(q) < 2: return q
    m = len(q) / 2
    return merge(merge_sort(q[:m]), merge_sort(q[m:]))

def merge(l, r):
    list = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            list.append(l[i])
            i += 1
        else:
            list.append(r[j])
            j += 1
    list += l[i:]
    list += r[j:]
    return list


def main():
  list1=[5,4,3,2,1]
  list2=[9,5,3,4]
  print merge_sort(list1)
  print merge_sort (list2)


if __name__ == '__main__':
  main()
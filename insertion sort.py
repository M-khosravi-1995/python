def sort_numbers(s):
    for i in range(1, len(s)):
        r = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > r):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = r

def main():
    x=[3,2,1]
    x = list(x)
    sort_numbers(x)
    print(x)


if __name__ == '__main__':
  main()
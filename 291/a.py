from sys import stdin
s = stdin.readline().strip()
def main(s):
    sn = len(s)
    for i in range(sn):
        if s[i].isupper():
            print(i+1)
            break

if __name__ == '__main__':
    main(s)
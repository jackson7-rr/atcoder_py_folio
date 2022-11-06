from sys import stdin 
s = stdin.readline()
temp = []
def main(s):
    if 'a' not in s:
        print(-1)
        exit()
    else:
        for i in range(len(s)):
            if s[i] == 'a':
                temp.append(i+1)
    print(temp[-1])
if __name__ == '__main__':
    main(s)
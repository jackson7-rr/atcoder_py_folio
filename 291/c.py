from sys import stdin
n = int(stdin.readline().strip())
s = stdin.readline().strip()
def main(n,s):
    loge = set()
    loge.add(0)
    direction = {'R':n,'L':-n,'U':1,'D':-1}
    sp = 0
    for i in range(n):
        sp += direction[s[i]]
        if sp in loge:
            print('Yes')
            #print(loge)
            exit()
        else:
            loge.add(sp)
    print('No')
    #print(loge)
if __name__ == '__main__':
    main(n,s)
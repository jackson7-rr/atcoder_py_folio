from sys import stdin 
from collections import Counter
s = stdin.readline().strip()
t = stdin.readline().strip()
def main(s,t):
    """
    sd = Counter(s)
    td = Counter(t)
    td.subtract(sd)
    ind = td.most_common(1)[0][0]
    """
    for i in range(len(t)-1):
        
        if s[i] != t[i]:
            ans = i
            break
        i = len(t)-1
    print(i+1)
if __name__ == '__main__':
    main(s,t)